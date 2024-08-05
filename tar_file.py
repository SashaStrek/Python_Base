import tarfile
import os

# Define the file path and the tar file path
file_path = "/Users/astrekal/someTestData/111.root"
tar_path = "/Users/astrekal/someTestData/111.tar"

def create_tar_file(file_path, tar_path):
    with tarfile.open(tar_path, "w") as tar:
        # Add the file to the tar archive
        tar.add(file_path, arcname=os.path.basename(file_path))

# Create the tar file
create_tar_file(file_path, tar_path)

print(f"Tar file created at: {tar_path}")
