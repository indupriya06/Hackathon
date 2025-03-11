import os
import shutil

# Define the paths
path_v = r"C:\Users\Indhu\Downloads\v"
path_ai = r"C:\Users\Indhu\Downloads\AI Receptionalist"

# Verify paths exist
if not os.path.exists(path_v):
    print(f"Path does not exist: {path_v}")
if not os.path.exists(path_ai):
    print(f"Path does not exist: {path_ai}")

# Function to list files in a directory
def list_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# List files in both directories
files_v = list_files(path_v)
files_ai = list_files(path_ai)

# Check if directories are empty
if not files_v:
    print("No files found in 'v' directory.")
if not files_ai:
    print("No files found in 'AI Receptionalist' directory.")

# Print files in both directories
print("Files in 'v' directory:")
for file in files_v:
    print(file)

print("\nFiles in 'AI Receptionalist' directory:")
for file in files_ai:
    print(file)

# Example: Copy all files from 'v' to 'AI Receptionalist'
for file in files_v:
    shutil.copy(file, path_ai)

print("\nFiles copied from 'v' to 'AI Receptionalist'.")
print("Files in 'v':", os.listdir(path_v))
print("Files in 'AI Receptionalist':", os.listdir(path_ai))