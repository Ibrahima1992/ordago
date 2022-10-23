start:
	docker-compose up -d

stop:
	docker-compose stop

restart:
	docker-compose restart

load_data:
	python3 api/routes/load_data.py
