import http

def fetch_website(url: str) -> str:
    response = http.get(url)
    return response.text

def main():
    content = fetch_website("http://example.com")
    print(content)

if __name__ == "__main__":
    main()
