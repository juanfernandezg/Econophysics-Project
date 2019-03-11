import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from functools import reduce

plt.close('all')

def openFile():
    with open("gemini_BTCUSD_2015_1min.csv") as csv_file:
    
        print("File opened!")
    
        csv_reader = csv.reader(csv_file, delimiter = ",")
        line_count = 0
    
    
        for row in csv_reader:
            if line_count == 1:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
                
            elif line_count == 0:
                # skips over line_count = 0
                # stops parsing over first line in .csv file
                line_count += 1
            
            elif line_count > 1:
                #print(f'\t{row[0]} is timestamp, {row[1]} is date and {row[2]} is symbol.')
                print(row)
                line_count += 1
            
            
                
        print("Done!")
        
def openFileAsPanda():
    with open("gemini_BTCUSD_2015_1min.csv") as csv_file:
        data = pd.read_csv(csv_file)
        print("Prices in USD imported.")
    
    with open("USACPI.csv") as csv_file:
        inflation = pd.read_csv(csv_file)
        print("Inflation imported.")
        
    return data, inflation
    
# returns the factors of a number n
def factors(n):    
    # this part adds each factor to a list
    return np.array(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))     

# returns a factors from number n
def factors_a(n,a): 
    multiplier = n**(1/a)
    factors = np.zeros(a)
    for i in range(a):
        factors[i] = multiplier**(i+1)

    # Convert to array of integers
    return factors.astype(int)    
            
<<<<<<< HEAD
###########################################                
#### MAIN CODE FOR EXECUTING FUNCTIONS HERE
###########################################    

=======
                
#def main():     I HAVE MAIN OPEN TO DEBUG
>>>>>>> 3c19dd7afe974bf9856456f2556266f06ed8f3a5
# The prices of cryptocurrencies in USD are imported
# Inflation is also imported
data, inflation = openFileAsPanda()

# change date so it can be plotted
# add a 'Returns' column
data['Formatted Date'] = [dt.datetime.strptime(date,'%d/%m/%Y %H:%M') for date in data['Date']]
#data['Assets Traded'] = data['Close'] * data['Volume']
data['Returns'] = data['Close'].diff()

length_max = len(data.index)
#==============================================================================
#     Plan to get a certain number of factors for the Hurst plot
#     round off to integers as
#     showed below:
#==============================================================================
# Get array with sizes of sections in time series 
facs = factors(length_max)
#facs = factors_a(length_max,10)    




#### Not sure what this commented out code means?
#    print('sample start')
#    for i in range(10):
#        print(np.zeros(np.int(fa2[i])))
#        
#    print('sample ends')
#    
#    plt.figure()
#    data.plot('Formatted Date', 'Assets')
#####



# calculate returns based on data stored 
# generally the first element in returns will be a NaN 
# replace NaN with 0.
rets = np.array(data['Returns'])
where_are_NaNs = np.isnan(rets)
rets[where_are_NaNs] = 0.

<<<<<<< HEAD
# cumulative sum of returns
rets_cumsum = np.cumsum(rets)

# list storing average of R/S for section sizes given (given as factors)
=======
####### Idea so far:
# Find factors of the total length of list - 121580       DONE in fa & fa2, we got to decide which one to use
# Use this as block length to calculate Hurst exponent 



#==============================================================================
# Below is the code that calculates the data used to obtain the hurst exponent
#==============================================================================
X = np.array(data['Close'])
x = np.zeros(data['Close'].shape) # For x & X to be of the same shape
x[:-1] = np.diff(X, n=1)
>>>>>>> 3c19dd7afe974bf9856456f2556266f06ed8f3a5
rav = []

# calculation of <R(fac)/S(fac)> for different section sizes fac
for fac in facs:
    r = []
    for k in range(np.int(length_max/fac)): 
        S = np.std(rets[k*fac:(k+1)*fac])
        R = np.max(rets_cumsum[k*fac:(k+1)*fac]) - np.min(rets_cumsum[k*fac:(k+1)*fac])
        r.append(R/S)                                         
        
    r = np.array(r)
    
<<<<<<< HEAD
    # give zero, instead of NaN, if S standard deviation is zero
    where_are_NaNs = np.isnan(r)
    r[where_are_NaNs] = 0.
    
    
    rav.append(np.mean(r))
 
# log both lists
lnN = np.log(facs)
=======
lnN = np.log(fa2)      # There's an error when obtaining the hurst exponent value
>>>>>>> 3c19dd7afe974bf9856456f2556266f06ed8f3a5
lnrav = np.log(rav)

plt.figure()
plt.plot(lnN,lnrav)

# fit lnN as x and lnrav as y as a linear fit
# in accordance with equation given in 'Statstical Properties of Financial Time Series'
plnNlnrav = np.polyfit(lnN,lnrav,1)
lnravfit = np.polyval(plnNlnrav,lnN)  

# print values of coefficients of linear fit
print(plnNlnrav)
    