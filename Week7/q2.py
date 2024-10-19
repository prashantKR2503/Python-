def read_file(file_name):
    """Reads all the lines from a file and returns them as a list"""
    with open(file_name, 'r') as file:
        return file.readlines()


def write_file(file_name, lines):
    """Writes the modified lines back to the file"""
    with open(file_name, 'w') as file:
        file.writelines(lines)


def swap_lines(file1, file2):
    # Read both files
    file1_lines = read_file(file1)
    file2_lines = read_file(file2)

    # Find the middle index for the first file (odd number of lines)
    middle_index = len(file1_lines) // 2

    # Get the last line from the second file
    last_line_index = len(file2_lines) - 1

    # Swap the middle line of file1 with the last line of file2
    file1_lines[middle_index], file2_lines[last_line_index] = file2_lines[last_line_index], file1_lines[middle_index]

    # Write the updated content back to the files
    write_file(file1, file1_lines)
    write_file(file2, file2_lines)


# Main function
def main():
    file1 = 'file1.txt'
    file2 = 'file2.txt'

    swap_lines(file1, file2)
    print(f"Swapped the middle line of {file1} with the last line of {file2}")


# Run the program
if __name__ == '__main__':
    main()
