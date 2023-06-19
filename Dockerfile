FROM python:3.9

WORKDIR /src

COPY requirements.txt .

CMD ["python", "install_requirements.py"]

# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run.py"]
