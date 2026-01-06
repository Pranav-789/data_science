# -------------------------------
# Multithreading example for I/O-bound tasks (Web Scraping)
# -------------------------------

import threading              # Provides low-level thread creation
import requests               # Used for making HTTP requests (blocking I/O)
from bs4 import BeautifulSoup # Used to parse HTML content


# List of URLs to be fetched concurrently
urls = [
    "https://python.langchain.com/v0.2/docs/introduction/",
    "https://python.langchain.com/v0.2/docs/concepts/",
    "https://python.langchain.com/v0.2/docs/tutorials/"
]


def fetch_contents(url):
    """
    Fetches the HTML content of a web page, parses it using BeautifulSoup,
    and prints the parsed HTML along with the character count.

    This function is I/O-bound because it waits for network responses,
    making it ideal for multithreading.
    """

    # Send HTTP GET request (blocking I/O operation)
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print parsed HTML (for inspection / debugging)
    print(soup, end="\n\n")

    # Print the length of extracted text content
    print(f"Fetched {len(soup.text)} characters from {url}")


# List to keep track of thread objects
threads = []

# Create and start a thread for each URL
for url in urls:
    # Create a new thread that executes fetch_contents(url)
    thread = threading.Thread(target=fetch_contents, args=(url,))

    # Store the thread reference
    threads.append(thread)

    # Start the thread (execution begins here)
    thread.start()


# Wait for all threads to complete before continuing
for thread in threads:
    thread.join()


# This line executes only after all threads have finished
print("All web pages fetched")
