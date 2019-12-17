# docker-flask-api

Docker running a flask api

Clone repo and build container locally:
```sh
git clone https://github.com/dalijolijo/docker-flask-api.git
cd docker-flask-api
docker build -t flask-api .
```

To run (at port `8080`):
```sh
docker run -d --rm -p 8080:8080 -v /root/docker-flask-api/app/:/app --name api flask-api
```

Test API with curl:
```sh
curl http://127.0.0.1:8080
{
    "about": "Hello World!"
}

curl http://127.0.0.1:8080/multi/22
{
    "result": 220
}

curl -H "Content-Type: application/json" -X POST -d '{"name":"LIMXTEX","link":"https://limxtec.org"}' http://127.0.0.1:8080
{
    "you sent": {
        "link": "https://limxtec.org",
        "name": "LIMXTEX"
    }
}
```

