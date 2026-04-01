import os
from pathlib import Path

try:
   os.mkdir('new_directory')


   with open('new_directory/new_file.txt', 'w') as file:
    file.write('This is a new file in the new directory.')
except FileExistsError:
    pass  

  

line = ' This line is appended to the new file.'    
     
with open('new_directory/new_file.txt', 'r') as file:
    content = file.read()
    print(content)  
if line not in content:    
    with open('new_directory/new_file.txt', 'a') as file:
        file.write(line)
        
        
      
# the mkdir() is creats a single subdirectory with a give name, and it will raise a FileExistsError if the directory already exists.
# the makedirs() is creats a directory and all intermediate directories if they do not exist, and it will raise a FileExistsError if the directory already exists.     
#pathlib.Path.mkdir() is a method of the Path class in the pathlib module, and it is used to create a directory at the specified path. It has similar functionality to os.mkdir(), but it is more object-oriented and provides additional features.
# the rmdir() is removes a single empty directory, and it will raise a FileNotFoundError if the directory does not exist, and it will raise an OSError if the directory is not empty.
# the removedirs() is removes a directory and all intermediate directories, and it will raise a FileNotFoundError if the directory does not exist, and it will raise an OSError if any of the directories are not empty.

#os.rmdir() removes a single empty directory, and it will raise a FileNotFoundError if the directory does not exist, and it will raise an OSError if the directory is not empty.    
#pathlib.Path.rmdir() is a method of the Path class in the pathlib module, and it is used to remove a directory at the specified path. It has similar functionality to os.rmdir(), but it is more object-oriented and provides additional features. 
#shutil.rmtree() is a function in the shutil module that is used to remove a directory and all its contents, including subdirectories and files. It will raise a FileNotFoundError if the directory does not exist, and it will raise an OSError if any of the files or directories cannot be removed.  

#import shutil 
# shutil.rmtree() is a function in the shutil module that is used to remove a directory and all its contents, including subdirectories and files. It will raise a FileNotFoundError if the directory does not exist, and it will raise an OSError if any of the files or directories cannot be removed. 