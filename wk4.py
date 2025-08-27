# File handling and exceptional handling assignment
f = open ('file', 'w')
f.write("A programming enthusiast") 

f = open ('file', 'r')
print(f.read())

f = open ('file', 'a')
f.write("Xenon codes the most exceplary code")


def read_file():
    filename = input("Enter the filename: ")
try:
        with open('file', "r") as f:
            content = f.read()
            print("\n--- File Content ---")
            print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
else:
    print("\nFile read successfully.")
finally:
    print("Exiting program...")

read_file()