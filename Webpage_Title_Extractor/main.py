
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_webpage_title(url):
    url = url.strip()

    if not re.match(r"^https?://", url, re.IGNORECASE):
        raise ValueError("Please enter a valid URL starting with http:// or https://")

    parsed_url = urlparse(url)

    if not parsed_url.netloc:
        raise ValueError("Invalid webpage URL.")

    response = requests.get(
        url,
        timeout=15,
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=True
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("title")

    if title_tag:
        return title_tag.get_text(strip=True)

    return None