#!/bin/bash

# Define the directory and filename
dir="$HOME/.config/autostart"
file="unsplash_wallpaper_downloader.desktop"
current_dir=$(pwd)

# Check if the directory exists and create it if it doesn't
if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
fi

# Create the .desktop file
# add the path to the main.py file
echo "[Desktop Entry]
Type=Application
Exec=/bin/bash -c 'cd $current_dir && poetry run python main.py'
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=Unsplash Wallpaper Downloader
Name=Unsplash Wallpaper Downloader
Comment[en_US]=Download wallpapers from Unsplash at startup
Comment=Download wallpapers from Unsplash at startup" > "$dir/$file"

# Make the .desktop file executable
chmod +x "$dir/$file"
