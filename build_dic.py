def build (csvfilename, dictionary):

    import csv
    import string

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