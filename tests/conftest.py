""" Gallagher Python idiomatic client library test

  As of gallagher/#96 the API client is not initialised in
  setup_module but is a fixture that is passed to tests.

  See also the decision to turn the __init__ to a sync method
  the other async methods are awaited as needed.

"""
import os
import tempfile

import pytest

from gallagher.cc.core import CommandCentreConfig
from gallagher.cc import APIClient

@pytest.fixture(scope="function")
async def api_client():
    """The Gallagher API client requires a test key, this is
    set in the environment variable GACC_API_KEY.

    For obvious security reasons never store or version a key
    in the source.
    """

    api_key = os.environ.get("GACC_API_KEY")

    # Read these from the environment variables, if they exists
    # they will be written to temporary files
    certificate_anomaly = os.environ.get("CERTIFICATE_ANOMALY")
    private_key_anomaly = os.environ.get("PRIVATE_KEY_ANOMALY")

    # Create temporary files to store the certificate and private key
    temp_file_certificate = tempfile.NamedTemporaryFile(
      suffix=".crt",
      delete=False
    )
    temp_file_private_key = tempfile.NamedTemporaryFile(
      suffix=".key",
      delete=False
    )

    # Write the certificate and private key to temporary files
    if not certificate_anomaly is None and not temp_file_certificate is None:
      temp_file_certificate.write(certificate_anomaly.encode('utf-8'))

    if not private_key_anomaly is None and not temp_file_private_key is None:
      temp_file_private_key.write(private_key_anomaly.encode('utf-8'))

    # Read the two files to ensure they are written
    temp_file_certificate.flush()
    temp_file_private_key.flush()

    config = CommandCentreConfig(
        api_key=api_key,
        file_private_key=temp_file_private_key.name,
        file_tls_certificate=temp_file_certificate.name,
    )
    api_client = APIClient(config=config)

    yield api_client

    # Cleanup temporary files
    if temp_file_certificate:
      os.unlink(temp_file_certificate.name)

    if temp_file_private_key:
      os.unlink(temp_file_private_key.name)
