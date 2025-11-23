# f = open('demo.txt','rt')
#
# print(f.read())
# f.close()

# with open("demo.txt", 'rt') as f:
  # print(f.read())
  # print(f.read(14)) #Read specific characters
  # print(f.readline()) #Read one line
  # print(f.readline()) #Read one line
  # for x in f:
  #     print(x)

# with open('demo.txt', 'a') as f:
#     f.write("This is new line")

# f = open("myfile.txt", "x") # Create new file but throw error if the file already exists
# f.close()

# f = open("myfile.txt", "w") # Create new file but  the file does not exist
# f.close()

import os

# os.remove("myfile.txt") # Remove file

# if os.path.exists("myfile.txt"):
#     os.remove("myfile.txt")
# else:
#     print("The file does not exist")

# os.rmdir("myfolder") # Remove empty directory




