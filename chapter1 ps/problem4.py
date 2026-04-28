import os

def list_directory_contents(path="."):
    try:
        items = os.listdir(path)
        print(f"Contents of '{os.path.abspath(path)}':\n")
        
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")
                
    except FileNotFoundError:
        print("Error: The directory does not exist.")
    except PermissionError:
        print("Error: Permission denied.")

if __name__ == "__main__":
    list_directory_contents(".")

