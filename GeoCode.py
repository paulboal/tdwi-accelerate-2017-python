import requests
import json

class GeoCode:
    def __init__(self, key='AIzaSyCsGHgVeGETA9Q_gtrwJmqh1G_V1HNv3qE'):
        self._key = key
        self._base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def lookup(self, address):
        url = self._get_url(address)
        r = requests.get(url)

        if r.status_code != 200:
            self._results = null
            return self

        self._results = r.json()
        return self

    def get_json(self):
        return self._results

    def get_zip(self):
        try:
            if self._results:
                for component in self._results['results'][0]['address_components']:
                    if 'postal_code' in component['types']:
                        return component['long_name']
            else:
                return ''
        except:
            return ''

    def _get_url(self, address):
        return self._base_url + '?key=' + self._key + '&address=' + address.replace(' ', '+')
