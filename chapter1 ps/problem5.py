import os

def list_directory_contents(path="."):
    try: 
        # Get the list of all files and directories
        items = os.listdir(path)
        print(f"Contents of '{os.path.abspath(path)}':\n")
        
        for item in items:
            # Join the path to check if its a file or directory
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
    # Change '.' to any specific path you want to inspect
    list_directory_contents(".")