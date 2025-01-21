FROM python:3.12.3-slim
WORKDIR /home
COPY ./requirements.txt ./
COPY ./api.py ./api.py
COPY ./src/utils.py ./utils.py
COPY ./src/preprocessing.py ./preprocessing.py
COPY ./models/ohe_default_on_file.pkl ./models/ohe_default_on_file.pkl
COPY ./models/ohe_home_ownership.pkl ./models/ohe_home_ownership.pkl
COPY ./models/ohe_loan_grade.pkl ./models/ohe_loan_grade.pkl
COPY ./models/ohe_loan_intent.pkl ./models/ohe_loan_intent.pkl
RUN \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    pip install --upgrade pip && \
    pip install wheel && \
    pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "api.py"]