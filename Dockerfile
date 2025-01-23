FROM python:3.8-slim-buster

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

COPY . .
EXPOSE 5000 

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "gunicorn", "--bind" , "0.0.0.0:80", "run:app", "--host=0.0.0.0"]