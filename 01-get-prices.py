from GetPrices import ClearHealthCosts

chc = ClearHealthCosts()
chc.get_sleep_prices('10001',100)
chc.get_sleep_prices('94016',100)
for price in chc.prices():
    print("{:7.2f} {:60.60} {:60.60}".format(price[0],price[1],price[2]))
