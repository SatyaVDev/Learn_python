import os


def print_and_delete_empty_folders(folder_path):
    # topdown=False ensures we process subdirectories first
    for root, dirs, files in os.walk(folder_path, topdown=False):
        # Check if the directory is empty
        if not dirs and not files:  # No files and no subdirectories
            print(f"Empty folder: {root}")  # Print the empty folder name
            os.rmdir(root)  # Delete the empty folder


# Use raw string (r'') for the path
folder_path = r'C:\Users\Satish\OneDrive\Documents'
print_and_delete_empty_folders(folder_path)
