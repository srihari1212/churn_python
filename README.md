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

## About models

## Important Tools used
* python 3.7
* anaconda-jupyternotebook
* conda environment
* flask
* html
* css
* js

## Training time
I trained the model through `50 epoch (cycles)`
For 50 cycles it took aroung `6 hours`

## Accuracy range
The overall accuracy range was between `88 to 91`

## Input 
After running the application just upload a `x-ray image`

## Output
It will say whether
    `The person is normal`
                or
    `The person has pnuemonia`
    
## Deployment
Now this is running `locally in my PC`
I tried with `Heroku` platform
But I couldnt deploy , since I used `Git LFS` to upload my 98.3mb .h5 model file, heroku couldnt pull LFS files to its server since I only have a `FREE TIER` account  
