import numpy
import pandas as pd

print(pd.__version__)

#url = 'https://github.com/edlich/eternalrepo/blob/master/DS-WAHLFACH/countries.csv'

url = 'https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/countries.csv'

#Load the data into a Pandas DataFrame
countrydata = pd.read_csv(url)

#Display the second row
print(countrydata.loc[1])



print("Huhu")


print(pd.options.display.max_rows)

print("\n\n" , countrydata.head(2))

#Showing the last 4 rows


#print(countrydata.loc[0])
#print(countrydata[:3])
