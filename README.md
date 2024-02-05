# Locust Load Test Template

This is a quick template for creating GET/POST load tests with Locust.

### Table of Contents
- [Locust Load Test Template](#locust-load-test-template)
    - [Table of Contents](#table-of-contents)
    - [Setup with Docker](#setup-with-docker)
        - [Requirements](#requirements)
        - [Setup](#setup)
    - [Setup with Python](#setup-with-python)
        - [Requirements](#requirements-1)
        - [Setup](#setup-1)
    - [Running the Load Test](#running-the-load-test)
    - [Development](#development)

### Setup with Docker

##### Requirements

-   `Docker`

##### Setup

1. Update the endpoints and parameters in [src/main.py](src/main.py) to the environment you'd like to test.

    NOTE: Sample GET and POST endpoints are provided in 
    the file.

2. Run locust through Docker

    ```
    docker-compose up
    ```

### Setup with Python

You can also

##### Requirements

-   `python`

##### Setup

1. Update the endpoints and parameters in [src/main.py](src/main.py) to the environment you'd like to test.
NOTE: Sample GET and POST endpoints are provided in the file.

1. Run locust through the startup script. This creates a virtual environment and installs the required packages.
    ```
    ./start.sh
    ```

### Running the Load Test

After running locust with your desired runtime, you can access the Locust UI to start the load test.

1. Access the Locust UI at http://localhost:8089

1. Use the host of your backend as the URL, and set the number of users and spawn rate to your desired load test.

### Development

This project uses the [Locust](https://locust.io/) library for load testing.

You can also install the dev dependencies for formatting and linting.

```
pip install -r requirements-dev.txt
```