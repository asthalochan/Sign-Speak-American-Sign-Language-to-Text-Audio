import os
import random
from shutil import copyfile

def split_dataset(input_folder, output_folder, train_ratio=0.8, test_ratio=0.1, val_ratio=0.1, seed=None):
    # Set random seed for reproducibility
    random.seed(seed)

    # Ensure output folders exist
    for split in ['train', 'test', 'val']:
        split_path = os.path.join(output_folder, split)
        os.makedirs(split_path, exist_ok=True)

    # Iterate through class folders
    for class_folder in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_folder)

        # Skip if not a directory
        if not os.path.isdir(class_path):
            continue

        # Collect video files in the class folder
        video_files = [f for f in os.listdir(class_path) if f.endswith('.mp4')]

        # Shuffle the list of video files
        random.shuffle(video_files)

        # Calculate split indices
        train_split = int(train_ratio * len(video_files))
        test_split = train_split + int(test_ratio * len(video_files))

        # Copy files to respective split folders
        for i, video_file in enumerate(video_files):
            source_path = os.path.join(class_path, video_file)

            if i < train_split:
                destination_folder = 'train'
            elif i < test_split:
                destination_folder = 'test'
            else:
                destination_folder = 'val'

            destination_path = os.path.join(output_folder, destination_folder, class_folder, video_file)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            copyfile(source_path, destination_path)

if __name__ == "__main__":
    # Specify your dataset and output folders
    output_folder = r"D:\sign to speak\Dataset\split_dataset_test"
    input_folder = r"D:\sign to speak\Dataset\Data2"

    # Set the ratio for train, test, and val splits
    train_ratio = 0.8
    test_ratio = 0.1
    val_ratio = 0.1

    # Set a random seed for reproducibility (optional)
    seed = 42

    # Split the dataset
    split_dataset(input_folder, output_folder, train_ratio, test_ratio, val_ratio, seed)
