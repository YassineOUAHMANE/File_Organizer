import os
import shutil

def organize_files(directory):
    """
    Organizes files in the specified directory into subdirectories based on their extensions.
    
    Args:
        directory (str): The path of the directory to organize.
    """
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # Iterate through all files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        file_extension = os.path.splitext(file_name)[1].lower()
        
        # If there's no extension, skip the file
        if not file_extension:
            continue
        
        # Create a subdirectory for the file extension if it doesn't exist
        subdirectory = os.path.join(directory, file_extension[1:])  # Remove the dot in the extension
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)
        
        # Move the file to the appropriate subdirectory
        shutil.move(file_path, os.path.join(subdirectory, file_name))
        print(f"Moved '{file_name}' to '{subdirectory}'")

if __name__ == "__main__":
    # Specify the directory to organize
    directory_to_organize = input("Enter the directory to organize: ").strip()
    organize_files(directory_to_organize)
