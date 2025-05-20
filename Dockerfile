# docker-oos python-ii 3.11-slim version tatax
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
# flask gedeg container vvsgex
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]