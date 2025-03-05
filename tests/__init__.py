""" Gallagher Python idiomatic client library test

  Test suite for the Gallagher Python idiomatic client library,
  using pytest run via Taskfile.

  The pytest.mark.asyncio marker can be omitted entirely in auto mode 
  where the asyncio marker is added automatically to async test functions.
  
  Refer to pytest.ini for configuration
  https://pytest-asyncio.readthedocs.io/en/latest/reference/markers/index.html

  TODO: check if setup and teardown can be turned into async

"""
import tempfile


def setup_module(module):
    """The Gallagher API client requires a test key, this is
    set in the environment variable GACC_API_KEY.

    For obvious security reasons never store or version a key
    in the source.
    """
    import os

    api_key = os.environ.get("GACC_API_KEY")

    # Read these from the environment variables, if they exists
    # they will be written to temporary files
    certificate_anomaly = os.environ.get("CERTIFICATE_ANOMALY")
    private_key_anomaly = os.environ.get("PRIVATE_KEY_ANOMALY")

    # Write the certificate_anomaly and private_key_anomaly to files
    # if they exist
    if certificate_anomaly:
        with open('certificate.pem', 'w') as f:
            f.write(certificate_anomaly)

    if private_key_anomaly:
        with open('private_key.pem', 'w') as f:
            f.write(private_key_anomaly)

    # Create temporary files to store the certificate and private key
    # temp_file_certificate = tempfile.NamedTemporaryFile(
    #   suffix=".crt",
    #   delete=False
    # )
    # temp_file_private_key = tempfile.NamedTemporaryFile(
    #   suffix=".key",
    #   delete=False
    # )

    # Write the certificate and private key to temporary files
    # if certificate_anomaly and temp_file_certificate:
    #   temp_file_certificate.write(certificate_anomaly.encode('utf-8'))

    # if private_key_anomaly and temp_file_private_key:
    #   temp_file_private_key.write(private_key_anomaly.encode('utf-8'))

    from gallagher import cc

    cc.api_key = api_key
    # cc.file_tls_certificate = temp_file_certificate.name
    # cc.file_private_key = temp_file_private_key.name
    cc.file_tls_certificate = 'certificate.pem'
    cc.file_private_key = 'private_key.pem'


def teardown_module(module):
    """When we are done running the tests return the API client
    to it's default state.

    This ensures that anything that runs past this point is not
    accessing the server
    """
    from gallagher import cc

    cc.api_key = None
