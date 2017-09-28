import csv

def build (csvfilename):

    dictionary = {}
    districts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for district in districts:
        dis_dic = {}
        with open(csvfilename, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                if str(district) in str(row[0].split(";")):
                    key = (row[0].split(";"))[0]
                    value = (row[0].split(";"))[2]
                # String replace the non-digit into empty
                    value = value.replace("/", "")
                    value = value.replace("'", "")
                    value = value.replace(" ", "")
                # add the second element of the list as a key and the third as value to the list
                    dis_dic[key] = value

            dictionary[district] = dis_dic

    return dictionary

def convert (dict, dis):

    lis = []
    for dis_dic in dict:
        if dis_dic == dis:
            for year in dict[dis]:
                lis.append(dict[dis][year])

    num_list = [float(i) for i in lis]
    return num_list