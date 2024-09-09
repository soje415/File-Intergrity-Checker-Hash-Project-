import os
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                sha256_hash.update(data)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    
    return sha256_hash.hexdigest()

def check_integrity(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' does not exist")
        return

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            if calculated_hash:
                print(f"File: {file_path}\nSHA-256 Hash: {calculated_hash}")

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check integrity: ")
    check_integrity(directory_to_check)
