class Error(Exception):
    """Base class for exceptions

    Attributes:
        message -- explanation of the error
    """

    def __init__(self,
                 message="Python-GlobalSign has experienced an unexpected error"
                 ):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.message = message


class GlobalSignError(Error):
    """Base class for handling exceptions for GlobalSign"""
    def __init__(self,
                 message="GlobalSign has experienced an error"
                 ):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.message = message


class GlobalSignDomainMissing(Error):
    """Handle exception for missing Globalsign Domain"""
    def __init__(self):
        # Call the base class constructor with the parameters it needs
        self.message = "GlobalSign: Missing GlobalSign's SOAP domain"
        super().__init__(self.message)


class GlobalSignWsdlPathMissing(Error):
    """Handle exception for missing Globalsign Wsdl Url path"""
    def __init__(self):
        # Call the base class constructor with the parameters it needs
        self.message = "GlobalSign: Missing GlobalSign's Wsdl Url Path"
        super().__init__(self.message)
