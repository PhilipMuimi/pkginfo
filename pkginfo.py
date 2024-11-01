import sys
import os

def list_packages(filename):
    """Prints package names in the order they appear in the file."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        if not lines:
            print("No packages installed")
        else:
            print("Installed packages:")
            for line in lines:
                parts = line.strip().split(',')
                print(parts[1])

def total_size(filename):
    """Calculates and prints the total size in kilobytes of all packages."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        if not lines:
            print("Total size in kilobytes: 0")
        else:
            total = sum(int(line.strip().split(',')[3]) for line in lines)
            print(f"Total size in kilobytes: {total}")

def package_info(filename, package_name):
    """Finds and prints details of a specified package by name."""
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if parts[1] == package_name:
                print(f"Package: {parts[1]}")
                print(f"Category: {parts[0]}")
                print(f"Description: {parts[2]}")
                print(f"Size in kilobytes: {parts[3]}")
                return
        print("No installed package with this name")

def author_info():
    """Prints author information."""
    print("Author: Your Name")
    print("Surname: Your Surname")
    print("Student ID: YourStudentID")
    print("Completion Date: 1 November 2024")

def main():
    # Ensure the correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: python pkginfo.py option argument_file")
        sys.exit(1)
    
    option = sys.argv[1]
    filename = sys.argv[2]

    # Verify the argument file exists, is a file, and is readable
    if not os.path.isfile(filename):
        print("Error: Argument file does not exist or is not a file.")
        sys.exit(1)
    
    # Handle each option accordingly
    if option == '-a':
        list_packages(filename)
    elif option == '-s':
        total_size(filename)
    elif option == '-l':
        if len(sys.argv) != 4:
            print("Usage: python pkginfo.py -l name argument_file")
            sys.exit(1)
        package_name = sys.argv[3]
        package_info(filename, package_name)
    elif option == '-v':
        author_info()
    else:
        print("Error: Invalid option.")
        print("Valid options are -a, -s, -l <name>, -v")
        sys.exit(1)

if __name__ == "__main__":
    main()
