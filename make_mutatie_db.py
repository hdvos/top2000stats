import pandas as pd 
import numpy as np


'''
given a filename
it reads this as a dataframe and returns the dataframe
'''
def read_rank_db(filename = "top2000_rank_db.csv", print_update = False):
	data = pd.read_table(filename, delimiter=';')
	
	if print_update:
		print('data loaded. Shape(r,c): {}'.format(data.shape))
	return data


'''
returns a numpy matrix given any compatible data.
'''
def make_matrix(data):
	return data.as_matrix()

'''
returns a pandas dataframe of a numpy.ndarray.
'''
def make_df(data_matrix, columns = None):
	return pd.DataFrame(data= data_matrix ,columns = columns)

'''
Checks whether song was in top 2000 in a year
Takes a cell from the top2000 database: the cell contains either the rank in the top2000 or  a '*' '-'
Retuns False if cell contains * or -. True otherwise
'''
def in_top2000(cell):
	return not ('*' in cell or '-' in cell)


'''
Takes a dataframe of two collumns
Substracts the first collumn from the second in order to get the mutation relative to the previous year
returns a clm with the mutations.
'''
def substract_years(data):
	data_matrix = make_matrix(data)
	mutatie_clm = []
	
	for row in data_matrix:
		if in_top2000(row[1]):
			if in_top2000(row[0]):
				
				mutatie = int(row[1]) - int(row[0])
			else:
				mutatie = 'i'
		else:
			if in_top2000(row[0]):
				mutatie = 'o'
			else:
				mutatie = '-'

		mutatie_clm.append(mutatie)

	mutatie_clm = np.array(mutatie_clm)
	return mutatie_clm



#"top2000_rank_db.csv", sep = ';'


def main():
	data = read_rank_db()
	
	#print (data[["Artiest", "Titel", "Jaar"]])
	newdf = data[["Artiest", "Titel", "Jaar"]]

	newcol = substract_years(data[["1999", "2000"]])
	newdf["1999-2000"] = pd.Series(newcol)


	newcol = substract_years(data[["2000", "2001"]])
	newdf["2000-2001"] = pd.Series(newcol)


	newcol = substract_years(data[["2001", "2002"]])
	newdf["2001-2002"] = pd.Series(newcol)


	newcol = substract_years(data[["2002", "2003"]])
	newdf["2002-2003"] = pd.Series(newcol)


	newcol = substract_years(data[["2003", "2004"]])
	newdf["2003-2004"] = pd.Series(newcol)


	newcol = substract_years(data[["2004", "2005"]])
	newdf["2004-2005"] = pd.Series(newcol)


	newcol = substract_years(data[["2005", "2006"]])
	newdf["2005-2006"] = pd.Series(newcol)


	newcol = substract_years(data[["2006", "2007"]])
	newdf["2006-2007"] = pd.Series(newcol)


	newcol = substract_years(data[["2007", "2008"]])
	newdf["2007-2008"] = pd.Series(newcol)


	newcol = substract_years(data[["2008", "2009"]])
	newdf["2008-2009"] = pd.Series(newcol)


	newcol = substract_years(data[["2009", "2010"]])
	newdf["2009-2010"] = pd.Series(newcol)


	newcol = substract_years(data[["2010", "2011"]])
	newdf["2010-2011"] = pd.Series(newcol)


	newcol = substract_years(data[["2011", "2012"]])
	newdf["2011-2012"] = pd.Series(newcol)


	newcol = substract_years(data[["2012", "2013"]])
	newdf["2012-2013"] = pd.Series(newcol)


	newcol = substract_years(data[["2013", "2014"]])
	newdf["2013-2014"] = pd.Series(newcol)


	newcol = substract_years(data[["2014", "2015"]])
	newdf["2014-2015"] = pd.Series(newcol)


	newcol = substract_years(data[["2015", "2016"]])
	newdf["2015-2016"] = pd.Series(newcol)
	print (newdf)


if __name__ == '__main__':
	main()
