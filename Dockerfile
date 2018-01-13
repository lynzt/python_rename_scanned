FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip3 install --upgrade -r requirements.txt

COPY . /usr/src/app

CMD [ "python3", "./rename_pics.py" ]
