run-server:
	flask --app app run --port 5050

unit-test:
	python3 -m unittest discover -p "*_test.py" -v
