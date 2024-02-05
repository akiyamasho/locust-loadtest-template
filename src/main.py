import requests
from locust import HttpUser, task

# TODO: replace this with your endpoint
ENDPOINT_GET = "/get_endpoint"
ENDPOINT_GET_WEIGHT = 1
ENDPOINT_GET_PARAMS = {
    "param_key1": "param_value1",
    "param_key2": "param_value2",
}

# TODO: replace this with your endpoint
ENDPOINT_POST = "/post_endpoint"
ENDPOINT_POST_WEIGHT = 1
ENDPOINT_POST_PARAMS = {
    "param_key1": "param_value1",
    "param_key2": "param_value2",
}


class LoadTest(HttpUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @task(ENDPOINT_GET_WEIGHT)
    def get_endpoint(self):
        self.client.get(
            ENDPOINT_GET,
            params=ENDPOINT_GET_PARAMS,
            # headers=ENDPOINT_GET_AUTH_HEADERS
            # TODO: you can also add auth headers here if needed
        ).json()

    @task(ENDPOINT_POST_WEIGHT)
    def post_status_text_only(self):
        try:
            response = self.client.post(
                ENDPOINT_POST,
                data=ENDPOINT_POST_PARAMS,
                # headers=ENDPOINT_POST_AUTH_HEADERS
                # TODO: you can also add auth headers here if needed
            )
            response.raise_for_status()
            response_json = response.json()
            print(response_json)
        except requests.exceptions.RequestException as e:
            print(f"Error sending POST {ENDPOINT_POST} request: {e}")
