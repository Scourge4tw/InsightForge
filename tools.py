from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()
from rich import print

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool  # First tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns Titles, URLs and Snippets."""
    results = tavily.search(query=query, max_results=5)

    out = []
    for r in results['results']:
        out.append(
            f"Title:{r['title']}\n URL:{r['url']}\n Snippet:{r['content'][:300]}\n"
        )
    return "\n----\n".join(out)


@tool  # Second tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove all non-content elements (scripts, boilerplate, nav/menu/ads)
        junk_tags = [
            "script", "style", "nav", "footer", "header", "aside",
            "form", "iframe", "noscript", "svg", "button", "input"
        ]
        for tag in soup(junk_tags):
            tag.decompose()

        # Remove elements whose class/id strongly suggests nav/menu/ad/sidebar content
        junk_keywords = [
            "nav", "menu", "sidebar", "footer", "header", "advert", "ads",
            "banner", "cookie", "subscribe", "newsletter", "social",
            "share", "related", "breadcrumb", "promo", "widget", "comment"
        ]
        for tag in soup.find_all(True):
            attr_string = " ".join(
                tag.get("class", []) + [tag.get("id", "")]
            ).lower()
            if any(keyword in attr_string for keyword in junk_keywords):
                tag.decompose()

        # Try to isolate the main article body first
        main_content = (
            soup.find("article")
            or soup.find(attrs={"role": "main"})
            or soup.find(class_=lambda c: c and "content" in c.lower())
            or soup.find(id=lambda i: i and "content" in i.lower())
        )

        target = main_content if main_content else soup

        # Extract text only from paragraph-like elements to avoid stray link clusters
        paragraphs = target.find_all(["p", "h1", "h2", "h3", "li"])
        if paragraphs:
            text = " ".join(p.get_text(separator=" ", strip=True) for p in paragraphs)
        else:
            text = target.get_text(separator=" ", strip=True)

        text = " ".join(text.split())  # collapse whitespace

        if len(text) < 100:
            return "No substantial article content found at this URL."

        return text[:3000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"