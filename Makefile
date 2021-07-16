up:
	docker-compose up -d client

down:
	docker-compose down client

test:
	docker-compose up --abort-on-container-exit --build test
