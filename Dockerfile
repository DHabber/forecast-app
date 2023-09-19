FROM python:3.10.6-alpine
ARG BG_COLOR
ENV BG_COLOR=$BG_COLOR


RUN mkdir /app
WORKDIR /app

COPY . .
RUN mkdir history

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
RUN rm requirements.txt

EXPOSE 5000
CMD export BG_COLOR=$BG_COLOR && gunicorn --bind 0.0.0.0:5000 app:app
