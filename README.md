# Pre_course-project
Neighbourhood demography vs. unemployment in Barcelona


1.	Data source:
CSV files from open data Barcelona
Example: http://opendata-ajuntament.barcelona.cat/data/en/dataset/ine-ine17

2.	Input
Matchable variables:
a.	Neighbourhoods
b.	Years
c.	Registered unemployment
Non-matchable variables:
d.	No. of population living alone
e.	Nationality
f.	Educational level
g.	Age

3.	Processing
a.	Calculate whether younger neighbourhood has higher employment, and if it changes over the year
i.	Input need: a/b/c/g
b.	Calculate which nationality has higher employment, and if it changes over the year
i.	Input need: a/b/c/e
c.	Calculate whether higher educational level has higher employment, and if it changes over the year
i.	Input need: a/b/c/f
d.	Calculate whether higher single house hold neighbourhood has higher employment, and if it changes over the year
i.	Input need: a/b/c/d

4.	Output
a.	Result of the correlation in number
b.	Or create a heatmap

5.	Methodology
a.	For correlations
i.	Reference:
1.	scipy & numpy
2.	https://stackoverflow.com/questions/3949226/calculating-pearson-correlation-and-significance-in-python

ii.	Pre-process my data
1.	Pivot each type of data into per district per year
2.	Make a dictionary from that
iii.	Read my CSV file
iv.	Match the variables
v.	Cal the avg and median age per neighbourhood 
vi.	Cal no. unemployment per neighbourhood
vii.	Cal significance between 2&3 for each year
viii.	See if significance change strongly over the year

b.	For heatmaps
i.	Reference:
https://martingonzalez.net/choropleth-maps-qgis-d3-spam
http://ramiro.org/notebook/basemap-choropleth/

ii.	load the necessary modules and specify the files for input and output
iii.	set the number of colours to use and meta information about what is displayed
iv.	need a code to identify the Barcelona neighbourhood? i.e. zip?
v.	map data values to colours, i.e. use Matplotlib's colormap API?
vi.	To plot the map? we first create a figure and add a subplot for the map itself?
vii.	…..
viii.	Use Barcelona map?

