import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt user for an image URL
    url = input("Enter the image URL: ").strip()

    # Directory to store fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Try fetching the image
        print("Fetching image from the web community...")
        response = requests.get(url, timeout=10)

        # Check for HTTP errors
        response.raise_for_status()

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # Generate fallback filename if missing
        if not filename:
            filename = "downloaded_image.jpg"

        # Create full path
        file_path = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully saved to: {file_path}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include 'http://' or 'https://'.")
    except requests.exceptions.Timeout:
        print("⚠️ Connection timed out. Please check your internet connection.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error occurred: {e}")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
