'''
In this project, you are going to use the web scraping technique to extract information from a website. You need to collect information such as the page title, a specific class, and an image from a web page.

Project Objective:

You need to extract the following information from a website of your choice (for example, the website of an online library or bookstore):

Web page title
Information inside a specific class (for example, the title of a book or product)
Image link related to the book or product
To do this, you will use the requests and BeautifulSoup libraries.
Project Steps:
Introduction: First, you need to install the required libraries:

pip install requests beautifulsoup4
Connect to the website: Connect to the desired website using the requests library.
Reading and Parsing HTML: Use the BeautifulSoup library to parse the HTML and extract the required information.
Extracting Information:

Page Title: Extract the main title of the web page.
Information from a specific class: For example, extracting book titles or product names from a specific class in HTML.
Images: Extract image links for each product or book.
Print results: Finally, print the extracted results to the console.

Inputs:

A URL from the website to extract information from.
An HTML class for which you want to extract information (for example, for books or products).
Outputs:

The title of the web page.
A list of titles in a specific class.
A list of image links on the page.

Note that when submitting the response, include a screenshot of the URL you are testing along with the code.
'''

pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def scrape_website(url, target_class):
    # Connect to website
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to connect. Status code: {response.status_code}")
        return
    
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract page title
    page_title = soup.title.string if soup.title else 'No Title Found'
    
    # Extract texts from elements with the target class
    elements = soup.find_all(class_=target_class)
    texts = [el.get_text(strip=True) for el in elements]
    
    # Extract image URLs (all <img> tags)
    images = soup.find_all('img')
    image_links = []
    for img in images:
        src = img.get('src')
        if src:
            # Fix relative URLs if any
            if src.startswith('http'):
                image_links.append(src)
            else:
                from urllib.parse import urljoin
                full_url = urljoin(url, src)
                image_links.append(full_url)
    
    # Print results
    print(f"Page Title: {page_title}\n")
    print(f"Texts in class '{target_class}':")
    for text in texts:
        print("-", text)
    print("\nImage Links:")
    for link in image_links:
        print("-", link)

# Example usage
url = "https://books.toscrape.com/"
target_class = "product_pod"  # This class wraps each book on the page

scrape_website(url, target_class)
