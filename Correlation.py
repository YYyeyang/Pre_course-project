import build_and_convert
import numpy
import matplotlib.pyplot as plt

age_dic= build_and_convert.build('Avg_age_processed.csv')
unemployment_dic= build_and_convert.build('Registered_unemployment_processed.csv')

print(age_dic)
print(unemployment_dic)

age2013=build_and_convert.convert(age_dic,2013)
print(age2013)

unemployment2013=build_and_convert.convert(unemployment_dic,2013)

sig2013 = numpy.corrcoef(age2013,unemployment2013)[0,1]
print(sig2013)

plt.scatter(age2013,unemployment2013)
plt.show()
