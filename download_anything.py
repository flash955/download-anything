import requests
import os

def download_file(url, save_as=None):
    try:
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()

        if not save_as:
            save_as = url.split("/")[-1] or "downloaded_file"

        with open(save_as, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"✅ Download complete: {save_as}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🌍 Simple Download Anything CLI Tool")
    url = input("Enter the file URL: ").strip()
    filename = input("Enter filename (or leave blank to auto-detect): ").strip()
    if filename == "":
        filename = None
    download_file(url, filename)
