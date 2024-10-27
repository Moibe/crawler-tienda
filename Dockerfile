FROM python:3.9

WORKDIR /crawler

COPY ./requirements.txt /crawler/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /crawler/requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]