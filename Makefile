up:
	docker-compose up -d

down:
	docker-compose down

test:
	docker-compose up --abort-on-container-exit --build test
