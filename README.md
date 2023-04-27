

## Overview of Project
![image](https://user-images.githubusercontent.com/96621003/208570215-63a19f6d-bab7-4952-8bf3-0b4809553f99.png)
![image](https://user-images.githubusercontent.com/96621003/208570569-2526edc5-5d4d-4f2a-a9ce-48c895fc1760.png)

These are the following steps used in the preparation of whole Water Quality Prediction 
Model using 8 ML Algorithms.
### 1. Data Extraction
We have used contextual data in our case based on different parameters of water in which potability 
depends which is collected from river and oceans and placed in tabulated form so that we can use it 
for training our model. Got water quality prediction data-set having 9 parameters from Kaggle.
These are the nine parameters -pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic 
carbon, Trihalomethanes, Turbidity.
### 2. Data Cleaning
Missing values handling like how may null values are present in data, getting data shape & mean of a 
particular parameter etc. In performing missing values handling by removing null values (in the case 
where we can’t fill data with arbitrary values like name of a candidate in a data set but our data do 
not contain any such parameter hence not removing null values just filling them by mean values) and 
by filling mean in place of null values with the mean or mod etc.
### 3. Exploratory Data Analysis
#### • Normalisation
We have analysed data using histogram and found no need of normalisation 
#### • Dimensionality Reduction
For dimensionality reduction we need to check which feature is less important after checking 
data correlation’s through heatmap they aren’t correlating even about 50% hence we haven’t 
done dimensionality reduction and have used all the 9 parameters.
#### • Outliner removal 
Outlier removal means when you are too away from the mean we can check the outlier by 
using boxplot our data we are having outlier in solids parameter so we have a choice to 
remove this outlier or not so we choose not to remove it because it might be possible that 
water is good or drinkable due to excess of solids. 
### 4. Data Partitioning
Data set is divided into X_test, Y_test, X_train, Y_train
### 5. Model training
Model is trained using 8 ML algorithms.
### 6. Model Testing
Model is tested using X_test and comparison is made with Y_test to check whether outcome is 
correct or not. Rather to check whether model is working fine or not.
### 7. Model Optimization
Model is optimised by using the best parameters with the classifiers and these best parameters are found using 
Grid Search CV. Where cross validation is made to enhance performance- cross validation 1st 1/5th will go 
for testing and rest 4/5th will go for training splitting X_train into training and testing itself group will go for 
training and testing every time hence it's a good approach
![image](https://user-images.githubusercontent.com/96621003/208570936-e56a7b80-3255-4da9-8596-c5b90de509be.png)
![image](https://user-images.githubusercontent.com/96621003/208570984-1b74646b-371a-4187-b235-0be545d6a0dc.png)

![image](https://user-images.githubusercontent.com/96621003/208570822-a47a5105-3047-4a19-8555-b1c8a95e1989.png)

### 8. Model Evaluation
Performance measures => recall, precision , Accuracy , F1-score is calculated using confusion 
matrix and based on that model is evaluated that which is performing the best.
EDA – Exploratory Data Analysis in EDA here we prepare the data by exploring the data
## Conclusion
We can observe from the mentioned below bar graph that XGBoost Classifier has clearly 
outperformed other methods. It has the maximum achieved accuracy i.e., 67.097967.

![image](https://user-images.githubusercontent.com/96621003/208570713-ece5acf0-32dc-4fcf-b449-167fb6440b2a.png)

If we see with respect to other parameters as well then, we have the highest precision, recall, F1-score for XGBoost 
shown below comparison with Gaussian Naïve Bayes.

![image](https://user-images.githubusercontent.com/96621003/208571108-90a10887-e3e7-40e3-b619-82928ef94c9d.png)

#### Hence, we can conclude that XGBoost classifier trained model gives the best prediction of water quality 
