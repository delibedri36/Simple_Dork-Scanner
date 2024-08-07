import requests
from bs4 import BeautifulSoup
import urllib.parse

def search_dorks(dorks):
    base_url = 'https://www.google.com/search'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    urls = []

    for dork in dorks:
        params = {
            'q': dork,
            'num': '10'  # Arama sonuçlarının sayısını belirler
        }
        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            for result in soup.find_all('div', class_='g'):
                link = result.find('a')['href']
                if link:
                    full_link = urllib.parse.urljoin(base_url, link)
                    urls.append(full_link)
        except requests.RequestException as e:
            print(f"Error: {e}")

    return urls

def main():
    print("Enter your dorks one by one. Type 'done' when you are finished.")
    dorks = []
    while True:
        dork = input("Enter dork: ")
        if dork.lower() == 'done':
            break
        dorks.append(dork)

    if not dorks:
        print("No dorks provided.")
        return

    print("Searching for dorks...")
    urls = search_dorks(dorks)

    if urls:
        print("Found URLs:")
        for url in urls:
            print(url)
    else:
        print("No URLs found.")

if __name__ == "__main__":
    main()
