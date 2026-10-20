import os
import shutil

def move_jpg_files(source_dir):
    # Target folder name for JPG images
    target_dir = os.path.join(source_dir, "JPEG_Images")

    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Directory {source_dir} does not exist.")
        return

    # Create target folder if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created directory: {target_dir}")

    files_moved = 0

    # Scan files in the source directory
    for filename in os.listdir(source_dir):
        # Match .jpg and .jpeg extensions (case-insensitive)
        if filename.lower().endswith(('.jpg', '.jpeg')):
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_dir, filename)

            # Skip directories
            if os.path.isdir(source_path):
                continue

            # Move file
            shutil.move(source_path, target_path)
            print(f"Moved: {filename} --> JPEG_Images/")
            files_moved += 1

    print("\n=================")
    print(f"Task Complete! Total .jpg files moved: {files_moved}")
    print("===================")

if __name__ == '__main__':
    print("=== TASK AUTOMATION: MOVE JPG FILES ===")
    folder_path = input("Enter path of the folder to organize (or press Enter for current directory): ").strip()

    if not folder_path:
        folder_path = "."  # Default to current directory

    move_jpg_files(folder_path)