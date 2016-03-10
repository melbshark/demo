apt-get install python-pip docker-engine daemontools daemontools-run
pip install -U butterfly
start svscan
crontab /root/crontab
cd /root/docker
docker build -t demo .
