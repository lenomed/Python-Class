import os

from pathlib import Path

def remove_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been removed.")
    else:
        print(f"File '{file_path}' does not exist.")
if __name__ == "__main__":
    file_to_remove = Path("path/to/your/file.txt")
    remove_file(file_to_remove)
    
remove_file("path/to/your/file.txt")
        
 #coping a file
 
#import shutil
#shutil.copy() copies a file and preserves the file's metadata, such as permissions and timestamps. It is used when you want to create a duplicate of a file while keeping its original attributes intact.
#shutil.copy2() also copies a file but includes additional metadata, such as extended attributes and ACLs (Access Control Lists). It is used when you want to create a duplicate of a file while preserving as much metadata as possible, including extended attributes and ACLs.       
#shutil.copytree() is used to copy an entire directory tree, including all files and subdirectories. It is used when you want to create a duplicate of a directory and its contents while preserving the directory structure and metadata.  
#shutil.move() is used to move a file or directory from one location to another. It is used when you want to relocate a file or directory without creating a duplicate. The original file or directory will be removed from its original location after the move operation is completed.    
#shutil.rename() is used to rename a file or directory. It is used when you want to change the name of a file or directory without moving it to a different location. The original file or directory will be renamed to the new name specified in the function call.    
