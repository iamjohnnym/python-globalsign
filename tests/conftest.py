import os
import pytest


@pytest.fixture
def globalsign_url():
    return {
        'globalsign_domain': os.environ.get(
            'TEST_GLOBALSIGN_DOMAIN', 'test-gcc.globalsign.com'
            ),
        'globalsign_wsdl_path': os.environ.get(
            'TEST_GLOBALSIGN_WSDL_PATH', 'set-me-as-an-env-var')
        }


@pytest.fixture
def credentials():
    return {
        'globalsign_username': os.environ.get('TEST_GLOBALSIGN_USERNAME'),
        'globalsign_password': os.environ.get('TEST_GLOBALSIGN_PASSWORD')
        }


@pytest.fixture
def globalsign_client(globalsign_url):
    from python_globalsign.client import Client
    return Client(
        **globalsign_url
        )
