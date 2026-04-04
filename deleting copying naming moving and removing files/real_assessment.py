name = input("Enter your name: ").strip()

while not name:
    print("Name cannot be empty. Please enter a valid name.")
    name = input("Enter your name: ").strip()
file_path = r"C:\Users\megam\Desktop\Python Class\deleting copying naming moving and removing files\customer.txt"

try:
    with open(file_path, "r") as file:
        users = file.read().splitlines()
except FileNotFoundError:
    users = []

if name in users:
    print("Name already exists in the file.")   
else:
    with open(file_path, "a") as file:
        file.write(name + "\n")

print("Name saved successfully!")