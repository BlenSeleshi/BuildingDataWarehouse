import os
#import shutil

def remove_duplicate_images_by_size(folder_path):
    """Removes duplicate images based on their size from a given folder.

    Args:
        folder_path (str): The path to the folder containing the images.
    """

    # Create a dictionary to store image sizes and their corresponding paths
    image_sizes = {}

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Get the file size
            file_size = os.path.getsize(file_path)

            # If the file size is already in the dictionary, it's a duplicate
            if file_size in image_sizes:
                # Remove the duplicate file
                os.remove(file_path)
                print(f"Removed duplicate: {filename}")
            else:
                # Add the file size and path to the dictionary
                image_sizes[file_size] = file_path

