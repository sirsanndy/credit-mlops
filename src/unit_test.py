import mlflow
def test_model_availability():
    mlflow.set_tracking_uri(uri = "http://13.250.109.123:5000")
    model = mlflow.sklearn.load_model("models:/RandomForestClassifier@rfc")
    assert type(model) == mlflow.sklearn.load_model("models:/RandomForestClassifier@rfc")