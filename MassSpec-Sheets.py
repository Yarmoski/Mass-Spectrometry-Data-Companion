import pandas as pd 
import re
from numbers import Number
import math
import pprint
import openpyxl


index_column = 0 #columns are zero indexed
num_trials=int(input("Please enter the number of trials.")) #3
num_rows = int(input("Please enter the total number of rows.")) #36

num_columns = 100 #can be greater than actual number
data = pd.read_excel('raw_data.xlsx', usecols=range(1,num_columns)) #important: do not change name "data"






#Note: these functions rely on the the dataframe being called "data"

#Note: several functions assume that each unique nucleoside column name has the same first two characters
#in the title. the input data is promised to be standardized, so this is reasonable.


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

#custom mean function to ignore NaN values
def mean(lst):
	total = 0
	num_entries = len(lst)
	for i in lst:
		if not math.isnan(float(i)):
			total += i
	return total / num_entries

# def trial_averages():
	#pprint.pprint(list(chunks(raw_percentages, 3)))
# count = 0
# column_number = 0
# data_file = 0
# for i in list(chunks(raw_percentages, num_trials)):
# 	try:
# 		label = data.columns[column_number]
# 	except IndexError:
# 		pass

# 	#Change the column name to the next column once all averages for that column have been outputted
# 	data_file += 1
	
# 	if count == 0:
# 		data_file = 1
# 	count += num_trials
# 	if num_rows - count == 0:
# 		column_number += 1
# 		count = 0

# 	try:
# 		print("The average percent concentration for {} file {} is {}".format(label, data_file, mean(i)))
# 	except:
# 		print("Non-numeric values or missing data")
# 		continue

def percent_conc(nuc, row, value):
	"""
	Returns the percent concentration of a data value relative to its category/nucleoside. 
	Params:
	nuc - small string to indicate which nucleoside is of interest. EX: "5mC", "dA"
	row - row where this datapoint is stored.
	value - the value/area under the curve for the datapoint of interest.
	 """

	#case insensitivity
	total = 0
	#Loop a number of times equal to the number of columns
	for i in data.columns:
		#Check if this column name begins with the given string nuc
		label = re.search("^" + nuc, i)
		#If the column name begins with nuc (because re.search() returns matches)
		if label != None:
			#If the value at the given row in this column is a number
			if isinstance(data[label.string][row], Number):
				#If the value is not empty or NaN
				if not math.isnan(float(data[label.string][row])):
					#Add the value at this point to the variable total
					total+=data[label.string][row]
			else:
				continue
		else:
			continue
	#Check for division by 0
	if total == 0:
		return "Total is 0"
	#Check if value passed in is NaN
	if math.isnan(value):
		return "nan passed in"
	#Return the given value divided by total
	return value / total

def get_index_list(index_column):
	"""
	Returns a list containing the indexes of the dataset. 
	Params:
	index_column - The column number where the indexes are contained.
	 """
	#initialize empty list
	index_list = []
	#set column_name equal to the index_column's name
	column_name = data.columns[index_column]
	loop through each index
	for title in data[column_name]:
		#if the title of the index is less than or equal to 10 characters, go to the next iteration
		#this is because index titles are longer than 10 characters so anything less can be discarded
		if len(title) <= 10:
			continue
		#add the index title to the list
		index_list.append(title)
	#return the list with all of the index titles
	return index_list

def create_conc_list(column_name):
	"""
	Returns a list containing the percent concentrations of each data point of the column.
	Params:
	column_name - name of the column for which the concentration list is to be created
	 """
	#initialize empty list
	conc_list = []
	#store all of the raw values in column_values
	column_values = data[column_name]
	#loop through each row
	for row in data.index:
		#skip the first row (!)
		if row == 0: 
			continue
		#add the percent concentration of the current data value to the list
		conc_list.append(percent_conc(column_name[0:2], row, column_values[row]))
	#return the list containing the percent concentrations
	return conc_list



def get_column_names():
	name_list = []
	for column_name in data.columns:
		if column_name[0:2] in get_nuc_list():
			print(column_name)	
			name_list.append(column_name)
	return name_list

def excel_output():
	title_list = get_nuc_list()
	with pd.ExcelWriter('Data_Output.xlsx') as writer:
		x = 0
		for i in create_df_list():
			print(i)
			i.to_excel(writer, sheet_name=title_list[x])
			x += 1

####APP

	

# for column_name in data.columns:
# 	pprint.pprint(create_conc_list(column_name))

excel_output()



	



	

