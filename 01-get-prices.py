from GetPrices import ClearHealthCosts
chc = ClearHealthCosts()
chc._get_base_url('sleep','10001',100)
prices = chc.get_sleep_prices('10001',100)
print(prices)
