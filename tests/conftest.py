import pytest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from inquestlabs import inquestlabs_api
import requests_mock
import requests

@pytest.fixture(scope="module")
def labs():
    return inquestlabs_api()


@pytest.fixture(scope="module")
def labs_with_key():
    return inquestlabs_api(api_key="mock")

