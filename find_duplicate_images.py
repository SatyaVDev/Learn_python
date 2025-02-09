import hashlib
import os
import shutil

# Define the base path (common part) for both source and duplicate folders
base_path = "D:\Camera"  # Using relative path for Images

# Define source and duplicate folder paths by appending folder names to the base path
source_folder = os.path.join(
    base_path, "source_folder"
)  # Replace with your source folder name
duplicate_folder = os.path.join(
    base_path, "duplicate_folder"
)  # Replace with your duplicate folder name

# List of image extensions to consider
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

# Create the duplicate folder if it doesn't exist
if not os.path.exists(duplicate_folder):
    os.makedirs(duplicate_folder)


def get_image_hash(image_path):
    """Generate a hash for an image file"""
    hash_md5 = hashlib.md5()
    with open(image_path, "rb") as f:
        # Read file in chunks
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def find_and_move_duplicates(source_folder, duplicate_folder):
    """Find duplicates in the source folder and move them to duplicate_folder"""
    seen_hashes = {}
    duplicate_count = 0

    print(f"Scanning folder: {source_folder}")

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()

            # Only process files with image extensions
            if file_extension in image_extensions:
                file_path = os.path.join(root, file)

                # Generate a hash for the current image
                image_hash = get_image_hash(file_path)

                # Check if the hash is already seen (duplicate)
                if image_hash in seen_hashes:
                    duplicate_count += 1
                    print(f"Duplicate found: {file} -> Moving to {duplicate_folder}")
                    shutil.move(file_path, os.path.join(duplicate_folder, file))
                else:
                    seen_hashes[image_hash] = file_path

    print(f"Total duplicates moved: {duplicate_count}")


# Run the function
print("Starting the duplicate image detection process...")
find_and_move_duplicates(source_folder, duplicate_folder)
print("Process completed!")
