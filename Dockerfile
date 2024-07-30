# Use an official Python runtime based on Debian 12 "bookworm" as a parent image.
FROM python:3.12-slim-bookworm  

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    curl \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    && rm -rf /var/lib/apt/lists/*


# Install task from their servers, not this requires curl
# so you must only have this tkas post the apt updates
RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" \
    -- -d -b /usr/local/bin

WORKDIR /opt
COPY Taskfile.yml Taskfile.yml
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

# Ask poetry to install all packages including the app
# not in virtual machine as we are in a container
# In prodduction add --no-dev to poetry installation
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Copy the files in the src directory which is the app package
# and the dependency matrix dedescribed by pyproject.toml
WORKDIR /opt/${PROJ_NAME}

# Run the CLI
ENTRYPOINT [ "gala" ]