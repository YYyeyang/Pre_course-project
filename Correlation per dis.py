import function_data_per_dis
import matplotlib.pyplot as plt
import itertools

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

#unemployments = [function_data_per_dis.convert(unemployment_dic,i) for i in range(1,11)]

plt.subplot(2,5,1)
plt.plot(age1[0],unemployment1[0], markersize=40, marker='+')
plt.plot(age1[1],unemployment1[1], markersize=40, marker='o')
plt.plot(age1[2],unemployment1[2], markersize=40, marker='v')
plt.plot(age1[3],unemployment1[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])
plt.title("Ciutat Vella")
plt.ylabel("No. unemployment")
plt.xlabel("Age")

plt.subplot(2,5,2)
plt.plot(age2[0],unemployment2[0], markersize=40, marker='+')
plt.plot(age2[1],unemployment2[1], markersize=40, marker='o')
plt.plot(age2[2],unemployment2[2], markersize=40, marker='v')
plt.plot(age2[3],unemployment2[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,3)
plt.plot(age3[0],unemployment3[0], markersize=40, marker='+')
plt.plot(age3[1],unemployment3[1], markersize=40, marker='o')
plt.plot(age3[2],unemployment3[2], markersize=40, marker='v')
plt.plot(age3[3],unemployment3[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,4)
plt.plot(age4[0],unemployment4[0], markersize=40, marker='+')
plt.plot(age4[1],unemployment4[1], markersize=40, marker='o')
plt.plot(age4[2],unemployment4[2], markersize=40, marker='v')
plt.plot(age4[3],unemployment4[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,5)
plt.plot(age5[0],unemployment5[0], markersize=40, marker='+')
plt.plot(age5[1],unemployment5[1], markersize=40, marker='o')
plt.plot(age5[2],unemployment5[2], markersize=40, marker='v')
plt.plot(age5[3],unemployment5[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,6)
plt.plot(age6[0],unemployment6[0], markersize=40, marker='+')
plt.plot(age6[1],unemployment6[1], markersize=40, marker='o')
plt.plot(age6[2],unemployment6[2], markersize=40, marker='v')
plt.plot(age6[3],unemployment6[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,7)
plt.plot(age7[0],unemployment7[0], markersize=40, marker='+')
plt.plot(age7[1],unemployment7[1], markersize=40, marker='o')
plt.plot(age7[2],unemployment7[2], markersize=40, marker='v')
plt.plot(age7[3],unemployment7[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,8)
plt.plot(age8[0],unemployment8[0], markersize=40, marker='+')
plt.plot(age8[1],unemployment8[1], markersize=40, marker='o')
plt.plot(age8[2],unemployment8[2], markersize=40, marker='v')
plt.plot(age8[3],unemployment8[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,9)
plt.plot(age9[0],unemployment9[0], markersize=40, marker='+')
plt.plot(age9[1],unemployment9[1], markersize=40, marker='o')
plt.plot(age9[2],unemployment9[2], markersize=40, marker='v')
plt.plot(age9[3],unemployment9[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.subplot(2,5,10)
plt.plot(age10[0],unemployment10[0], markersize=40, marker='+')
plt.plot(age10[1],unemployment10[1], markersize=40, marker='o')
plt.plot(age10[2],unemployment10[2], markersize=40, marker='v')
plt.plot(age10[3],unemployment10[3], markersize=40, marker='*')
plt.xticks([41,42,43,44])
plt.yticks([800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800])

plt.figure()
plt.show()