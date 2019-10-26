from suds.client import Client as SudsClient
from python_globalsign.exceptions import (
    GlobalSignError, GlobalSignDomainMissing, GlobalSignWsdlPathMissing
    )


class Client:
    def __init__(self, globalsign_domain, globalsign_wsdl_path):
        self._globalsign_domain = globalsign_domain
        self._globalsign_wsdl_path = globalsign_wsdl_path
        self._globalsign_url = self._construct_globalsign_url()

    def _construct_globalsign_url(self):
        """Constructs the GlobalSign URL for accessing the SOAP api.

        Takes the object's `globalsign_domain' and `globalsign_wdsl_path'
        variables and constructs a valid Url for interacting with GlobalSign's
        SOAP api.
            url = f'http://{globalsign_domain}/{globalsign_wsdl_path}'

        Returns:
            String :: Formated GlobalSign Url with Wdsl path
        """
        globalsign_domain = self.get_globalsign_domain()
        globalsign_wsdl_path = self.get_globalsign_wsdl_path()
        return f'http://{globalsign_domain}/{globalsign_wsdl_path}'

    def get_globalsign_domain(self):
        """Get the object's current GlobalSign domain for the SOAP api.

        Returns:
            String :: Objects current value for `globalsign_domain'

        Exception:
            GlobalSignDomainMissing :: Raises when
                                       `self._globalsign_domain' is None
        """
        if self._globalsign_domain:
            # Validating the string to ensure it's a domain would not be a bad
            # idea.
            return self._globalsign_domain
        raise GlobalSignDomainMissing

    def get_globalsign_wsdl_path(self):
        """Get the object's current GlobalSign Wsdl endpoint.

        Returns:
            String :: Objects current value for `globalsign_wsdl_path'

        Exception:
            GlobalSignWsdlPathMissing :: Raises when
                                         `self._globalsign_wsdl_path' is None
        """
        if self._globalsign_wsdl_path:
            return self._globalsign_wsdl_path
        raise GlobalSignWsdlPathMissing
