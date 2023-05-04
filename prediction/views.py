from django.shortcuts import render

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



def index(request):
	return render(request, "index.html")


def predict(request):
	return render(request, "predict.html")


def result(request):
	dataframe = pd.read_csv("collegePlace.csv")
	dataframe['Gender'].replace({'Male': 0,
								'Female': 1}, inplace=True)
	dataframe['Stream'].replace(
		{'Electronics And Communication': 0,
		'Computer Science': 1,
		'Information Technology': 2,
		'Mechanical': 3, 'Electrical': 4,
		'Civil': 5}, inplace=True)

	Y = dataframe["PlacedOrNot"]
	X = dataframe.drop(["PlacedOrNot"], axis=1)

	X_train, X_test, Y_train,Y_test = train_test_split(X, Y, test_size=0.1)

	model = LogisticRegression()
	model.fit(X_train, Y_train)

	val1 = float(request.GET['n1'])
	val2 = float(request.GET['n2'])
	val3 = float(request.GET['n3'])
	val4 = float(request.GET['n4'])
	val5 = float(request.GET['n5'])
	val6 = float(request.GET['n6'])
	val7 = float(request.GET['n7'])

	pred = model.predict([[val1, val2, val3,
						val4, val5, val6, val7]])

	result1 = ""
	if pred == [0]:
		result1 =0
	else:
		result1 =1

	return render(request, "resultat.html",{"result2": result1})

# Create your views here.
