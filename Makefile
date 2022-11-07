install:
	pip install -r requirements.txt

start:
	python snake

format:
	black .

push: format
	git add .
	git commit -m "$(MSG)"
	git push
