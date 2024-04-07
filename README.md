BitcoinPriceLight is a Python script that changes the colors of your Govee lights based on if Bitcoin value is growing or falling
Green if it's growing, Red if falling.
Interval cannot be too small because then it won't catch the changes and it may cause to go over the rate limit of 10 per minute for govee api
libraries used:
https://github.com/LaggAt/python-govee-api
https://pypi.org/project/bitcoin-value/
