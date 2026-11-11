from pathlib import Path
import urllib.request
import zipfile

def download_visdrone_val(dest: Path)->Path:
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/VisDrone2019-DET-val.zip"
    zip_path = dest / "VisDrone2019-DET-val.zip"
    extracted_folder = dest / "VisDrone2019-DET-val"

    if not zip_path.exists():
        print(f"Downloading VisDrone validation split from {url}...")
        urllib.request.urlretrieve(url, zip_path)
    else:
        print(f"Zip file already found at {zip_path}, skipping download.")

    if not extracted_folder.exists():
        print(f"Extracting archive to {dest}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zipfile.ZipFile(...).testzip()
            zip_ref.extractall(dest)

    else:
        print(f"Extracted folder already exists at {extracted_folder}, skipping extraction.")

    return extracted_folder