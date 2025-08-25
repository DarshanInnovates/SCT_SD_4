import requests
from bs4 import BeautifulSoup
import csv

GBP_TO_INR = 105  

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price (₹ INR)", "Rating"])

    products = soup.find_all("article", class_="product_pod")

    for product in products:
        name = product.h3.a["title"]

        # Get price text and clean it
        price_text = product.find("p", class_="price_color").text.strip()
        price_text = price_text.replace("£", "").replace("Â", "").replace("\xa0", "").strip()
        price_gbp = float(price_text)

        # Convert GBP → INR
        price_inr = round(price_gbp * GBP_TO_INR, 2)

        rating = product.p["class"][1]

        writer.writerow([name, f"₹{price_inr}", rating])

        # Print on screen too
        print(f"{name} | ₹{price_inr} | {rating}")

print("✅ Done! Data saved in products.csv (Prices in INR)")
