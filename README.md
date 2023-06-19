# Unsplash Wallpaper Downloader

A Python script for automatically downloading wallpapers from Unsplash.

## Installation

1. Clone this repository.
2. Install the dependencies with Poetry: `poetry install`

## Usage

Run the script with Python: `poetry run python main.py`

You can customize the script's behavior by setting environment variables in a `.env` file:

- `UNSPLASH_ACCESS_KEY`: Your Unsplash API access key. This is required.
- `DEFAULT_SAVE_LOCATION`: The directory where wallpapers will be saved. Default is `~/wallpapers`.
- `DEFAULT_RESOLUTION`: The resolution of the downloaded wallpapers. Default is `regular`.
- `DEFAULT_NUMBER`: The number of wallpapers to download. Default is `5`.
- `DEFAULT_ORIENTATION`: The orientation of the downloaded wallpapers. Default is `landscape`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
