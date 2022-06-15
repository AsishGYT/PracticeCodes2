from bs4 import BeautifulSoup
import pandas as pd

import requests

url = "https://www.amazon.com/MSI-Thin-Bezel-Quad-Core-i5-10300H-Keyboard/dp/B098JFL5DK"
# https://www.amazon.com/MSI-Thin-Bezel-Quad-Core-i5-10300H-Keyboard/dp/B098JFL5DK
# https://www.amazon.in/HP-Processor-16-1-inch-Graphics-16-e0301ax/dp/B09RX35BKN
# https://www.amazon.in/Dell-Alienware-Display-Keyboard-Windows/dp/B09HS84XXX


# prod_title = s.select("#productTitle")[0].get_text().strip()
#print("NAME : ", "\n",  prod_title,'\n')


#prod_price_tag = s.find("span", class_="a-price-whole").get_text().strip()
#print("PRICE :", '\n', prod_price_tag, '\n' )

# sets = pd.DataFrame(data4, columns=['Name', 'Value'])
# print(sets)


def get_product_details(product_amazon_url):
    """
    takes url, 
    return : dictionary of product details
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    resp = requests.get(product_amazon_url, headers=headers)
    s = BeautifulSoup(resp.content, features="lxml")

    table_data = s.find('table', class_="a-keyvalue prodDetTable")
    rows = table_data.find_all('tr')

    product_details = {}
    for i in rows:
        td = i.find('td')
        th = i.find('th')
        td_text = td.text.encode("ascii", "ignore")
        td_text = td_text.decode().strip()
        th_text = th.text.strip()
        product_details[th_text] = td_text

    return product_details


if __name__ == "__main__":
    products = []
    product_search_results_df = pd.read_csv(r"laptop.csv")
    # iterate row in
    for i, product_row in product_search_results_df.iterrows():
        product_url = product_row["product url"]
        product_details_dict = get_product_details(product_url)
        print("new detialas", product_details_dict, "\n\n")
        # update row, with abo dict
        product_row = dict(product_row)
        product_details_dict.update(product_row)
        products.append(product_details_dict)
        print(product_url, "done..")

    # convert it to df , and store

    products_df_wide = pd.DataFrame(products)
    products_df_wide.to_csv("test.csv")
