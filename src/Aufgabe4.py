import numpy
import pandas as pd

print(pd.__version__)

# url = 'https://github.com/edlich/eternalrepo/blob/master/DS-WAHLFACH/countries.csv'

url = 'https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/countries.csv'

# Load the data into a Pandas DataFrame
countrydata = pd.read_csv(url)

# Display the data of the second row
print("\n\n", countrydata.loc[1])

# Display the column "Currency
print("\n\nHier sind die Daten der Spalte Currency:\n", countrydata.Currency)
# print("\n\nHier ist die Spalte Currency:\n", countrydata.Currency.to_string(index=False))

# Display the first 3 rows
print("\n\n", countrydata.head(2))

# Showing the last 4 rows
last4rows = countrydata.tail(4)
print("\n\nHere are the last four rows:\n", last4rows)

# Showing all the rows of countries who have the EURO
print("\n\nHier sind alle Zeilen die Euro als Währung verwenden:\n", countrydata.loc[countrydata['Currency'] == "EUR"])

# Showing only name and Currency in a new data frame
print("\n\nHier werden nur Namen und Währungen angezeigt:")
print(countrydata[['Name', 'Currency']])

# Showing only the rows/countries that have more than 2000 BIP (it is in Milliarden USD Bruttoinlandsprodukt)
print("\n\nHier werden nur Länder anzegeit, die mehr als 2000 Milliarden USD BIP haben:")
print(countrydata.loc[countrydata['BIP'].values > 2000])

# Selecting all countries with inhabitants between 50 and 150 Mio
print("\n\nHier werden nur Länder angezeigt, die zwischen 50 und 150 Millionen Einwohner haben:")
print(countrydata.loc[(countrydata['People'].values > 50000000) & (countrydata['People'].values < 150000000)])
