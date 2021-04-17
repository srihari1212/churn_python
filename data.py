encode = {
    'colname':{'gender':{'male':1,'female':0},
                'SeniorCitizen':{'Yes':1,'No':0},
                'Partner':{'Yes':1, 'No':0},
                'Dependents':{'Yes':1, 'No':0},
                'PhoneService':{'Yes':1, 'No':0},
                'MultipleLines':{'No phone service':0, 'No':1, 'Yes':2},
                'InternetService':{'DSL':0, 'Fiber optic':1, 'No':2},
                'OnlineSecurity':{'No':0, 'Yes':1, 'No internet service':1},
                'OnlineBackup':{'Yes':2, 'No':0, 'No internet service':1},
                'DeviceProtection':{'No':0, 'Yes':2, 'No internet service':1},
                'TechSupport':{'No':0, 'Yes':2, 'No internet service':1},
                'StreamingTV':{'No':0, 'Yes':2, 'No internet service':1},
                'StreamingMovies':{'No':0, 'Yes':2, 'No internet service':1},
                'Contract':{'Month-to-month':0, 'One year':1, 'Two year':2},
                'PaperlessBilling':{'Yes':1, 'No':0},
                'PaymentMethod':{'Electronic check':2, 'Mailed check':3, 'Bank transfer (automatic)':0, 'Credit card (automatic)':1},

    } 
}

