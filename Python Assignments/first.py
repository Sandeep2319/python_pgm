from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        # Inner NavigableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()
    
    except AttributeError:
        title_string = ""
    
    return title_string
    

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("span", attrs={"class":'priceToPay'}).find("span", attrs={"class":'a-price-whole'}).text.strip()
    except AttributeError as e:
        price = ""
 
    return price
    print(price,"hello")


# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

# Function to extract Number of User Reviews
def get_reviews(soup):
    try:
        reviews = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        reviews = ""	

    return reviews

# Function to extract Description
def get_description(soup):
    try:
        description = soup.find("div", attrs={"id": 'productDescription_feature_div'}).find("div", attrs={"class":'a-section a-spacing-small'}).text.strip()

    except AttributeError:
        description = ""

    return description

# Function to extract Manufacturer
def get_manufacturer(soup):
    try:
        manufacturer = soup.find("div", attrs={"id": 'detailBullets_feature_div'}).find_all("li")[2].find_all("span")[2].text.strip()

    except AttributeError:
        manufacturer = ""
    
    return manufacturer

# Function to extract ASIN number

def get_asin_number(soup):

    try:
        asin_number = soup.find("div", attrs={"id": 'detailBullets_feature_div'}).find_all("li")[3].find_all("span")[2].text.strip()

    except AttributeError:
         asin_number = ""

    return  asin_number
    

if __name__ == '__main__':

    # add your user agent 
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    URL = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
            links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "reviews":[], "description":[], "manufacturer": [], "asin_number": []}

    # Loop for extracting product details from each link 
    for link in links_list:
        try:
            new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)
        except: 
            print("skipping")
            continue
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_reviews(new_soup))
        d['description'].append(get_description(new_soup))
        d['manufacturer'].append(get_manufacturer(new_soup))
        d['asin_number'].append(get_asin_number(new_soup))

    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)