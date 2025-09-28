import requests
from bs4 import BeautifulSoup


def fetch_headlines():
    """
    Fetches cryptocurrency news headlines from multiple sources.
    Returns a list of headline strings.
    """
    urls = [
        "https://cointelegraph.com",
        "https://cryptonews.com",
            "https://decrypt.co",
    "https://bitcoinmagazine.com",
    "https://www.coindesk.com",

    ]
    headlines = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            continue
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract h2 headlines as an example; adjust selectors based on site structure
        for h2 in soup.find_all("h2"):
            text = h2.get_text(strip=True)
            if text and text not in headlines:
                headlines.append(text)
    return headlines


def main():
    """Main function to fetch and display headlines."""
    headlines = fetch_headlines()
    print("Latest cryptocurrency news headlines:\n")
    for i, headline in enumerate(headlines[:10], start=1):
        print(f"{i}. {headline}")


if __name__ == "__main__":
    main()
