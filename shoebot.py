"""This is going to be a shoe bot"""
# Import dependencies
import random
import webbrowser
import bs4
import requests

# Base URL = http://www.adidas.com/us/nmd_r1-shoes/BZ0220.html?forceSelSize=BZ0220_640

def url_gen(model, size):
    "function_docstring"
    base_size = 580
    # Base Size for the Shoe is 6.5
    # Minus 6.5 from the shoe size to give a base, 6.5 would equal 0
    shoe_size = float(size) - 6.5
    # Number that we need to add to base size to equal the desired shoe size
    shoe_size = shoe_size * 20
    # Gives us the desired shoe size code
    raw_size = shoe_size + base_size
    # Convert RawSize to int
    shoe_size_code = int(raw_size)
    # Build the URL
    url = 'http://www.adidas.com/us/nmd_r1-shoes/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(shoe_size_code)
    return url
def check_stock(url, model):
    """Doc-string"""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # Get the raw html from the url
    raw_html = requests.get(url, headers=headers)
    # Page stores the readable version of the raw html
    page = bs4.BeautifulSoup(raw_html.text, "html.parser")
    # Gets the sizes from the size dropdown (not usable yet)
    list_of_raw_sizes = page.select('.size-dropdown-block')
    # Remove uneeded info from the sizes and then put in a list
    sizes = str(list_of_raw_sizes[0].getText()).replace('\t', '')
    sizes = sizes.replace('\n\n', ' ')
    sizes = sizes.replace(' Select size \n', '')
    sizes = sizes.split()
    # Prints a message telling the user what sizes are available
    for size in sizes:
        print(str(model) + ' Size: '  + str(size)  + ' Available')
def main(model, size):
    """Doc-string"""
    # Set the url to the result of the url_gen function
    url = url_gen(model, size)
    # Calls the check_stock function passing in the url created 
    check_stock(url, model)
