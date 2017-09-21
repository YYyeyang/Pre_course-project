import csv
import string



with open('Registered_unemployment_processed.csv', mode='r') as infile:
    reader = csv.reader(infile)
    unemployment_years = {}
    for year in [2013,2014,2015,2016,2017]:
        year_dic = {}
        for row in reader:
            if str(year) in row[0].split(";"):
                key = (row[0].split(";"))[1]
                value = (row[0].split(";"))[2]
                # strreplace= String replace the non-digit into empty
                value = value.replace("/", "")
                value = value.replace("'", "")
                value = value.replace(" ", "")
                # add the second element of the list as a key and the third as value to the list
                year_dic[key] = value

    unemployment_years[year] = year_dic

# if row(0) = year

# for year in years

# if year is 2016, write to the 2016 dic
# if the year dic is in range 2013-2016, then write to unemployment dic
