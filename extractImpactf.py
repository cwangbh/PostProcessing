# to extract the impact force on the rigid barrier
import pandas as pd 
import glob
import re
import matplotlib.pyplot as plt

#define the numerical sort function
def numericalsort(value):
    number=re.compile(r"(\d+)")
    parts=number.split(value)
    return int(parts[1])

# read in all the sorted csv files (sorted by the file number)
rootname=r"impact"
filelist=glob.glob(rootname+'_*.csv')
filelist=sorted(filelist,key=numericalsort)
print filelist

#functions:
# process each csv file and generate the output file

def sortDataframe(eachtimestep):
    xmin=1200
    ymin=0
    xmax=1250
    ymax=1000
    file1=pd.read_csv(eachtimestep,names=['x','y','z','fx','fy','fz'],header=None,index_col=False,delimiter=r"[\s+]",skiprows=[0])
    file1.convert_objects(convert_numeric=True)
    #pd.to_numeric(file1)
    file1.sort_values('x',0,inplace=False)
    # SLICE TO GET THE mesh points for the barrier
    file1[((file1.x>=xmin) &(file1.x<=xmax) )]
    file1[((file1.y>=ymin)&(file1.y<=ymax))]
    return file1

# loop all the files
# plot the figure and save
xforce=[]
for eachtimestep in filelist:
    tempframe=sortDataframe(eachtimestep)
    temp_fx_sum=tempframe.fx.sum()
    xforce.append(temp_fx_sum)

plt.plot([(-x) for x in xforce])
plt.show()