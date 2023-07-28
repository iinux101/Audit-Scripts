import os
import re
import multiprocessing

def extract_ip_addresses(line):
    # Regular expression to extract IP addresses from a line
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.findall(ip_pattern, line)

def search_file(ip_addresses, file_path, output_file):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, 1):
                for ip in ip_addresses:
                    if ip in line:
                        result = f"Found IP '{ip}' in '{file_path}' (Line {line_number}): {line.strip()}\n"
                        with open(output_file, 'a') as output:
                            output.write(result)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def main():
    # Get the path to the file containing IP addresses from the user
    ip_file_path = input("Enter the path to the file containing IP addresses: ")

    # Read IP addresses from the file
    with open(ip_file_path, 'r') as ip_file:
        ip_addresses = [ip.strip() for ip in ip_file]

    # Get the path to the directory containing the files from the user
    directory_path = input("Enter the path to the directory containing the files: ")

    # Get the path to the output file
    output_file = input("Enter the path to the output file: ")

    # Get the number of available CPU cores minus 2
    num_cores = max(1, multiprocessing.cpu_count() - 2)

    # Create a pool of processes to perform the search
    pool = multiprocessing.Pool(processes=num_cores)

    # Get a list of file paths in the specified directory
    file_paths = [os.path.join(directory_path, filename) for filename in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, filename))]

    # Start searching each IP address from the file in each file from the directory using multiple processes
    for file_path in file_paths:
        pool.apply_async(search_file, args=(ip_addresses, file_path, output_file))

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
