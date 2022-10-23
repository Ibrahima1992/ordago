clone:
	git clone git@github.com:Ibrahima1992/ordago.git && cd ordago

start:
	docker-compose up -d

stop:
	docker-compose stop

restart:
	docker-compose restart

add_data:
	python3 api/routes/automobile.py