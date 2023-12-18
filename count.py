import os

def count_subdirectories_and_files(root_directory):
    # Initialize counters
    subdirectory_count = 0
    files_per_subdirectory = {}

    # Iterate over all items (directories and files) in the root_directory
    for root, dirs, files in os.walk(root_directory):
        # Skip the root_directory itself
        if root != root_directory:
            # Increment subdirectory count for each subdirectory
            subdirectory_count += 1

            # Count the number of files in the current subdirectory
            files_per_subdirectory[root] = len(files)

    # Print the results
    print(f"Total subdirectories: {subdirectory_count}")
    print("Files per subdirectory:")
    for subdirectory, file_count in files_per_subdirectory.items():
        print(f"{subdirectory}: {file_count} files")

# Replace 'D:\\sign to speak\\Dataset\\Data2' with your actual directory path
directory_path = r'D:\sign to speak\Dataset\Data2'
count_subdirectories_and_files(directory_path)
