import build_dic
import numpy
import matplotlib.pyplot as plt

age={}
unemployment={}

age_dic= build_dic.build('Avg_age_processed.csv', age)
unemployment_dic= build_dic.build('Registered_unemployment_processed.csv', unemployment)

print(age_dic)
print(unemployment_dic)



# loop over the year
# loop over the district
# append to my two list

# 2013age[39,45,23,67...] vs. 2013umemp[2314,4578,2346,....]
age2013=[]
for year_dic in age_dic:
    if year_dic == 2013:
        for district in age_dic[2013]:
            age2013.append(age_dic[2013][district])


age2013_num = [float(i) for i in age2013]

unemployment2013=[]
for year_dic in unemployment_dic:
    if year_dic == 2013:
        for district in unemployment_dic[2013]:
            unemployment2013.append(unemployment_dic[2013][district])

unemployment2013_num = [float(i) for i in unemployment2013]

sig2013 = numpy.corrcoef(age2013_num,unemployment2013_num)[0,1]
print(sig2013)

plt.scatter(age2013_num,unemployment2013_num)
plt.show()
