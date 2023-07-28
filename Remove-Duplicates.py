def remove_duplicates(input_file, output_file):
    try:
        # Set to store seen lines
        seen_lines = set()

        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Remove leading/trailing whitespaces and newline characters
                cleaned_line = line.strip()

                # Check if the line is not empty and not seen before
                if cleaned_line and cleaned_line not in seen_lines:
                    # Write the unique line to the output file
                    outfile.write(cleaned_line + '\n')
                    # Add the line to the set of seen lines
                    seen_lines.add(cleaned_line)

        print("Successfully removed duplicate lines from the file.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_filename = "INPUT_NAME.txt"   # Replace with your input file name
    output_filename = "OUTPUT_NAME.txt"  # Replace with your output file name
    remove_duplicates(input_filename, output_filename)
