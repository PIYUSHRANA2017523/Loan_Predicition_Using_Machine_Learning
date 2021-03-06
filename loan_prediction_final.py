# -*- coding: utf-8 -*-
"""Loan_Prediction Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18tSZtEfZX10h97tcEuX1R4JKED2Wq4cd
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd                       # for reading the files
import numpy as np                        # for creating multi-dimensional-array
import matplotlib.pyplot as plt           # for plotting
import seaborn as sns                     # for data visulization
import warnings                           # for ignoring the warnings
warnings.filterwarnings("ignore")
# %matplotlib inline

test= pd.read_csv('/content/Test.csv')
train= pd.read_csv('/content/train.csv')

test.head()

test.shape

train.head()

train.shape

test_original= test.copy()
train_original= train.copy()

test.dtypes

train.dtypes

train['Loan_Status'].value_counts()                    #counting the values of different Loan Status

train['Loan_Status'].value_counts().plot.bar()

train['Loan_Status'].value_counts(normalize=True).plot.bar()
# normalize = True will give the probability in y-axis

plt.title("Loan Status")

plt.figure()
plt.subplot(321)
train['Gender'].value_counts(normalize=True).plot.bar(figsize=(20,20),title='Gender')

plt.subplot(322)
train['Married'].value_counts(normalize=True).plot.bar(figsize=(20,20),title='Married')

plt.subplot(323)
train['Education'].value_counts(normalize=True).plot.bar(figsize=(20,20),title='Education')

plt.subplot(324)
train['Self_Employed'].value_counts(normalize=True).plot.bar(figsize=(20,20),title='Self-Employed')

plt.subplot(325)
train['Credit_History'].value_counts(normalize=True).plot.bar(figsize=(20,20),title='Credit_History')

plt.figure()
plt.subplot(121)
train['Dependents'].value_counts(normalize=True).plot.bar(figsize=(20,5),title='Dependents')

plt.subplot(122)
train['Property_Area'].value_counts(normalize=True).plot.bar(figsize=(20,5),title='Property Area')

plt.subplot(121)
sns.distplot(train['ApplicantIncome'])
plt.subplot(122)
train['ApplicantIncome'].plot.box(figsize=(20,5))

train.boxplot(column='ApplicantIncome',by='Education')
plt.suptitle("")

plt.subplot(121)
sns.distplot(train['CoapplicantIncome'])
plt.subplot(122)
train['CoapplicantIncome'].plot.box(figsize=(20,5))

df=train.dropna()
plt.subplot(121)
sns.distplot(df['LoanAmount'])

plt.subplot(122)
df['LoanAmount'].plot.box(figsize=(20,5))

Gender=pd.crosstab(train['Gender'],train['Loan_Status']) 
Gender

Gender.div(Gender.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))

Married=pd.crosstab(train['Married'],train['Loan_Status']) 
Married

Married.div(Married.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))

Dependents=pd.crosstab(train['Dependents'],train['Loan_Status']) 
Dependents

Dependents.div(Dependents.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(4,4))

Education= pd.crosstab(train['Education'],train['Loan_Status'])
Education

Education.div(Education.sum(1).astype(float),axis=0).plot(kind="bar", stacked=True, figsize=(4,4) )

Self_Employed= pd.crosstab(train['Self_Employed'],train['Loan_Status'])
Self_Employed

Self_Employed.div(Self_Employed.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True,figsize=(4,4))

Credit_History= pd.crosstab(train['Credit_History'],train['Loan_Status'])
Credit_History

Credit_History.div(Credit_History.sum(1).astype(float),axis=0).plot(kind="bar",stacked=True, figsize=(4,4))

Property_Area=pd.crosstab(train['Property_Area'],train['Loan_Status'])
Property_Area

Property_Area.div(Property_Area.sum(1).astype(float),axis=0).plot(kind='bar', stacked=True, figsize=(4,4))

bins=[0,2500,4000,6000,8100] 
group=['Low','Average','High', 'Very high'] 
train['Income_bin']=pd.cut(train['ApplicantIncome'],bins,labels=group)

Income_bin=pd.crosstab(train['Income_bin'],train['Loan_Status']) 
Income_bin.div(Income_bin.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True) 
plt.xlabel('ApplicantIncome') 
P=plt.ylabel('Percentage')

bins=[0,1000,3000,42000] 
group=['Low','Average','High'] 
train['Coapplicant_Income_bin']=pd.cut(train['CoapplicantIncome'],bins,labels=group)
Coapplicant_Income_bin=pd.crosstab(train['Coapplicant_Income_bin'],train['Loan_Status']) 
Coapplicant_Income_bin.div(Coapplicant_Income_bin.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True) 
plt.xlabel('CoapplicantIncome') 
P = plt.ylabel('Percentage')

train['Total_Income']=train['ApplicantIncome']+train['CoapplicantIncome']
bins=[0,2500,4000,6000,81000] 
group=['Low','Average','High', 'Very high'] 
train['Total_Income_bin']=pd.cut(train['Total_Income'],bins,labels=group)
Total_Income_bin=pd.crosstab(train['Total_Income_bin'],train['Loan_Status']) 
Total_Income_bin.div(Total_Income_bin.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True) 
plt.xlabel('Total_Income') 
P = plt.ylabel('Percentage')

bins=[0,100,200,700] 
group=['Low','Average','High'] 
train['LoanAmount_bin']=pd.cut(train['LoanAmount'],bins,labels=group)
LoanAmount_bin=pd.crosstab(train['LoanAmount_bin'],train['Loan_Status']) 
LoanAmount_bin.div(LoanAmount_bin.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True) 
plt.xlabel('LoanAmount') 
P = plt.ylabel('Percentage')

train['Dependents'].replace('3+', 3,inplace=True) 
test['Dependents'].replace('3+', 3,inplace=True)

train['Loan_Status'].replace('N', 0,inplace=True) 
train['Loan_Status'].replace('Y', 1,inplace=True)

matrix = train.corr() 
plt.figure(figsize=(9,6))
sns.heatmap(matrix, square=True, cmap="BuPu")

train=train.drop(['Income_bin', 'Coapplicant_Income_bin', 'LoanAmount_bin', 'Total_Income_bin', 'Total_Income'], axis=1)

train.head()

train.isnull().sum()

train['Gender'].fillna(train['Gender'].mode()[0],inplace=True)

train['Married'].fillna(train['Married'].mode()[0],inplace=True)

train['Dependents'].fillna(train['Dependents'].mode()[0],inplace=True)

train['Self_Employed'].fillna(train['Self_Employed'].mode()[0],inplace=True)

train['Credit_History'].fillna(train['Credit_History'].mode()[0],inplace=True)

train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].mode()[0],inplace=True)

train['LoanAmount'].fillna(train['LoanAmount'].median(),inplace=True)

test['Gender'].fillna(test['Gender'].mode()[0],inplace=True)

test['Married'].fillna(test['Married'].mode()[0],inplace=True)

test['Dependents'].fillna(test['Dependents'].mode()[0],inplace=True)

test['Self_Employed'].fillna(test['Self_Employed'].mode()[0],inplace=True)

test['Credit_History'].fillna(test['Credit_History'].mode()[0],inplace=True)

test['Loan_Amount_Term'].fillna(test['Loan_Amount_Term'].mode()[0],inplace=True)

test['LoanAmount'].fillna(test['LoanAmount'].median(),inplace=True)

train['LoanAmount_log'] = np.log(train['LoanAmount']) 
train['LoanAmount_log'].hist(bins=20) 


test['LoanAmount_log'] = np.log(test['LoanAmount'])
test['LoanAmount_log'].hist(bins=20)

train=train.drop('Loan_ID',axis=1)
train.head()

test=test.drop('Loan_ID',axis=1)
test.head()

train=train.drop('Gender',axis=1)
test=test.drop('Gender',axis=1)

train=train.drop('Dependents',axis=1)
test=test.drop('Dependents',axis=1)

train=train.drop('Self_Employed',axis=1)
test=test.drop('Self_Employed',axis=1)

x=train.drop('Loan_Status',axis=1)
x.head()

y=train['Loan_Status']
y.head()

x=pd.get_dummies(x) 
train=pd.get_dummies(train) 
test=pd.get_dummies(test)

x.head()

from sklearn.model_selection import train_test_split
x_train, x_cv, y_train, y_cv = train_test_split(x,y, train_size =0.75,random_state=0)

from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score
model = LogisticRegression() 
model.fit(x_train, y_train)

pred_cv = model.predict(x_cv)

accuracy_score(y_cv,pred_cv)

from sklearn.metrics import confusion_matrix
c=confusion_matrix(y_cv,pred_cv)
c

test.head()

pred_test = model.predict(test)

submission=pd.read_csv("/content/Sample_Submission.csv",header=0)

submission['Loan_Status']=pred_test 
submission['Loan_ID']=test_original['Loan_ID']

submission.head()

submission['Loan_Status'].replace(0, 'N',inplace=True) 
submission['Loan_Status'].replace(1, 'Y',inplace=True)

pd.DataFrame(submission, columns=['Loan_ID','Loan_Status']).to_csv('logistic.csv')

submission

from statistics import mean

from sklearn.model_selection import StratifiedKFold

i=1 
pred_scores=[]
kf = StratifiedKFold(n_splits=5,random_state=1,shuffle=True) 
for train_index,test_index in kf.split(x,y):
    print('\n{} of kfold {}'.format(i,kf.n_splits))
    xtr,xvl = x.loc[train_index],x.loc[test_index]
    ytr,yvl = y[train_index],y[test_index]
    model = LogisticRegression(random_state=1)
    model.fit(xtr, ytr)
    pred_test = model.predict(xvl)
    score = accuracy_score(yvl,pred_test) 
    print('accuracy_score',score)     
    i+=1 
    pred_test = model.predict(test) 
    pred=model.predict_proba(xvl)[:,1]
    pred_scores.append(score)
print("\nMean of Accuracy Scores=",mean(pred_scores))

from sklearn import tree

i=1 
kf = StratifiedKFold(n_splits=5,random_state=1,shuffle=True) 
for train_index,test_index in kf.split(x,y):     
    print('\n{} of kfold {}'.format(i,kf.n_splits))     
    xtr,xvl = x.loc[train_index],x.loc[test_index]     
    ytr,yvl = y[train_index],y[test_index]         
    model = tree.DecisionTreeClassifier(random_state=1)     
    model.fit(xtr, ytr)     
    pred_test = model.predict(xvl)     
    score = accuracy_score(yvl,pred_test)     
    print('accuracy_score',score)     
    i+=1 
pred_test = model.predict(test)

submission['Loan_Status']=pred_test            
submission['Loan_ID']=test_original['Loan_ID'] 
submission.head()

submission['Loan_Status'].replace(0, 'N',inplace=True) 
submission['Loan_Status'].replace(1, 'Y',inplace=True)

pd.DataFrame(submission, columns=['Loan_ID','Loan_Status']).to_csv('Decision Tree.csv')

new_X = (5849,0.0,128.0,360.0,1.0,4.852030,1,0,1,0,0,0,1)
new_arr = np.asarray(new_X)
arr_reshaped = new_arr.reshape(1,-1)
prediction = model.predict(arr_reshaped)
print(prediction)
if(prediction[0] == 1.0):
  print("Loan Approved")
else:
  print("Loan Disapproved")

new_X = (5000,1800,208.0,360.0,1.0,5.337538,0,1,1,0,0,0,1)
new_arr = np.asarray(new_X)
arr_reshaped = new_arr.reshape(1,-1)
prediction = model.predict(arr_reshaped)
print(prediction)
if(prediction[0] == 1.0):
  print("Loan Approved")
else:
  print("Loan Disapproved")