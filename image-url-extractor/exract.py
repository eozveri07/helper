import re

def extract_unique_image_urls(text):
    pattern = r'https?://[^/]+/wp-content/uploads/\d{4}/\d{2}/[^"\s]+\.(?:png|jpe?g|webp)(?:\.\w+)?'
    
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    unique_urls = set()
    
    for url in matches:
        base_url = re.sub(r'-\d+x\d+(\.(png|jpe?g|webp))', r'\1', url)
        unique_urls.add(base_url)
    
    return list(unique_urls)

def save_urls_to_file(urls, filename='url-list.txt'):
    with open(filename, 'w') as f:
        for url in sorted(urls):
            f.write(url + '\n')

def main():
    input_file = 'input.txt'
    output_file = 'url-list.txt'

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        unique_image_urls = extract_unique_image_urls(text)
        
        save_urls_to_file(unique_image_urls, output_file)
        
        print(f"{len(unique_image_urls)} unique URLs found and saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found. Please ensure the file exists in the current directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()