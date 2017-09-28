import function_data_per_dis
import matplotlib.pyplot as plt

# built full-dictionary for age and unemployment
age_dic= function_data_per_dis.build('Avg_age_processed.csv')
unemployment_dic= function_data_per_dis.build('Registered_unemployment_processed.csv')

# convert them into a float list per year per type
age1=function_data_per_dis.convert(age_dic,1)
age2=function_data_per_dis.convert(age_dic,2)
age3=function_data_per_dis.convert(age_dic,3)
age4=function_data_per_dis.convert(age_dic,4)
age5=function_data_per_dis.convert(age_dic,5)
age6=function_data_per_dis.convert(age_dic,6)
age7=function_data_per_dis.convert(age_dic,7)
age8=function_data_per_dis.convert(age_dic,8)
age9=function_data_per_dis.convert(age_dic,9)
age10=function_data_per_dis.convert(age_dic,10)

unemployment1=function_data_per_dis.convert(unemployment_dic,1)
unemployment2=function_data_per_dis.convert(unemployment_dic,2)
unemployment3=function_data_per_dis.convert(unemployment_dic,3)
unemployment4=function_data_per_dis.convert(unemployment_dic,4)
unemployment5=function_data_per_dis.convert(unemployment_dic,5)
unemployment6=function_data_per_dis.convert(unemployment_dic,6)
unemployment7=function_data_per_dis.convert(unemployment_dic,7)
unemployment8=function_data_per_dis.convert(unemployment_dic,8)
unemployment9=function_data_per_dis.convert(unemployment_dic,9)
unemployment10=function_data_per_dis.convert(unemployment_dic,10)

plt.subplot(2,5,1)
plt.scatter(age1,unemployment1)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,2)
plt.scatter(age2,unemployment2)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,3)
plt.scatter(age3,unemployment3)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,4)
plt.scatter(age4,unemployment4)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,5)
plt.scatter(age5,unemployment5)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,6)
plt.scatter(age6,unemployment6)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,7)
plt.scatter(age7,unemployment7)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,8)
plt.scatter(age8,unemployment8)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,9)
plt.scatter(age9,unemployment9)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,10)
plt.scatter(age10,unemployment10)
plt.xticks([42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.show()