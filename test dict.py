import csv

dictionary={}

with open('Registered_unemployment_processed.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        if row[0].split(";")=="2016":
            key=(row[0].split(";"))[1]
            value=(row[0].split(";"))[2]
            #strplace= String replace the non-digit into empty
            dictionary[key]=value



        print(newlist)

        #Split with ;
        #check if its starts with 2016
        #add the second element of the list as a key and the third as value to the list