apt-get install python-pip docker-engine daemontools daemontools-run
pip install -U butterfly
start svscan

cd docker
docker build -t demo .
