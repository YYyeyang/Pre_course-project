import build_dic
import numpy

age={}
unemployment={}

age_dic=build_dic.build('Avg_age_processed.csv',age)
unemployment_dic=build_dic.build('Registered_unemployment_processed.csv',unemployment)

print(age_dic)
print(unemployment_dic)

result=numpy.corrcoef(age_dic[2013],unemployment_dic[2013])[0, 1]
print(result)


#loop over the year
#loop over the distrct
#append to my two list


