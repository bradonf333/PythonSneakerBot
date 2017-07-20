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
    #Base Size for the Shoe is 6.5
    #Minus 6.5 from the shoe size to give a base, 6.5 would equal 0
    shoe_size = float(size) - 6.5
    #Number that we need to add to base size to equal the desired shoe size
    shoe_size = shoe_size * 20
    #Gives us the desired shoe size code
    raw_size = shoe_size + base_size
    #Convert RawSize to int
    shoe_size_code = int(raw_size)
    #Build the URL
    url = 'http://www.adidas.com/us/nmd_r1-shoes/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(shoe_size_code)
    return url
def check_stock(url):
    """Doc-string"""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    raw_html = requests.get(url, headers=headers)
    page = bs4.BeautifulSoup(raw_html.text)
    list_of_raw_sizes = page.select('.size-dropdown-block')
    sizes = str(list_of_raw_sizes[0].getText()).replace('\t', '')
    sizes = sizes.replace('\n\n', ' ')
    sizes = sizes.replace(' Select size \n', '')
    sizes = sizes.split()
