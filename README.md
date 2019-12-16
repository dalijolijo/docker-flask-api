# docker-flask-api

Docker running a flask api

To run (at port `8080`):

    git clone https://github.com/dalijolijo/docker-flask-api.git
    cd docker-flask-api
    docker build -t flask-api . 
    docker run -d --rm -p 8080:8080 -v /root/docker-flask-api/app/:/app --name api flask-api
