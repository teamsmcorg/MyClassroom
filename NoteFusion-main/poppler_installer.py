import os
import platform
import requests
import shutil
import tarfile
import tempfile
import zipfile


def download_and_install_poppler():
    system = platform.system()

    # Define the download URL based on the system type
    if system == "Windows":
        download_url = "https://poppler.freedesktop.org/poppler-21.05.0.tar.xz"
        extract_folder = "poppler-21.05.0"
    elif system == "Linux":
        download_url = "https://poppler.freedesktop.org/poppler-21.05.0.tar.xz"
        extract_folder = "poppler-21.05.0"
    elif system == "Darwin":
        download_url = "https://poppler.freedesktop.org/poppler-21.05.0.tar.xz"
        extract_folder = "poppler-21.05.0"
    else:
        print("Unsupported operating system.")
        return

    # Download the Poppler archive
    print("Downloading Poppler...")
    response = requests.get(download_url, stream=True)
    response.raise_for_status()

    # Create a temporary directory for extraction
    temp_dir = tempfile.mkdtemp(prefix="poppler_temp")
    os.makedirs(temp_dir, exist_ok=True)

    # Save the archive to a file
    archive_path = os.path.join(temp_dir, "poppler.tar.xz")
    with open(archive_path, "wb") as file:
        shutil.copyfileobj(response.raw, file)

    # Extract the archive contents
    print("Extracting Poppler...")
    with tarfile.open(archive_path, "r:xz") as tar_file:
        tar_file.extractall(temp_dir)

    # Move the extracted folder to the desired location
    extracted_path = os.path.join(temp_dir, extract_folder)
    install_dir = os.path.join(os.getcwd(), extract_folder)

    # Check if the destination directory exists
    if os.path.exists(install_dir):
        print("Poppler is already installed. Skipping installation.")
        shutil.rmtree(temp_dir)
        return

    shutil.move(extracted_path, install_dir)

    # Add Poppler to the system PATH
    print("Adding Poppler to the system PATH...")
    path_var = os.environ.get("PATH", "")
    os.environ["PATH"] = install_dir + os.pathsep + path_var
    
    print("Poppler installation completed.")
    print("Please make sure to restart your Streamlit Cloud app for the PATH changes to take effect.")


# Usage
download_and_install_poppler()
