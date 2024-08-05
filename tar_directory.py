import tarfile
import os

# Define the directory path and the tar file path
directory_path = "/Users/astrekal/someTestData"
tar_path = "/Users/astrekal/someTestData/full_dir.tar"

def get_directory_size(directory_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def check_disk_space_ok(destination_path, required_space):
    # Get the available disk space in the destination directory
    statvfs = os.statvfs(destination_path) # os.statvfs() function returns an object that contains information about the file system. 
    available_space = statvfs.f_frsize * statvfs.f_bavail # f_frsize: The fragment size (or block size) used in the file system; f_bavail: The number of free blocks available to non-superuser processes.
    # print(f"availeble space is {available_space} bytes")
    return available_space >= required_space

def create_tar_file(directory_path, tar_path):
    with tarfile.open(tar_path, "w") as tar:
        # Add the directory to the tar archive
        # tarfile module in Python handle subdirectories and their files recursively, so There is no need for a separate recursive function.
        # When you create a TARBALL (.tar) of a directory, it sequentially archives all the files and subdirectories within that directory, 
        # preserving their metadata. The metadata includes file permissions, ownership, timestamps, and directory structure.
        #tar.add(directory_path, arcname='.')
        tar.add(directory_path, arcname=os.path.basename(directory_path))

# Check if there is enough space in the destination directory
total_size = get_directory_size(directory_path)
destination_dir = os.path.dirname(tar_path)
if not check_disk_space_ok(destination_dir, total_size):
    print("Not enough space in the destination directory to create the tar file.")
else:
    # Create the tar file
    create_tar_file(directory_path, tar_path)
    print(f"Tar file created at: {tar_path} with size {os.path.getsize(tar_path)} bytes")
