SERVICE=EC2Lambda

.ec2-lambda:
	pip install virtualenv && \
	virtualenv .ec2-lambda && \
	. .ec2-lambda/bin/activate && \
	pip install -r requirements-test.txt

black: .ec2-lambda
	. .ec2-lambda/bin/activate && \
	black src/ tests/

build:
	sam build -m requirements.txt --use-container

test: .ec2-lambda
	. .ec2-lambda/bin/activate && \
	black --check src/ tests/ && \
	pytest ./tests

run:
	sam local invoke "$(SERVICE)" -e ./events/sample.json

zip:
	./zip.sh $(SERVICE)

clean:
	rm -rf .aws-sam