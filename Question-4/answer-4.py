import requests
from bs4 import BeautifulSoup
import re

technologies = {
    "jQuery": "jquery[.-]?\d+\.\d+",
    "React.js": "['\"]react(-dom)?\.min\.js['\"]",
    "WooCommerce": "woocommerce\/assets\/",
    "Bootstrap": "bootstrap(\.min)?\.css",
    "Shopify": "cdn\.shopify\.com",
    "Next.js": "next\.js\/",
    "Materialize CSS": "materialize(\.min)?\.css",
    "PHP": "\.php[?/]?",
    "Python": "['\"]Python\/\d+\.\d+",
    "Google Maps": "maps\.googleapis\.com"
}

sample_websites = {
    "jQuery": "https://www.wikipedia.org/",
    "React.js": "https://www.airbnb.com/",
    "WooCommerce": "https://shop.lululemon.com/",
    "Bootstrap": "https://getbootstrap.com/",
    "Shopify": "https://www.gymshark.com/",
    "Next.js": "https://vercel.com/",
    "Materialize CSS": "https://materializecss.com/",
    "PHP": "https://wordpress.com/",
    "Python": "https://www.python.org/",
    "Google Maps": "https://www.uber.com/"
}

def detect_technology(url, pattern):
    try:
        response = requests.get(url)
        if re.search(pattern, response.text):
            return True
        else:
            return False
    except Exception as e:
        return False

for tech, pattern in technologies.items():
    url = sample_websites[tech]
    is_detected = detect_technology(url, pattern)
    print(f"Technology Name: {tech}")
    print(f"Sample Website: {url}")
    if is_detected:
        print(f"{tech} detected!")
    else:
        print(f"{tech} not detected!")
    print("-----------------------------")
