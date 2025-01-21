import utils as utils
import preprocessing as preprocessing
import pandas as pd
from fastapi import FastAPI
import pydantic
import mlflow
import uvicorn
import dotenv


app = FastAPI()

ohe_loan_grade = utils.deserialize_data("models/ohe_loan_grade.pkl")
ohe_loan_intent = utils.deserialize_data("models/ohe_loan_intent.pkl")
ohe_home_ownership = utils.deserialize_data("models/ohe_home_ownership.pkl")
ohe_default_on_file = utils.deserialize_data("models/ohe_default_on_file.pkl")

class Item(pydantic.BaseModel):
    person_age: int
    person_income: int
    person_home_ownership: str
    person_emp_length: int
    loan_intent: str
    loan_amnt: int
    loan_int_rate: float
    loan_grade: str
    loan_percent_income: float
    cb_person_default_on_file: str
    cb_person_cred_hist_length: int


@app.post("/predict") 
def predict(item: Item): 
    dotenv.load_dotenv(".env")
    mlflow.set_tracking_uri(uri = "http://13.250.109.123:5000")
    model = mlflow.sklearn.load_model("models:/RandomForestClassifier@rfc")
    
    # Convert input data to pandas DataFrame 
    data = pd.DataFrame({
        'person_age': [item.person_age],
        'person_income': [item.person_income],
        'person_home_ownership': [item.person_home_ownership],
        'person_emp_length': [item.person_emp_length],
        'loan_intent': [item.loan_intent],
        'loan_grade': [item.loan_grade],
        'loan_amnt': [item.loan_amnt],
        'loan_int_rate': [item.loan_int_rate],
        'loan_percent_income': [item.loan_percent_income],
        'cb_person_default_on_file': [item.cb_person_default_on_file],
        'cb_person_cred_hist_length': [item.cb_person_cred_hist_length]
    }) 
    # Perform preprocessing 
    data = preprocessing.ohe_transform(data, "person_home_ownership", "home_ownership", ohe_home_ownership)
    data = preprocessing.ohe_transform(data, "loan_intent", "loan_intent", ohe_loan_intent)
    data = preprocessing.ohe_transform(data, "loan_grade", "loan_grade", ohe_loan_grade)
    data = preprocessing.ohe_transform(data, "cb_person_default_on_file", "default_onfile", ohe_default_on_file)
    probabilities = model.predict_proba(data)[:, 1]
    threshold = 0.5 
    # replace with your best threshold value 
    prediction = (probabilities >= threshold).astype(int) 
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)