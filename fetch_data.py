import os
import tarfile
import urllib.request

# -----------------------------
# Config
# -----------------------------
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

# Project root (folder containing this fetch_data.py)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Folder to store the dataset
HOUSING_PATH = os.path.join(PROJECT_ROOT, "datasets", "housing")


# -----------------------------
# Function to fetch the dataset
# -----------------------------
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    Downloads and extracts the California housing dataset to the specified folder.
    """
    # Make sure the folder exists
    os.makedirs(housing_path, exist_ok=True)
    
    tgz_path = os.path.join(housing_path, "housing.tgz")
    
    # Download the file
    print(f"Downloading {housing_url} → {tgz_path} ...")
    urllib.request.urlretrieve(housing_url, tgz_path)
    
    # Extract the tar.gz
    print(f"Extracting {tgz_path} ...")
    with tarfile.open(tgz_path) as housing_tgz:
        housing_tgz.extractall(path=housing_path)
    
    print(f"Dataset ready at: {housing_path}")


# -----------------------------
# Optional: run automatically if script is executed
# -----------------------------
if __name__ == "__main__":
    fetch_housing_data()