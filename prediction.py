import joblib
def predict(data):
	model = joblib.load("model.pkl")
	return model.predict(data)