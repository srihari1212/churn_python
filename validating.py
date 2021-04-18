import pickle
from data import  encode
from flask import Flask, render_template, request, make_response, jsonify
import logging
import logging.config
import statistics
from statistics import mode

app = Flask(__name__)

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)
logger = logging.getLogger('churnLogger')

@app.route('/')
def Home():
    try:
        logger.info('entered home')
        return render_template('index.html')
    except:
        logger.error("Error in starting the app",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in starting the app',
                        'result' : {}
                    }
                ), 400)

def pre_dict_decisiontree(data):
    try:
        model = pickle.load(open('models/decision_tree.pkl', 'rb'))
        prediction=model.predict([data])
        return prediction
    except:
        logger.error("Error in decision tree prediction",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in decision tree prediction',
                        'result' : {}
                    }
                ), 400)

def pre_dict_gaussian(data):
    try:
        model = pickle.load(open('models/gaussian.pkl', 'rb'))
        prediction=model.predict([data])
        return prediction
    except:
        logger.error("Error in gaussian prediction",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in gaussian prediction',
                        'result' : {}
                    }
                ), 400)

def pre_dict_kernal_svm(data):
    try:
        model = pickle.load(open('models/kernal_svm.pkl', 'rb'))
        prediction=model.predict([data])
        return prediction
    except:
        logger.error("Error in kernal SVM prediction",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in  kernal SVM prediction',
                        'result' : {}
                    }
                ), 400)


def pre_dict_knn(data):
    try:
        model = pickle.load(open('models/knn.pkl', 'rb'))
        prediction=model.predict([data])
        return prediction
    except:
        logger.error("Error in knn prediction",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in knn prediction',
                        'result' : {}
                    }
                ), 400)

def pre_dict_logistic(data):
    try:
        model = pickle.load(open('models/logistic.pkl', 'rb'))
        prediction=model.predict([data])
        return prediction
    except:
        logger.error("Error in logistic prediction",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in logistic prediction',
                        'result' : {}
                    }
                ), 400)

def pre_dict_random(data):
    try:
        model = pickle.load(open('models/random_forest.pkl', 'rb'))
        prediction=model.predict([data])
        return prediction
    except:
        logger.error("Error in random forest prediction",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in random forest prediction',
                        'result' : {}
                    }
                ), 400)

def pre_dict_svm(data):
    try:
        model = pickle.load(open('models/svm.pkl', 'rb'))
        prediction=model.predict([data])
        return prediction
    except:
        logger.error("Error in gaussian prediction",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in gaussian prediction',
                        'result' : {}
                    }
                ), 400)

@app.route('/get_data',methods = ["POST","GET"]) 
def get_data():
    logger.info('entered get_data')

    try:
        gender = request.form['gender']
        gender = int(encode['colname']['gender'][gender])
    except:
        logger.error("Error in getting --- gender --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- gender --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        SeniorCitizen = request.form['scn']
        SeniorCitizen = int(encode['colname']['SeniorCitizen'][SeniorCitizen])
    except:
        logger.error("Error in getting --- SeniorCitizen --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- SeniorCitizen --- and decoding',
                        'result' : {}
                    }
                ), 400)
   
    try:
        Partner = request.form['partner']
        Partner = int(encode['colname']['Partner'][Partner])
    except:
        logger.error("Error in getting --- Partner --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- Partner --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        Dependents = request.form['dependents']
        Dependents = int(encode['colname']['Dependents'][Dependents])
    except:
        logger.error("Error in getting --- Dependents --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- Dependents --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        PhoneService = request.form['ps']
        PhoneService = int(encode['colname']['PhoneService'][PhoneService])
    except:
        logger.error("Error in getting --- PhoneService --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- PhoneService --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        MultipleLines = request.form['ml']
        MultipleLines = int(encode['colname']['MultipleLines'][MultipleLines])
    except:
        logger.error("Error in getting --- MultipleLines --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- MultipleLines --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        InternetService = request.form['isp']
        InternetService = int(encode['colname']['InternetService'][InternetService])
    except:
        logger.error("Error in getting --- InternetService --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- InternetService --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        OnlineSecurity = request.form['os']
        OnlineSecurity = int(encode['colname']['OnlineSecurity'][OnlineSecurity])
    except:
        logger.error("Error in getting --- OnlineSecurity --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- OnlineSecurity --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        OnlineBackup = request.form['ob']
        OnlineBackup = int(encode['colname']['OnlineBackup'][OnlineBackup])
    except:
        logger.error("Error in getting --- OnlineBackup --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- OnlineBackup --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        DeviceProtection = request.form['dp']
        DeviceProtection = int(encode['colname']['DeviceProtection'][DeviceProtection])
    except:
        logger.error("Error in getting --- DeviceProtection --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- DeviceProtection --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        TechSupport = request.form['tss']
        TechSupport = int(encode['colname']['TechSupport'][TechSupport])
    except:
        logger.error("Error in getting --- TechSupport --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- TechSupport --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        StreamingTV = request.form['stt']
        StreamingTV = int(encode['colname']['StreamingTV'][StreamingTV])
    except:
        logger.error("Error in getting --- StreamingTV --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- StreamingTV --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        StreamingMovies = request.form['smm']
        StreamingMovies = int(encode['colname']['StreamingMovies'][StreamingMovies])
    except:
        logger.error("Error in getting --- StreamingMovies --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- StreamingMovies --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        Contract = request.form['contract']
        Contract = int(encode['colname']['Contract'][Contract])
    except:
        logger.error("Error in getting --- Contract --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- Contract --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        PaperlessBilling = request.form['pls']
        PaperlessBilling = int(encode['colname']['PaperlessBilling'][PaperlessBilling])
    except:
        logger.error("Error in getting --- PaperlessBilling --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- PaperlessBilling --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        PaymentMethod = request.form['PaymentMethod']
        PaymentMethod = int(encode['colname']['PaymentMethod'][PaymentMethod])
    except:
        logger.error("Error in getting --- PaymentMethod --- and decoding",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- PaymentMethod --- and decoding',
                        'result' : {}
                    }
                ), 400)
 
    try:
        tenure = int(request.form['Tenure'])
    except:
        logger.error("Error in getting --- tenure --- ",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- tenure --- ',
                        'result' : {}
                    }
                ), 400)
 
    try:
        MonthlyCharges = int(request.form['MonthlyCharges'])
    except:
        logger.error("Error in getting --- MonthlyCharges ---",exc_info=True)
        return make_response(jsonify(
                    {
                        'status' : 'fail',
                        'desc':'Error in getting --- MonthlyCharges ---',
                        'result' : {}
                    }
                ), 400)
 
    data = [gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity, OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges]
    

    
    kernal = pre_dict_kernal_svm(data)[0]

    dt = pre_dict_decisiontree(data)[0]
   
    gaus = pre_dict_gaussian(data)[0]
  
    knn = pre_dict_knn(data)[0]
  
    logistic = pre_dict_logistic(data)[0]
 
    random = pre_dict_random(data)[0]

    svm = pre_dict_svm(data)[0]
   
    all_res = [dt,kernal,gaus,knn,logistic,random,svm]
    
    
    final_result = mode(all_res)
   
    result = 'this customer will stay - not churn'
    if final_result == 1:
        result = 'this customer will leave - churn'

    return render_template('index.html',prediction_text= "{}".format(result))
 
