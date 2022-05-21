import numpy
import pandas as pd

print(pd.__version__)

#url = 'https://github.com/edlich/eternalrepo/blob/master/DS-WAHLFACH/countries.csv'

url = 'https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/countries.csv'

#Load the data into a Pandas DataFrame
countrydata = pd.read_csv(url)

#Display the data of the second row
print("\n\n", countrydata.loc[1])

#Display the column "Currency
print("\n\nHier sind die Daten der Spalte Currency:\n", countrydata.Currency)
#print("\n\nHier ist die Spalte Currency:\n", countrydata.Currency.to_string(index=False))

#Display the first 3 rows
print("\n\n" , countrydata.head(2))

#Showing the last 4 rows
last4rows = countrydata.tail(4)
print("\n\nHere are the last four rows:\n", last4rows)

#print(countrydata.loc[0])
#print(countrydata[:3])
