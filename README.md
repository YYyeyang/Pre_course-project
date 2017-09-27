# Pre_course-project
**Neighbourhood demography vs. No. of unemployment in Barcelona**


1.	Data source:

		CSV files from open data Barcelona
		Example: http://opendata-ajuntament.barcelona.cat/data/en/dataset/ine-ine17


2.	Input

		Matchable variables:
	
			a. Neighbourhood
			b. Years
			c. Registered unemployment
  
		Non-matchable variables:
	
			d. Age
			e. Nationality
  

3.	Processing

		a. Calculate whether younger neighbourhood has higher employment, and if it changes over the year
		   Input needed: a/b/c/d

		b. Calculate which nationality has higher employment, and if it changes over the year
		   Input needed: a/b/c/e
	


4.	Output

		a. Result of the correlation in number and in graphs
		b. Maybe create a heatmap?


5.	Current status

		a. Finished:
			1. Pre-processed my CSV files, so I could easliy access the data I need
			2. Built a funtion that creates a dictionary with years and districts
			3. Got dictionary 1: Average age in each distrcit in each year
			4. dictionary 2: Average unemployment in each distrcit in each year
			
		b. To be done:
			1. Convert my dictionaries into a list
			2. Use numpy to calculate the correlation between age and unemployment
			3. Plot my correlations
			4. Decide what to do with the nationality data? Take the max nationality to represent one district?
			5. Heatmap maybe??
		
