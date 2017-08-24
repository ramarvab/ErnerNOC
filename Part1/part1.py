#D:\Study\MS in CS\Post Grad\all-data.tar\all-data\csv

# Rank the data streams with nans and 0s
# Ignore data streams that appears to hold only binary

import os
import pandas as pd
import numpy as np
import sys

#path = "/Users/rama.arvabhumi/Desktop/Erner/all-data/csv/"
# file = path+"\\6.csv"
ranks = []
ignoredfiles =[]

def rankFiles(pathLocation):
	if os.path.exists(pathLocation):
		for file in os.listdir(pathLocation):
			try:
				if ".csv" not in os.path.abspath(file):
					continue
				df = pd.read_csv(os.path.join(pathLocation,file), usecols=[2])
				intervals = df['value'].count().sum()

				# if there are strings in the value clolumn then data type of vaue column in object.
				if df['value'].dtype=="object":
					zeroes = (df['value']=="0").sum()
				else:
					zeroes = (df['value'] == 0).sum()
				#print(zeroes)
				#checking for any non numeric or strings in the given data set.
				nans = np.isnan(pd.to_numeric(df['value'], errors='coerce')).sum()
				#print(nans)
				ones = (df['value']==1).sum()
				#ignoring the data stream if it contains only 0 and 1.
				if intervals == ones+zeroes:
					ignoredfiles.append(file)
					continue
				ranks.append((zeroes+nans, file, str(round(100*(zeroes+nans)/intervals,2))+"%"))
			except:
				print ("Unexpected error in procesisng files",sys.exc_info()[0])
		ranks.sort(reverse=True)
		return ranks,ignoredfiles
	else:
		raise Exception(" the given path does not exist")


if __name__ == '__main__':
	if len(sys.argv) !=2:
		raise Exception(" please specify path to the files")
	# reading the system specified path value
	pathLocation = sys.argv[1]
	ranks,ignoredfiles = rankFiles(pathLocation)
	print ("File",10*" ","% 0s/NaNs",10*" ","No. of 0s/NaNs")
	for entry in ranks:
		print (entry[1],(17-2-len(entry[1]))*" ",entry[2],(22-len(entry[2]))*" ",entry[0])
	if len(ignoredfiles) ==0:
		print (" There are no streams with values 0 and 1")
	else:
		print("The ignored streams with 0 and 1 are")
		for stream in ignoredfiles:
			print (stream)
