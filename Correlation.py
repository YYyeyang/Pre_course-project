import function_data_per_yr
import numpy
import matplotlib.pyplot as plt

# built full-dictionary for age and unemployment
age_dic= function_data_per_yr.build('Avg_age_processed.csv')
unemployment_dic= function_data_per_yr.build('Registered_unemployment_processed.csv')

# convert them into a float list per year per type
age2013=function_data_per_yr.convert(age_dic,2013)
age2014=function_data_per_yr.convert(age_dic,2014)
age2015=function_data_per_yr.convert(age_dic,2015)
age2016=function_data_per_yr.convert(age_dic,2016)

unemployment2013=function_data_per_yr.convert(unemployment_dic,2013)
unemployment2014=function_data_per_yr.convert(unemployment_dic,2014)
unemployment2015=function_data_per_yr.convert(unemployment_dic,2015)
unemployment2016=function_data_per_yr.convert(unemployment_dic,2016)

# add all year together
all_age=age2013+age2014+age2015+age2016
all_unemployment=unemployment2013+unemployment2014+unemployment2015+unemployment2016

# calculate the correlation coefficient
cor = numpy.corrcoef(all_age,all_unemployment)[0,1]
print(cor)

# plot my correlations
plt.scatter(all_age,all_unemployment)
plt.show()

