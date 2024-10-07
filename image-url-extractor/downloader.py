import os
import re
import requests

def read_url_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def clean_file_name(url):
    file_name = url.split("/")[-1]  
    clean_name = re.sub(r'[-_]\d+x\d+|-\d+', '', file_name)  
    return clean_name

def download_images(url_list):
    os.makedirs('downloaded_images', exist_ok=True)

    for url in url_list:
        try:
            response = requests.get(url)
            clean_name = clean_file_name(url)  
            file_name = os.path.join('downloaded_images', clean_name)
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f'{file_name} downloaded successfully.')
        except Exception as e:
            print(f'Failed to download {url}. Error: {e}')

if __name__ == "__main__":
    url_list = read_url_list('url-list.txt')
    download_images(url_list)