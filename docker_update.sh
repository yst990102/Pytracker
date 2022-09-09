# update pytracker:latest in docker repo
docker image build -t pytracker .
docker tag pytracker:latest yst990102/pytracker
docker push yst990102/pytracker