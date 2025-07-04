# Installation & Usage

What you need to install will widely depend on if you are looking to use our tools, building software with our libraries or contributing to the project. This guide will get you set up for each one of the use cases. While the end user tools do not require software development experience, the other development tools are biased towards Python developers.

## Requirements

You will require Python 3.10 or above to run the SDK and tools. We provide containerised versions and binaries for most popular platforms. Please keep reading for specific instructions.

## Installation

In the most trivial cases we recommend installation via `PyPI`. The package is designed such that you only install what you need. The SDK is required by all our tools, hence it's the lowest common denominator.

The SDK can be installed by adding it as a dependency to your project:

```bash
uv add gallagher
```

If you are feeling adventurous you can install everything by:

```bash
uv add gallagher[all]
```

### SDK

To use the API (or the associated tools, as they use the API client in return) you must have an API key supplied by the Command Centre instance. The same key is used if you were were using the API on premise or in the cloud.

You would typically read the API key from an environment variable or a secrets manager, depending on your setup.

You should only ever setup the API key once in your application instance. The rest of the client is designed to discover. An example of how you would do this would look like:

```python
from gallagher import cc
api_key = os.environ.get("GACC_API_KEY")
cc.api_key = api_key
```

following this you can call any of the SDK methods and the client will performance the necessary discovery and authentication. If you fail to set the API key, the client will raise the following exceptions:

- `NoAPIKeyProvidedError` - If the API key is not set.
- `ValueError` - If the API key does not conform to the expected format (which looks like eight tokens separated by `-`).

#### Using TLS certificates

Command Centre optionally allows you to use self signed client side TLS certificates for authentication. You can use this along side your API key as an additional layer of security.

You can use `openssl` to generate yourself a client side certificate and key.

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout client.key -out client.pem
```

Fill in the required details for the certificate and then generate a `sha1` hash of the certificate.

```bash
openssl x509 -in client.pem -noout -fingerprint -sha1
```

> Note that the Command Centre does not use the `colon` separated format, see their documentation for more information.

Once you have completed these steps all you have to do is provide the path to the certificate and key files to the client.

```python
from gallagher import cc
api_key = os.environ.get("GACC_API_KEY")
cc.api_key = api_key

cc.file_tls_certificate = '/path/to/client.pem'
cc.file_private_key = '/path/to/client.key'
```

The rest of the requests and operations remain the same, the library will use an `SSL Context` to do the needful.

> Our testsuites are configured to run with and without TLS certificates to ensure that we support both modes of operation.

In instances (such as Github actions, where we store the certificate and key in the Github secrets manager) where you can't store the certificate and key in the filesystem, you can use Python's `tempfile` module to create temporary files and clean up once you are done using them.

```python
import tempfile

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
if certificate_anomaly and temp_file_certificate:
    temp_file_certificate.write(certificate_anomaly.encode('utf-8'))

if private_key_anomaly and temp_file_private_key:
    temp_file_private_key.write(private_key_anomaly.encode('utf-8'))
```

You can assign these temporary files to the client as shown above.

```python
from gallagher import cc

cc.api_key = api_key
cc.file_tls_certificate = temp_file_certificate.name
cc.file_private_key = temp_file_private_key.name
```

### Command line interface

### Terminal user interface

### SQL support

## Developer notes

This library uses [httpx](https://www.python-httpx.org) as the HTTP transport and [pydantic](https://pydantic.dev) to construct and ingest payloads. We use [taskfile](https://taskfile.dev) to run tasks. Our test suite is setup using `pytest`.

Anomaly has a demo Command Centre set up in the cloud that we run tests against. This is populate using a sample site configuration. There are no real security controllers connected to this instance. Upon a PR being lodged, Github actions is configured to run the entire test suite against our demo instance.

To contribute to the library, please fork this repository and lodge a pull request for us to accept your changes.

### Taskfile

[Task](https://taskfile.dev) is a task runner / build tool that aims to be simpler and easier to use than, for example, GNU Make. Gallagher Python Toolkit uses Task to run common tasks such as testing, linting, and building the documentation. First follow the [installation steps](https://taskfile.dev/installation/) to install Task on your system.

All the `tasks` are quite logically grouped and most of them will need you to have a `virtualenv` initialised via `uv`.

!!! info

    Our Github workflows use [Task](https://taskfile.dev/installation/#github-actions) via the Github action.

Some of the `task` targets take parameters e.g.

`task test` will run the entire test suite, while `task test -- test_cardholder.py` will run only the tests in `test_cardholder.py`.

### Building the docs

The documentation is build using [mkdocs](https://www.mkdocs.org) and hosted on [Github pages](https://anomaly.github.io/gallagher/). The project repository is configured to build and publish the documentation on every commit to the `master` branch.

Some handy commands to get you started:

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve -a localhost:8003` - Start the live-reloading docs server, `-a` allows you to provide a custom address.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

We have a wrapper for running the `mkdocs` web server at `task dev:docs` which runs the server on port `8001`.

To start contributing please fork this repository, make the changes you desire and submit a pull request for us to merge your changes in. Alternatively consider [starting a discussion](https://github.com/anomaly/gallagher/discussions) or [raising an issue](https://github.com/anomaly/gallagher/issues). Be kind to our maintainers and check to see if a similar discussion is already in place and join the thread.
