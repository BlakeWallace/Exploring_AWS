'''Functions in this notebook

1. read_text_files - Read in text
2. read_transform_text_files - Read in and transform text files

'''


import os
import datacleaning as dc

def read_text_files(folder_path):
    """
    Reads all text files in a specified folder and returns their content.

    Args:
        folder_path (str): The path to the folder containing the text files.

    Returns:
        dict: A dictionary where keys are file names and values are file contents.
               Returns an empty dictionary if the folder does not exist or 
               no text files are found.
    """
    file_contents = {}
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return file_contents
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r') as file:
                    file_contents[filename] = file.read()
            except Exception as e:
                 print(f"Error reading {filename}: {e}")
    return file_contents


def read_transform_text_files(folder_path):
    """
    Reads all text files in a specified folder and returns their content.

    Args:
        folder_path (str): The path to the folder containing the text files.

    Returns:
        dict: A dictionary where keys are file names and values are file contents.
               Returns an empty dictionary if the folder does not exist or 
               no text files are found.
    """
    file_contents = {}
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return file_contents
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                file_contents[filename] = dc.clean_document(dc.sentTokenizer(dc.cleanFile(file_path)))
            except Exception as e:
                 print(f"Error reading {filename}: {e}")
    return file_contents