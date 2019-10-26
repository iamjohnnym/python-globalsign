import pytest
import unittest

from python_globalsign.client import Client
from python_globalsign.exceptions import (
    GlobalSignDomainMissing, GlobalSignWsdlPathMissing
    )


class TestClient:
    def test_client_init(self, globalsign_url):
        client = Client(
            globalsign_domain=globalsign_url['globalsign_domain'],
            globalsign_wsdl_path=globalsign_url['globalsign_wsdl_path']
            )
        assert client

    def test_globalsign_domain(self, globalsign_client):
        globalsign_client.get_globalsign_domain()

    def test_globalsign_domain_raises_missing(self, globalsign_client):
        setattr(globalsign_client, '_globalsign_domain', '')
        with pytest.raises(GlobalSignDomainMissing):
            globalsign_client.get_globalsign_domain()

    def test_globalsign_wsdl_path(self, globalsign_client):
        assert globalsign_client.get_globalsign_wsdl_path()

    def test_globalsign_wsdl_path_raises_missing(self, globalsign_client):
        setattr(globalsign_client, '_globalsign_wsdl_path', '')
        with pytest.raises(GlobalSignWsdlPathMissing):
            globalsign_client.get_globalsign_wsdl_path()
