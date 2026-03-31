import import_python_module.mod1 as mod1
import import_python_module.mod2 as mod2

def main():
    print("This is the main function.")
    mod1.load_data()
    mod2.clean_data()

if __name__ == "__main__":
    main()      
    