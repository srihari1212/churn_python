# Churn predictor
Churn predictor is a end to end Flask application that predicts whether `a customer will move out of company or will stay`.

## URL
Run this App [HERE](https://churn--predic.herokuapp.com/)

Created By
----------
Sri hari K V
https://bit.ly/34R7lrj

## Dataset
Thanks to Kaggle
You can find dataset [HERE](https://www.kaggle.com/blastchar/telco-customer-churn)

## installation
one can install required packages for this application using 
```bash
pip install -r requirements
```
## Separate environment
Alwas create a separate `conda environment/any environment` so that you can avoid version errors between packages

## usage
After installing the required packages use the following command to start the flask app
```bash
python wsgi.py
```

## folder structure
```bash
'
.
├── models                      #model created for churn prediction application
    ├── decision_tree.pkl
    ├── gaussian.pkl
    ├── kernal_svm.pkl
    ├── knn.pkl
    ├── logistic.pkl
    ├── random_forest.pkl
    └── svm.pkl
├── static                      #contains required fonts images css 
    ├── fonts
    ├── images
├── templates                   #contains required HTML files
    ├── index.html
├── BI.pbix                     #Power BI dash board for Churn 
├── Procfile                    #file for Heroku deployment
├── README.md
├── churn.log                   #all logs will be logged here
├── customer_churn_data.csv     #dataset
├── data.py                     #data from UI are decoded for model using this
├── last_churn.ipynb            #File which generated all pkl files
├── log.conf                    #config file for structure of logs
├── requirements.txt
├── test_list.py                #models got tested here
├── validating.py               #core script with API that finds the result
└── wsgi.py                     #web server gateway Interface
```

## Important Tools used
* python 3.7
* anaconda-jupyternotebook
* conda environment
* flask
* html
* css
* js

## Steps for training models
* cleaning the data - `totalcharges` from object to float
* Check for `Null` values and remove them using `mean imputation`
* Encoding all the labels in data using `sklearn.preprocessing-LabelEncoder`
* Visualise `correlation` between each variable and target(churn)
* Check `Multicollinearity` using Variable Inflation Factors (VIF)
* monthly charges and totalcharges have high multicollinearity with others and both are highly correlated(from correlation plot), so `drop one`
* split into `train and test` data - `0.8:0.2`
* `normalize` using StandardScaler
* should not use accuracy as metric since this is `imbalance data`, since this is churn,`false negatives are more costly than false positives`, `Recall` will be better
* Tune hyperparameter (k in knn,no of trees for RF)
* Fitting models
* Ensembling the results using mode

## Models used
* Logistic regression
* SVM (Linear)
* K-Nearest Neighbours
* Kernel SVM
* Naive Byes
* Decision Tree
* Random Forest

## Accuracy range
The overall accuracy range was between `78 to 82`
Recall range `0.52 to 0.71` >0.5 , so not bad 

## Input 
Fill the Information about customer required by model in web app's UI

## Output
It will say whether
    `this customer will stay - not churn`
                or
    `this customer will leave - churn`

Logging is included
-------------------
This API is `completely logged` in churn.log file. So Application can be monitered any time

## Deployment
This Application is Deployed in Heroku Platform. 
To Run this App [CLICK HERE](https://churn--predic.herokuapp.com/)
