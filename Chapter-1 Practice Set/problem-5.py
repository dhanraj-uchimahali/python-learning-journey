# 5. Label the program written in problem 4 with comments.
import os

# Get the list of files and directories in the specified path
directory_path = "/"

# Use the os module to list the directory content
contents = os.listdir(directory_path)

# Print the contents of the directory
print(contents)