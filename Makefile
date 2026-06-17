run-server:
	flask --app app run --port 5050 --debug

unit-test:
	pytest -v
