import os
def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"File '{filepath}' deleted successfully.")
    else:
        print(f"File '{filepath}' does not exist.")


filepath = 'trash.txt'
delete_file(filepath)