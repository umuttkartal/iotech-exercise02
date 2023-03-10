# IoTech coding assessment exercise 02

## Install the required packages

- pip install -r requirements.txt

## Running the program

To run the program, use the following command:

- python main.py

This will parse the data from exercise-02/data/data.json, discard the devices where the timestamp value is before the current time, get the total of all value entries, parse the uuid from the info field of each entry, and output the values total and the list of uuids in the format described by the JSON schema. The output will be written to the file named output.json in the folder exercise-02.

## Running the tests:

To run the tests, use the following command:

- python -m unittest test_02.py

This will discover and run all tests in the project.

## Docker

To build the image, navigate to the project directory and run:

- docker build -t "image-name" .

To run the container:

- docker run "image-name"

This will run the main program inside the container.

### docker-compose option for running the tests and the solution in the same container:

- docker-compose up

It will create a container with the image built from the current directory and run the command specified in the yml file.

You can also use docker-compose run command to run the test and script separately, for example:

- docker-compose run iotech02 python main.py
- docker-compose run iotech02 python -m unittest test_02.py
