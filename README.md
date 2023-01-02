# nepal-stock-price
This is a python package to download the stock price data of the companies listed in Nepal Stock Exchage(NEPSE).

## Installation

```bash
pip install nepal-stock-price
```

##  Usage
```python
from nepse_data import NepseData

#scripts name
price_history = NepseData("nica")

data_df = price_history.price_history()

#filepath to save price history in csv format
file_name = "nica.csv"
data_df.to_csv("data/" + file_name, encoding='utf-8', index=False)
```

Hurray!!! Now you will be able to download the stock price data of any companies which are listed on NEPSE...

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

You can get some of the data from [my kaggle profile](https://www.kaggle.com/datasets/keskhanal2413/stock-price-dataset-of-top-companies-of-nepse/settings)

## Contact
If you have any queries then drop a [message here](https://www.linkedin.com/in/keskhanal/)
