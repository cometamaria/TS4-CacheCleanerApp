import os
import shutil
import json

FOLDER = "../../Electronic Arts/The Sims 4/"  # change this to your folder path
JSON_FILE = "ts4_cachedata.json"

def load_items(json_file):
    """Load the list of files and folders from a JSON file."""
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
        files = data.get("files", [])
        folders = data.get("folders", [])
        return files, folders
    except FileNotFoundError:
        print(f"{json_file} not found.")
        return [], []
    except json.JSONDecodeError:
        print(f"Error decoding {json_file}.")
        return [], []

def remove_files(folder, file_list):
    """Remove the files listed in file_list from the folder."""
    for filename in file_list:
        if filename.endswith("*"):  # treat as prefix
            prefix = filename[:-1]
            for f in os.listdir(folder):
                if f.startswith(prefix):
                    path = os.path.join(folder, f)
                    if os.path.isfile(path):
                        os.remove(path)
                        print(f"Removed file by prefix: {f}")
        else:  # exact file match
            path = os.path.join(folder, filename)
            if os.path.isfile(path):
                os.remove(path)
                print(f"Removed file: {filename}")
            else:
                print(f"File not found: {filename}")

def remove_folders(folder, folder_list):
    """Remove the folders listed in folder_list from the folder, including their contents."""
    for foldername in folder_list:
        path = os.path.join(folder, foldername)
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Removed folder: {foldername}")
        else:
            print(f"Folder not found: {foldername}")

def main():
    files, folders = load_items(JSON_FILE)
    
    if not files and not folders:
        print("No files or folders to remove.")
        return

    remove_files(FOLDER, files)
    remove_folders(FOLDER, folders)

if __name__ == "__main__":
    main()