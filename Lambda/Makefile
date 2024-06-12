SERVICE=EC2Lambda

build:
	sam build -m requirements.txt --use-container

run:
	sam local invoke "$(SERVICE)" -e ./events/sample.json

zip:
	./zip.sh $(SERVICE)

clean:
	rm -rf .aws-sam