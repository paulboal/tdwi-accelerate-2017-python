# PURPOSE
# This module contains functions for retrieving and compiling a list of prices for sleep related procedures from Clear Health Costs .com
#
# get_sleep_prices() - returns a list of sleep study pricing information from the website, given a particular zip code and search range.
#   get_prices() - helper that works with any procedures

from bs4 import BeautifulSoup
import requests
import logging

class ClearHealthCosts:

    #---------------------------------------------------------------------------
    # PUBLIC METHODS
    #---------------------------------------------------------------------------
    def prices(self):
        return self._prices

    def clear_prices(self):
        self._prices = []
        return self

    def get_prices(self, condition, zip, radius):
        url = self._get_base_url(condition, zip, radius)
        result = requests.get(url)

        if result.status_code == 200:
            prices = self._parse_pricelist(result.content)
            for i in range(0,len(prices)):
                prices[i] += [condition, zip, radius]

            self._prices += prices

        return self

    def get_sleep_prices(self, zip, radius=100):
        return self.get_prices('sleep', zip, radius)

    #---------------------------------------------------------------------------
    # PRIVATE METHODS
    #---------------------------------------------------------------------------

    _prices = []
    _base_url = 'https://clearhealthcosts.com/search/?'

    def __init__(self):
        self.clear_prices()

    def _get_base_url(self, query, zip_code, radius):
        return self._base_url+'query='+str(query)+'&zip_code='+str(zip_code)+'&radius='+str(radius)+'&submit='

    def _parse_price(self, item):
        charged = item.find('div','price-badge price-charged')
        price = float(charged.findAll('p')[1].getText().strip().strip('$').replace(',',''))
        name = item.find('span','provider').getText().strip()
        addr = item.find('span','address').getText().strip()

        return [price, name, addr]


    def _parse_pricelist(self, page):
        prices = []
        soup = BeautifulSoup(page, 'html.parser')
        items = soup.findAll('div', 'ui grid segment')

        for item in items:
            price = self._parse_price(item)
            prices.append(price)

        return prices
