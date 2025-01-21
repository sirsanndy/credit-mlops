FROM python:3.12.3-slim
WORKDIR /home
COPY ./requirements.txt ./
COPY ./ui.py ./ui.py
RUN \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    pip install --upgrade pip && \
    pip install wheel && \
    pip install -r requirements.txt
EXPOSE 8051
CMD ["streamlit run --server.port=8051", "ui.py"]