import requests
from bs4 import BeautifulSoup
import re

def extract_details_from_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Social Links extraction
    social_domains = ['facebook.com', 'twitter.com', 'linkedin.com', 'instagram.com']
    social_links = []

    for link in soup.find_all('a', href=True):
        if any(domain in link['href'] for domain in social_domains):
            social_links.append(link['href'])
    
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}"
    emails = re.findall(email_pattern, response.text)

    contact_pattern = r"\+?\d{1,3}?[- .]?\(?(?:\d{2,3})?\)?[- .]?\d\d\d[- .]?\d\d\d\d"
    contacts = re.findall(contact_pattern, response.text)

    return social_links, emails, contacts

if __name__ == "__main__":
    url = input("Enter the website URL: ")
    social_links, emails, contacts = extract_details_from_website(url)

    print("\nSocial links -")
    for link in social_links:
        print(link)
    
    print("\nEmails:")
    for email in emails:
        print(email)
    
    print("\nContacts:")
    for contact in contacts:
        print(contact)
