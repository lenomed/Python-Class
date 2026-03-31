with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n")
    
with open("file.txt", "r") as file:
       content = file.read()
       print(content)
       
with open("file.txt", "a") as file:
    
    file.write("This line is appended to the file.\n")
    
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
    
with open("file.txt", "w") as file:
    file.write("This line overwrites the previous content.\n")
 
with open("file.txt", "r") as file:
    content = file.read()
    print(content)           
    
file.close()    