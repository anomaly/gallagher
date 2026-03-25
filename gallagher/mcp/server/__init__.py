""" MCP server for Gallagher access control systems
"""

import os
import tempfile
import random


from mcp.server.fastmcp import FastMCP
from gallagher.cc import APIClient, CommandCentreConfig

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
temp_file_tls_key = tempfile.NamedTemporaryFile(
    suffix=".key",
    delete=False
)

# Write the certificate and private key to temporary files
if not certificate_anomaly is None and not temp_file_certificate is None:
    temp_file_certificate.write(certificate_anomaly.encode('utf-8'))

if not private_key_anomaly is None and not temp_file_tls_key is None:
    temp_file_tls_key.write(private_key_anomaly.encode('utf-8'))

# Read the two files to ensure they are written
temp_file_certificate.flush()
temp_file_tls_key.flush()

# Since supporting Basic authentication #65, randomly choose
# between Basic and API Key authentication for tests
config = CommandCentreConfig(
    api_key=api_key,
    file_tls_key=temp_file_tls_key.name,
    file_tls_certificate=temp_file_certificate.name,
    use_basic_authentication=random.choice([True, False]),
)

api_client = APIClient(config=config)

mcp = FastMCP(name="gallagher")

# Add your tools here, for example:
@mcp.tool()
async def list_divisions():
    """List all divisions in the Command Centre"""
    # Implementation here
    divisions = await api_client.divisions.list()
    return divisions

@mcp.tool()
async def search_cardholders(name: str):
    """Search for cardholders by name in the Command Centre"""
    # Implementation here
    cardholders = await api_client.cardholders.search(name=name)
    return cardholders

@mcp.tool()
async def list_all_cardholders():
    """List all cardholders in the Command Centre"""
    # Implementation here
    cardholders = await api_client.cardholders.list()
    return cardholders
