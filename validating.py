import pickle
from data import  encode
from flask import Flask, render_template, request
#from test_list import pre_dict_decisiontree,pre_dict_gaussian,pre_dict_kernal_svm,pre_dict_knn,pre_dict_logistic,pre_dict_random,pre_dict_svm
import statistics
from statistics import mode

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

def pre_dict_decisiontree(data):
    model = pickle.load(open('models/decision_tree.pkl', 'rb'))
    prediction=model.predict([data])
    return prediction

def pre_dict_gaussian(data):
    model = pickle.load(open('models/gaussian.pkl', 'rb'))
    prediction=model.predict([data])
    return prediction

def pre_dict_kernal_svm(data):
    model = pickle.load(open('models/kernal_svm.pkl', 'rb'))
    prediction=model.predict([data])
    return prediction

def pre_dict_knn(data):
    model = pickle.load(open('models/knn.pkl', 'rb'))
    prediction=model.predict([data])
    return prediction

def pre_dict_logistic(data):
    model = pickle.load(open('models/logistic.pkl', 'rb'))
    prediction=model.predict([data])
    return prediction

def pre_dict_random(data):
    model = pickle.load(open('models/random_forest.pkl', 'rb'))
    prediction=model.predict([data])
    return prediction

def pre_dict_svm(data):
    model = pickle.load(open('models/svm.pkl', 'rb'))
    prediction=model.predict([data])
    return prediction

@app.route('/get_data',methods = ["POST","GET"]) 
def get_data():
    gender = request.form['gender']
    gender = int(encode['colname']['gender'][gender])
    print('gender',gender)
    SeniorCitizen = request.form['scn']
    SeniorCitizen = int(encode['colname']['SeniorCitizen'][SeniorCitizen])
    print('SeniorCitizen ',SeniorCitizen)
    Partner = request.form['partner']
    Partner = int(encode['colname']['Partner'][Partner])
    print('Partner ',Partner)
    Dependents = request.form['dependents']
    Dependents = int(encode['colname']['Dependents'][Dependents])
    print('Dependents ',Dependents)
    PhoneService = request.form['ps']
    PhoneService = int(encode['colname']['PhoneService'][PhoneService])
    print('PhoneService ',PhoneService)
    MultipleLines = request.form['ml']
    MultipleLines = int(encode['colname']['MultipleLines'][MultipleLines])
    print('MultipleLines ',MultipleLines)
    InternetService = request.form['isp']
    InternetService = int(encode['colname']['InternetService'][InternetService])
    print('InternetService ',InternetService)
    OnlineSecurity = request.form['os']
    OnlineSecurity = int(encode['colname']['OnlineSecurity'][OnlineSecurity])
    print('OnlineSecurity ',OnlineSecurity)
    OnlineBackup = request.form['ob']
    OnlineBackup = int(encode['colname']['OnlineBackup'][OnlineBackup])
    print('OnlineBackup ',OnlineBackup)
    DeviceProtection = request.form['dp']
    DeviceProtection = int(encode['colname']['DeviceProtection'][DeviceProtection])
    print('DeviceProtection ',DeviceProtection)
    TechSupport = request.form['tss']
    TechSupport = int(encode['colname']['TechSupport'][TechSupport])
    print('TechSupport ',TechSupport)
    StreamingTV = request.form['stt']
    StreamingTV = int(encode['colname']['StreamingTV'][StreamingTV])
    print('StreamingTV ',StreamingTV)
    StreamingMovies = request.form['smm']
    StreamingMovies = int(encode['colname']['StreamingMovies'][StreamingMovies])
    print('StreamingMovies ',StreamingMovies)
    Contract = request.form['contract']
    Contract = int(encode['colname']['Contract'][Contract])
    print('Contract ',Contract)
    PaperlessBilling = request.form['pls']
    PaperlessBilling = int(encode['colname']['PaperlessBilling'][PaperlessBilling])
    print('PaperlessBilling ',PaperlessBilling)
    PaymentMethod = request.form['PaymentMethod']
    PaymentMethod = int(encode['colname']['PaymentMethod'][PaymentMethod])
    print('PaymentMethod ',PaymentMethod)
    tenure = int(request.form['Tenure'])
    print('tenure ',tenure)
    MonthlyCharges = int(request.form['MonthlyCharges'])
    print('MonthlyCharges ',MonthlyCharges)
    #data=[0	,0	            ,0	    ,0	,         2	,     1	,               2	,            1	           ,0	            ,2              	,0	            ,0	        ,0	        ,0	            ,0,     	0,                  	2	    ,79.55]

    data = [gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity, OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges]
    
#   gender	SeniorCitizen	Partner	Dependents	tenure	PhoneService	MultipleLines	InternetService	OnlineSecurity	OnlineBackup	DeviceProtection	TechSupport	StreamingTV	StreamingMovies	Contract	PaperlessBilling	PaymentMethod	MonthlyCharges
    print(type(data))
    kernal = pre_dict_kernal_svm(data)[0]
    print("ker",kernal)
    dt = pre_dict_decisiontree(data)[0]
    print(dt)
    gaus = pre_dict_gaussian(data)[0]
    print(gaus)
    knn = pre_dict_knn(data)[0]
    print(knn)
    logistic = pre_dict_logistic(data)[0]
    print(logistic)
    random = pre_dict_random(data)[0]
    print(random)
    svm = pre_dict_svm(data)[0]
    print(svm)
    all_res = [dt,kernal,gaus,knn,logistic,random,svm]
    print(all_res)
    final_result = mode(all_res)
    print(final_result)
    
    # res = pre_dict(data)
    # print(res)
    result = 'this customer will stay - not churn'
    if final_result == 1:
        result = 'this customer will leave - churn'

    return render_template('index.html',prediction_text= "{}".format(result))
 


#    gender	SeniorCitizen	Partner	Dependents	tenure	PhoneService	MultipleLines	InternetService	OnlineSecurity	OnlineBackup	DeviceProtection	TechSupport	StreamingTV	StreamingMovies	Contract	PaperlessBilling	PaymentMethod	MonthlyCharges
#data=[0	,0	            ,0	    ,0	,         2	,     1	,               2	,            1	           ,0	            ,2              	,0	            ,0	        ,0	        ,0	            ,0,     	0,                  	2	    ,79.55]

#-1.009990	-0.438325	-0.958953	-0.649346	-1.228662	0.331226	1.113063	0.179412	-0.914152	1.255274	-1.026900	-0.918308	-1.109686	-1.123124	-0.815525	-1.208413	0.392229	0.492176
# data = [-1.007125,
# -0.442347	,
# 1.038733	,
# 1.536089	,
# -1.106970	,
# 0.327252	,
# -0.987361	,
# 0.172842	,
# -0.924417	,
# 1.249457	,
# -1.026449	,
# -0.923452	,
# -1.109917	,
# 1.150022	,
# -0.822475	,
# 0.832717	,
# 0.392168	,
# 0.632515]

def pre_dict(data):
    model = pickle.load(open('logistic_churn.pkl', 'rb'))
    prediction=model.predict([data])
    return prediction


if __name__=="__main__":
    app.run(debug=True)
