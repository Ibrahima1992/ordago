start:
	docker-compose up -d

stop:
	docker-compose stop

restart:
	docker-compose restart
status:
	docker-compose ps

load_data:
	pip install pandas; pip install psycopg2-binary; python3 api/routes/load_data.py

api_auto:
	docker exec -it ordago_api bash

bdd:
	docker exec -it ordago_bdd bash