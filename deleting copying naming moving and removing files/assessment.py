def user_input_data():
    user_input = input("Enter your name: ").strip()
    file_path = "user_data.txt"

    try:
        with open(file_path, "r") as f:
            users = f.read().splitlines()
    except FileNotFoundError:
        users = []

    if user_input in users:
        print("User already exists ❌")
    else:
        with open(file_path, "a") as f:
            f.write(user_input + "\n")
        print("User added ✅")

        # show updated content
        with open(file_path, "r") as f:
            print(f.read())

user_input_data()
