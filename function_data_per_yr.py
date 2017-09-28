import csv

def build (csvfilename):

    dictionary = {}
    years = [2013, 2014, 2015, 2016]
    for year in years:
        year_dic = {}
        with open(csvfilename, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                if str(year) in str(row[0].split(";")):
                    key = (row[0].split(";"))[1]
                    value = (row[0].split(";"))[2]
                # String replace the non-digit into empty
                    value = value.replace("/", "")
                    value = value.replace("'", "")
                    value = value.replace(" ", "")
                # add the second element of the list as a key and the third as value to the list
                    year_dic[key] = value

            dictionary[year] = year_dic

    return dictionary


def convert (dict, year):

    lis = []
    for year_dic in dict:
        if year_dic == year:
            for district in dict[year]:
                lis.append(dict[year][district])

    num_list = [float(i) for i in lis]
    return num_list