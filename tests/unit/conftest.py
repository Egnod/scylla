import pytest

from scylla import Client


@pytest.fixture(scope="module")
def test_client():
    client = Client(client=True)

    client._username = client._password = "123"

    return client
