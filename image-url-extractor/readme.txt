WordPress Image URL Extractor
This Python script extracts unique image URLs from WordPress-based websites. It's designed to work with any WordPress site, making it a versatile tool for web scraping and content analysis.
Features

Extracts image URLs from WordPress sites
Works with any domain (not limited to a specific website)
Removes duplicate URLs
Cleans URLs by removing size information (e.g., -300x200)
Supports .png, .jpg, .jpeg, and .webp image formats

Requirements

Python 3.x

Installation

Clone this repository or download the exract.py file.
Ensure you have Python 3.x installed on your system.

Usage

Prepare your input:

Create a file named input.txt in the same directory as the script.
Paste the HTML content or text containing the WordPress image URLs into this file.


Run the script:
python exract.py

View the results:

The script will create (or overwrite) a file named url-list.txt.
This file will contain the extracted unique image URLs, one per line.
The console will display the number of unique URLs found.



Customization

To change the input or output file names, modify the input_file and output_file variables in the main() function of the script.

How It Works

The script reads the content from input.txt.
It uses a regular expression to find all WordPress-style image URLs.
Each URL is processed to remove size information.
Duplicate URLs are eliminated.
The unique URLs are sorted and saved to url-list.txt.

Troubleshooting

If you see "Error: 'input.txt' not found", ensure that you've created the input file in the same directory as the script.
For any other errors, check that the input file contains valid HTML or text content with WordPress image URLs.

Contributing
Feel free to fork this repository and submit pull requests with any enhancements.
License
This project is open source and available under the MIT License.