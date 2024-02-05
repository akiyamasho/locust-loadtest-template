# Locust Load Test Template

This is a quick template for creating load tests with Locust.
<img width="905" alt="スクリーンショット 2024-02-06 5 16 01" src="https://github.com/akiyamasho/locust-loadtest-template/assets/35907066/5e7d8cef-a6e1-4a1a-8bbd-9b18629b2d80">

### Table of Contents
- [Locust Load Test Template](#locust-load-test-template)
    - [Table of Contents](#table-of-contents)
    - [Requirements](#requirements)
    - [Setup](#setup)
    - [Development](#development)

### Requirements

Either of the following:
-  `docker` with `docker-compose`
-  `python3`

### Setup

1. Update the endpoints and parameters in [src/main.py](src/main.py) to the environment you'd like to test.
    
    NOTE: Sample GET and POST endpoints are provided in the file.

1. Run locust through the startup script
    1. With `docker-compose`:
        ```
        docker-compose up
        ```
    2. With `python` (this creates a virtualenv and installs the requirements): 
        ```
        ./start.sh
        ```
2. Access the Locust UI at http://localhost:8089
3. Use the host of your backend as the URL, and set the number of users and spawn rate to your desired load test.

### Development

This project uses the [Locust](https://locust.io/) library for load testing.

You can also install the dev dependencies for formatting and linting.

```
pip install -r requirements_dev.txt
```
