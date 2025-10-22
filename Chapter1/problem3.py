import os

# Specify the directory you want to access
directory_path = '/'  # Replace with your actual path

contents = os.listdir(directory_path)

for item in contents:
    print(item)