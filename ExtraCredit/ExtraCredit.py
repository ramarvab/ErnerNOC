import sys,os
import pandas as pd

def calculatestats(file):
    newdf = pd.DataFrame()
    df = pd.read_csv(file, usecols=[1, 2])
    mean = df['value'].mean()
    sd = df['value'].std()
    return mean,sd

if __name__ == '__main__':
    if len(sys.argv) !=2:
        raise Exception(" please specify path to the files")
    # reading the system specified path value
    pathLocation = sys.argv[1]
    if os.path.exists(pathLocation):
        for file in os.listdir(pathLocation):
            if ".csv" not in os.path.abspath(file):
                continue
            #print ("Calculating Stats for" + file)
            #print (os.path.join(pathLocation,file))
            mean,sd = calculatestats(os.path.join(pathLocation,file ))

            print (file,mean,sd)