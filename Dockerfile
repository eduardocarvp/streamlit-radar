FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY /app .

EXPOSE 8501

ENV PYTHONPATH="$PYTHONPATH:/app"

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]