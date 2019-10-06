import json

from pytest_httpserver.httpserver import Request, Response


def auth(request: Request):
    request = json.loads(request.data)

    if "password" in request and "username" in request:
        response = {"access_token": "123"}

        return json.dumps(response)

    else:
        response = {"description": "Invalid credentials", "error": "Bad Request", "status_code": "401"}

        return Response(response=json.dumps(response), status=401, content_type="application/json")


def test_get_token(httpserver, test_client):
    httpserver.expect_request("/auth", method="POST").respond_with_handler(auth)

    test_client._endpoint = f"http://{httpserver.host}:{httpserver.port}"
    test_client._auth_path = "/auth"

    assert test_client._get_token() == "123"
