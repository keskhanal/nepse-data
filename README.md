# nepal-stock-price
This is a python package to download the stock price data of the companies listed in Nepal Stock Exchage(NEPSE).

## Installation

```bash
pip install nepal-stock-price
```

##  Usage
```python
from nepse_data.automation import Automate

#scripts name
automation = Automate("nica")

final_df = automation.price_history()

#filepath to save price data in csv format
file_name = "nica.csv"
final_df.to_csv("data/" + file_name, encoding='utf-8', index=False)
```

Hurray!!! Now you will be able to get the stock price data of any companies which are listed on NEPSE...

## TODO
* add visualization
* add features like to get todays_price, broker_list, news, dividend_history etc. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact
If you have any queries then drop a [message here](https://www.linkedin.com/in/keskhanal/) or [visit](https://www.khanalkeshav.com.np/)
