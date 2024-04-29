import os
import requests

# Get the current working directory
current_directory = os.getcwd()

# Construct the file path for saving the .jl file in the current directory
jl_file_path = os.path.join(current_directory, "book_list_data.jl")

book_list_url = "https://www.goodreads.com/review/list/11083989-s?shelf=%23ALL%23"

# Add headers to mimic a legitimate browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(book_list_url, headers=headers)
if response.status_code == 200:
    # Open the .jl file in write mode to save the JSON Lines data
    with open(jl_file_path, "w") as f:
        # Iterate over each line of the JSON response and write it to the file
        for line in response.iter_lines():
            if line:
                # Write each line to the file followed by a newline character
                f.write(line.decode('utf-8') + '\n')
    print("JSON Lines data saved successfully at:", jl_file_path)
else:
    print("Failed to fetch JSON data. Status code:", response.status_code)

