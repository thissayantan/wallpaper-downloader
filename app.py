from dotenv import load_dotenv
import os
import requests
from urllib.parse import urljoin
from pathlib import Path

# Load environment variables from .env file
load_dotenv()


def download_images(
    query="minimal colorful dark",
    resolution="regular",
    number=10,
    directory=None,
    orientation="landscape",
):
    # Get Unsplash API access key from environment variables
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")

    # If no directory is provided, get the default directory from environment variables
    # If that's also not set, use "~/wallpapers" as the default directory
    if directory is None:
        directory = os.getenv("DEFAULT_SAVE_LOCATION", "~/wallpapers")

    # Convert the directory path to an absolute path (in case it's relative)
    directory = Path(directory).expanduser()

    # Create the directory if it doesn't exist
    directory.mkdir(parents=True, exist_ok=True)

    # Set the headers and parameters for the API request
    headers = {"Authorization": f"Client-ID {access_key}"}
    params = {"query": query, "per_page": number, "orientation": orientation}

    # Send a GET request to the Unsplash API
    response = requests.get(
        "https://api.unsplash.com/search/photos", headers=headers, params=params
    )

    # If the request was unsuccessful, raise an exception
    response.raise_for_status()

    # Parse the JSON response
    results = response.json()["results"]

    # For each image in the results...
    for result in results:
        # Get the URL of the image in the requested resolution
        image_url = result["urls"][resolution]

        # Get the ID of the image
        image_id = result["id"]

        # Construct the path where the image will be saved
        image_path = directory / f"{image_id}.jpg"

        # Send a GET request to download the image
        with requests.get(image_url, stream=True) as r:
            # If the request was unsuccessful, raise an exception
            r.raise_for_status()

            # Save the image to the file
            image_path.write_bytes(r.content)


if __name__ == "__main__":
    download_images()
