#supervised machine learning - regression
#in this case, it is simple linear regression -> goal is to model the data by fitting a line to it
#find m and b in y = mx + b
#https://www.youtube.com/watch?v=JcI5Vnw0b2c&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=2
#key = '7yRCWsxmUUEVjyrn14Jb' 
import quandl
import pandas as pd
import math
import pickle #pickle is a file that you can open and close when you want it
import datetime
import numpy as np
    #allows us to use arrays because Python doesn't have built in arrays
from sklearn import preprocessing, svm
    #preprocessing -> using scaling on the features to get them between -1 and 1
    #cross_validation -> to create our training and testing samples, a nice way to split up data and shuffle helping with unbiased statistics 
    #svm -> support vector machines
from sklearn.model_selection import cross_validate, train_test_split
    #instead of cross_validation
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt # to plot stuff
from matplotlib import style # to make it look decent

style.use('ggplot') # which decent looking thing you want
#features are the attributes that make up the label -> in this case, they are the continuous data
            #features: Open, High, Low, Close, Volume, etc.
#label is a prediction about the future
df = quandl.get('WIKI/GOOGL') #to find what goes in the '', go to Quandl.com, df -> dataframe
    #dataframes are made of lists, *numpy lists* -> fancy list, more functionalities
#print(df.head()) #prints out the data


df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']] #new dataframe with features that matter
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/df['Adj. Low'] * 100.0 #defines a new column in the dataframe df for HL_PCT
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] * 100.0 #defines a new column in the dataframe df for PCT_change
#want to simplify your data as much as possible
            #get rid of unneeded or irrelevant data

df = df[['Adj. Close', 'HL_PCT','PCT_change', 'Adj. Volume']] #new dataframe with features that matter
#print(df.head())

#figuring out what the label is
#https://www.youtube.com/watch?v=lN5jesocJjk&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=3
#the label will be the value of Adj. Close in the future, so we need to get some more info to figure that out
forecast_col = 'Adj. Close' #what you're forecasting, just a variable, just a String
df.fillna(-99999, inplace=True) #in case there's missing data, fill with -99999
                    #you do this because in machine learning, you can't work with nan data, but you don't want to delete data either
#generally you use regression to forecast out
forecast_out = int(math.ceil(0.01*len(df))) #trying to predict out 1% of the dataframe
        #math.ceil takes anything and gets it to the ceiling -> rounds everything up to the nearest whole number (0.2 -> 1)
        #len.df gets the length of the dataframe
        #int casts it because math.ceil returns a float
df['label'] = df[forecast_col].shift(-forecast_out) 
        #.shift(-forecast_out) shifts the columns up -> the label column for each row will be the Adj. Close 1% days into the future
#df.dropna(inplace=True)
#print(df.tail())

#training and testing in regression
#https://www.youtube.com/watch?v=r4mwkS2T9aI&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=4

X = np.array(df.drop(['label'], 1)) #because features are everything except the label
    #defined features
X = preprocessing.scale(X) #scaling X, needs to be done with other data
#X = X[:-forecast_out + 1] #because we shifted the values, so we want to make sure we're only using values of X where we have values of y, don't need actually because of df.dropna(inplace=True)
X_lately = X[-forecast_out:] # this is what we're going to predict against
X = X[:-forecast_out]


df.dropna(inplace=True)
y = np.array(df['label'])
    #label

#print(len(X), len(y)) #to check that we have the correct lengths
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.2) #0.2 -> 20% of data, shuffles up data

clf = LinearRegression() #classifier
clf.fit(X_train, y_train) #fit classifier
accuracy = clf.score(X_test, y_test) #test classifer
    #you want to use different data so that when you go to test, it hasn't already seen this information
#print(accuracy)

#using svm -> support vector regression
#to switch algorithms:
    #clf = svm.SVR() replaces clf = LinearRegression()
    #you could test it out with different things: clf = svm.SVR(kernel='poly') for example. which fits a polynomial

#when testing various algorithms, you want to check the documentation to look for which algorithms can be threaded
    #example: for linear regression, you look for n_jobs
            #you can thread linear regression as opposed to a support vector machine

#regression forecasting and predicting
#https://www.youtube.com/watch?v=QLVMqwpOLPk&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=5
#using scikit learn, to predict using linear regression
forecast_set = clf.predict(X_lately) # use the classifier to predict using X_lately
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan # set to empty
last_date = df.iloc[-1].name # get last date
last_unix = last_date.timestamp() # way to calculate time
one_day = 86400 # seconds in a day
next_unix = last_unix + one_day # the next day

#populate dataframe with new dates and forecast values
#for dates on the axes
for i in forecast_set:     #iterating through the forecast_set
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i] # setting the values equal to those in the data frame
    #.loc references the index of the data frame
        #.loc is the actual date like 2004-08-25
        #if the date there didn't exist -> create it
        #if the date existed -> replace it
    #sets the other columns in data frame to NaN because that data doesn't exist yet in the future
    #sets Forecast to i from forecast_set since it is the thing being predicted
df['Adj. Close'].plot() # plot Adj. Close
df['Forecast'].plot() # plot Forecast
plt.legend(loc=4) # putting in the bottom right, 4th position
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

#pickling and scaling
#https://www.youtube.com/watch?v=za5s7RB_VLw&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=6
#pickling is simply the serialization of any python object
#by pickling, you can skip the training step and directly use the already trained classifier
#clf = LinearRegression() #classifier
#clf.fit(X_train, y_train) #fit classifier
#accuracy = clf.score(X_test, y_test) #test classifer
with open('linearregression.pickle', 'wb') as f: #saves as temporary variable f
    pickle.dump(clf, f) #dumps classifier

#to use classifier
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)

#then you can delete these five lines:
#clf = LinearRegression() #classifier
#clf.fit(X_train, y_train) #fit classifier
#accuracy = clf.score(X_test, y_test) #test classifer
#with open('linearregression.pickle', 'wb') as f: #saves as temporary variable f
    #pickle.dump(clf, f) #dumps classifier
#only need this
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)
forecast_set = clf.predict(X_lately) # use the classifier to predict using X_lately
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan # set to empty
last_date = df.iloc[-1].name # get last date
last_unix = last_date.timestamp() # way to calculate time
one_day = 86400 # seconds in a day
next_unix = last_unix + one_day # the next day

#populate dataframe with new dates and forecast values
#for dates on the axes
for i in forecast_set:     #iterating through the forecast_set
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i] # setting the values equal to those in the data frame
    #.loc references the index of the data frame
        #.loc is the actual date like 2004-08-25
        #if the date there didn't exist -> create it
        #if the date existed -> replace it
    #sets the other columns in data frame to NaN because that data doesn't exist yet in the future
    #sets Forecast to i from forecast_set since it is the thing being predicted
df['Adj. Close'].plot() # plot Adj. Close
df['Forecast'].plot() # plot Forecast
plt.legend(loc=4) # putting in the bottom right, 4th position
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


#how regression works (behind the scenes)
#https://www.youtube.com/watch?v=V59bYfIomVk&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=7
