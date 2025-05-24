import os


print("Current Directory:", os.getcwd())



#
#
# os.mkdir("my_new_folder")


files = os.listdir("..")  # "." means current directory
print("Files and Folders:", files)
#
# os.rmdir("my_new_folder")
#
# os.rename("sampl.py", "sample_example.py")
#
if os.path.exists("sample_example.py"):
    print("File exists!")
else:
    print("File not found.")


# create a program to write into file

# Open the file in write mode (creates file if not exists)
with open("../exception_handlings/output.txt", "a") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.\n")
    # file.read()

print("Data written to file successfully.")