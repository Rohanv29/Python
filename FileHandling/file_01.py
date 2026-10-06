# Making a file
file = open("data.txt", "w")
file.write("Hello all\n")
file.write("Hope you are doing good in life!\n")
file.write("Copyright by and for Rohan Verma Corp. Ltd.")
file.close()
print("File edited successfully!\n")

# Read Operation
file = open("data.txt", "r")
data = file.read()
print(data)
file.close()

# Append mode
file = open("data.txt", "a")
file.write(
    "\nAll rights reserved for this program by Ishaan Goswami Corp. Ltd."
)
file.write(
    "\nLegal issues shall be validated upon plagiarism of the program by any unauthorised personnel."
)
file.close()
print("\nFile edited successfully!\n")

# Read Operation
file = open("data.txt", "r")
data = file.read()
print(data)
file.close()

# Reading first two lines
with open("data.txt", "r") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")

# Reading all lines sequentially (Fixed line iteration)
with open("data.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())

# Appending legal jurisdiction line
with open("data.txt", "a") as file:
    file.write("\nAll rights are reserved under the jurisdiction of the law of Ishaan Goswami' Constitution of the Republic of IG country\n")

# Final Read Operation (Added print to display)
with open("data.txt", "r") as file:
    print(file.read())

try:
    with open("newFile.txt","x") as file:
        file.write("New File")
except FileExistsError:
    print("File already exists")

with open("newFile.txt","r") as file:
    print("Name: ", file.name)
    print("Mode: ", file.mode)
    print("Readable: ", file.readable)
    print("Writable: ", file.writable)
    print("Closed inside with: ", file.closed)