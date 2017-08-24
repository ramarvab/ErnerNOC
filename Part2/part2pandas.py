import sys,os
import pandas as pd
import numpy as np
import time
def calculatestats(file):
    hourlydf = pd.DataFrame()
    dailydf = pd.DataFrame()
    df = pd.read_csv(file,usecols=[1,2])
    df = df.set_index(['dttm_utc'])
    df.index = pd.to_datetime(df.index)
    hourlydf['value'] = df.value.resample('H').sum()
    hourlydf['mean'] = df.value.resample('H').mean()
    hourlydf['median'] = df.value.resample('H').median()
    hourlydf['min'] = df.value.resample('H').min()
    hourlydf['max'] = df.value.resample('H').max()
    dailydf['value'] = df.value.resample('D').sum()
    dailydf['mean'] = df.value.resample('D').mean()
    dailydf['median'] = df.value.resample('D').median()
    dailydf['min'] = df.value.resample('D').min()
    dailydf['max'] = df.value.resample('D').max()
    return dailydf,hourlydf

if __name__ == '__main__':
    start_time = time.time()
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
            dailyStats,hourlyStats = calculatestats(os.path.join(pathLocation,file ))

            print("========================Hourly Stats ============================================")
            print (hourlyStats)
            print("==========================Daily Stats ==================================")
            print(dailyStats)
    print("--- %s seconds ---" % (time.time() - start_time))