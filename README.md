# churn_python
URL
----
https://churn--predic.herokuapp.com/

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
├── models
    ├── decision_tree.pkl
    ├── gaussian.pkl
    ├── kernal_svm.pkl
    ├── knn.pkl
    ├── logistic.pkl
    ├── random_forest.pkl
    └── svm.pkl
├── static
    ├── fonts
    ├── images
├── templates
    ├── index.html
├── BI.pbix
├── Procfile
├── README.md
├── churn.log
├── customer_churn_data.csv
├── data.py
├── last_churn.ipynb
├── log.conf
├── requirements.txt
├── test_list.py
├── validating.py
└── wsgi.py
```

## About Resnet50
Resnet50 is a `pretrained model` by Imagenet which is `50 layers deep` and already got trained with 1000 categories. Here I used `transfer learning` process to retrain resnet50 for pneumonia data obtained from kaggle. 

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
