def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the entire content of the file

        # Modify the content (for example, converting to uppercase)
        modified_content = content.upper()  # Example modification

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully wrote modified content to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")

# Ask the user for the input filename and output filename
input_file = input("Enter the name of the file to read: ")
output_file = input("Enter the name of the file to write to: ")

# Call the function
read_and_modify_file(input_file, output_file)