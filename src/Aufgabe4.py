import numpy
import pandas as pd

print(pd.__version__)

#url = 'https://github.com/edlich/eternalrepo/blob/master/DS-WAHLFACH/countries.csv'

url = 'https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/countries.csv'

#Load the data into a Pandas DataFrame
countrydata = pd.read_csv(url, index_col=0)

print(countrydata)

print(pd.options.display.max_rows)

print(countrydata.head(2))

print(countrydata.info())

#print(countrydata.loc[0])
#print(countrydata[:3])
