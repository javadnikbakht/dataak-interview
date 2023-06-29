# dataak-interview

* Setup kafka
```sh
docker-compose -f zk-kafka-single.yml up -d
```

* Setup elastic and kibana
```sh
docker-compose -f elastic-kibana-single.yml up -d
```

* Python Virtualenv and Install requiements
```sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

* Running Producer
```sh
celery -A producer.app worker --beat --loglevel=info --scheduler=cron -s /app/celerybeat-schedule"
```

* Running Consumer
```sh
python consumer.py
```

* Running Flask app
```sh
python main.py
```

* Some curl sample for flask webservice
 - Search 
 ```sh
 curl -X GET 'http://localhost:5000/search?query={"text":"Hi"}'
 ```
 - Tag
 ```sh
 curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "doc_id": "q8FBDokBeVjFa6NEfDUi",
    "tags": ["1", "2", "3"]
  }' \
  http://localhost:5000/tag
 ```