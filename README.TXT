create reqs:
cd /path/to/python-docker
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install Flask
python3 -m pip freeze > requirements.txt
deactivate

create image:
# sudo docker build --build-arg BG_COLOR="pink" -t weatherapp-history .
#sudo docker run --name scootaloo -p 80:5000 weatherapp-history
# sudo docker run -e bg_color="teal" --name scootaloo -p 5000:5000 weatherapp-history
# sudo docker run -e bg_color="#d3d3d3" --name scootaloo -p 5000:5000 weatherapp-history
# sudo docker run -env bg_color='teal' --name scootaloo -p 5000:5000 weatherapp-history
docker build --build-arg BG_COLOR="purple" -t weatherapp-history .
docker run --name scootaloo -e "BG_COLOR=yellow" -p 5000:5000 weatherapp-history:latest

multi stage build:
sudo apt install docker-compose
docker-compose up
sudo docker-compose up
browser: http://0.0.0.0:8989/

run app for tests
export BG_COLOR="teal"
python3 app.py

push to dockerhub
echo <DOCKERHUB_PSW> | docker login -u <DOCKERHUB_USR> --password-stdin
docker tag weatherapp-history danielhabber/weatherapp-history:latest
docker push danielhabber/weatherapp-history:latest

security groups:
5000:webapp
22 SSH
80 HTTP

