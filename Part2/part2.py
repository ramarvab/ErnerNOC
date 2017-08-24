import os, dateutil
import statistics
import csv,sys
import pandas as pd
import numpy as np
import sqlite3
import time,datetime

#path = "/Users/rama.arvabhumi/Desktop/Erner/all-data/csv"
#file = path+"/6.csv"

conn = sqlite3.connect('ErnerNOC')

c = conn.cursor()

#create table
#c.execute('Create TABLE if not exists HourlyStats(id INT,date DATETIME, total REAL,minimum REAL, maximum REAL, mean REAL,median REAL)')
def consolidate(values):
	return round(sum(values),4), min(values), max(values), round(statistics.mean(values),4), round(statistics.median(values),4)

def calculatestats(file,filename):
	dailyStats =[]
	hourlyStats = []
	csvfile = open(file, "r")
	filereader = csv.reader(csvfile)
	next(filereader) #skips headers
	valuesForHourly = []
	valuesForDaily = []
	prevDate = ""

	for row in filereader:
		currDate = row[1].strip().split(" ")[0]
		dateobject =datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
		minute = dateobject.minute
		second = dateobject.second
		try:
			x = float(row[2])
		except:
			pass
		else:
			valuesForHourly.append(float(row[2]))
			valuesForDaily.append(float(row[2]))
		finally:
			if minute == 00 and second == 00:
				total, minimum, maximum, mean, median = consolidate(valuesForHourly)
				valuesForHourly = []
				hourlyStats.append((total, minimum, maximum, mean, median,row[1],filename))
				if(prevDate!="" and currDate!=prevDate):
					total, minimum, maximum, mean, median = consolidate(valuesForDaily)
					dailyStats.append((total, minimum, maximum, mean, median, currDate,filename))
					valuesForDaily = []
			prevDate = currDate
	csvfile.close()
	return hourlyStats,dailyStats



if __name__ == '__main__':

	start_time = time.time()
	conn = sqlite3.connect('ErnerNOC')
	c = conn.cursor()
	# create table
	#c.execute('DELETE FROM HourlyStats')
	#c.execute('DELETE FROM DailyStats')
	#c.execute('Drop TABLE HourlyStats')
	c.execute('Create TABLE if not exists HourlyStats(id INT,date DATETIME, total REAL,minimum REAL, maximum REAL, mean REAL,median REAL,filename TEXT)')
	c.execute('Create TABLE if not exists DailyStats(id INT,date DATETIME, total REAL,minimum REAL, maximum REAL, mean REAL,median REAL,filename TEXT)')
	if len(sys.argv) !=2:
		raise Exception(" please specify path to the files")
	# reading the system specified path value
	pathLocation = sys.argv[1]

	if os.path.exists(pathLocation):
		for file in os.listdir(pathLocation):
			if ".csv" not in os.path.abspath(file):
				continue
			print ("Calculating Stats for" + file)
			print (os.path.join(pathLocation,file))
			hourlyStats,dailyStats = calculatestats(os.path.join(pathLocation,file),file)
			print (len(hourlyStats),len(dailyStats))

			print("========================Hourly Stats ============================================")
			id = 1
			hour = 1
			for entry in hourlyStats:
				c.execute(
					"INSERT INTO HourlyStats(id,date,total,minimum,maximum,mean,median,filename) VALUES(?, ?, ?, ?, ?, ?, ?,?)",
					(id,entry[5], entry[0], entry[1], entry[2], entry[3], entry[4],entry[6]))
				print(id, entry[5], entry[0], entry[1], entry[2], entry[3], entry[4])
				id += 1
				hour += 1

			print("==========================Daily Stats ==================================")

			id = 1
			for entry in dailyStats:
				c.execute(
					"INSERT INTO HourlyStats(id,date,total,minimum,maximum,mean,median,filename) VALUES(?, ?, ?, ?, ?, ?, ?,?)",
					(id, entry[5], entry[0], entry[1], entry[2], entry[3], entry[4], entry[6]))
				print(id, entry[5], entry[0], entry[1], entry[2], entry[3], entry[4])
				id += 1
	conn.commit()
	conn.close()
	print("--- %s seconds ---" % (time.time() - start_time))