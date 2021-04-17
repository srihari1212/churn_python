import pickle

#data=[0	,0 ,0 ,0, 2	, 1, 2, 1,0,2 ,0 ,0	 ,0 ,0 ,0, 	0, 2,79.55]
#data = [-1.007125	,-0.442347,	-0.962711,	-0.651004	,-1.025396,	0.327252,	-0.987361	,0.172842,	-0.924417,	-1.025734	,-1.026449,	-0.923452	,-1.109917,	-1.111487,	-0.822475,	0.832717,	1.330372	,0.177254]
#data = [-0.998227,-0.440625,1.041692,1.532835,-0.745692,0.326254,-1.210193,0.521902,-0.962027,-0.326254,1.167585,1.382072,-0.888655,-0.52353,1.010707,-0.52353,-0.639416,0.23]
#data = [0,	0,	1	,0,	1	,0,	1,	0	,0	,2,	0	,0	,0,	0	,0,	1	,2,	29.85] #churn-0
#data = [1,	0,	0	,0	,34	,1	,0	,0,	2,	0	,2,	0	,0,	0,	1	,0	,3	,56.95	] ##churn-0
#data = [1,	0	,0,	0	,2,	1,	0	,0	,2	,2,	0	,0	,0,	0	,0	,1,	3,	53.85] #churn-1
#data = [1	,0	,0,	1	,1,	1	,0,	2,	1	,1,	1,	1,	1	,1,	0,	0	,3	,19.25] #churn-1
#data = [1	,1	,0	,0,	14,	1,	0	,1,	0,	0	,0	,0,	2	,2	,0,	0,	1	,90.45] #churn-1
#data = [0.989758,	-0.442060,	-0.970958,	1.539356,	-1.272258	,0.325254,	-0.988525,	1.518468,	0.248207,	0.113846	,0.110161	,0.253050	,0.016678,	0.015472,	-0.824659,	-1.208858	,1.340123	,-1.502274]
#data = [0.989758,	2.262137,	-0.970958,	-0.649622	,-0.743916,	0.325254	,-0.988525,	0.166532,	-0.918098	,-1.025424,	-1.028644,	-0.914587	,1.148793,	1.147566,	-0.824659	,-1.208858,	-0.539686	,0.860985]

#data = [0,	0,	1,	0,	1,	0,	1	,0,	0	,2,	0	,0,	0,	0	,0	,1,	2	,29.85]	#0
#data = [1	,0	,0	,0	,34	,1	,0	,0	,2	,0	,2	,0	,0	,0	,1	,0	,3	,56.95]	#0	
#data = [1	,0	,0	,0	,2	,1	,0	,0	,2	,2	,0	,0	,0	,0	,0	,1	,3	,53.85]	#1	
#data = [1	,0	,0	,0	,45	,0	,1	,0	,2	,0	,2	,2	,0	,0	,1	,0	,0	,42.30]	#0	
#data = [0	,0	,0	,0	,2	,1	,0	,1	,0	,0	,0	,0	,0	,0	,0	,1	,2	,70.70]	#1	
data = [0, 0, 0, 0, 2, 0, 2, 2, 1, 0, 0, 2, 0, 0, 0, 0, 2, 12]
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
print(data)
print("decision tree",pre_dict_decisiontree(data))
print("gaussioan    ",pre_dict_gaussian(data))
print("k.svm        ",pre_dict_kernal_svm(data))
print("knn          ",pre_dict_knn(data))
print("logistic     ",pre_dict_logistic(data))
print("random forest",pre_dict_random(data))
print("svm          ",pre_dict_svm(data))