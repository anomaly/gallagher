# Use an official Python runtime based on Debian 12 "bookworm" as a parent image.
FROM python:3.12-slim-bookworm  

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet 
RUN apt-get install --yes --quiet --no-install-recommends build-essential
RUN rm -rf /var/lib/apt/lists/*

# Copy poetry files and get ready to install package
WORKDIR /opt
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

# Ask poetry to install all packages including the app
# not in virtual machine as we are in a container
# In prodduction add --no-dev to poetry installation
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Build and install the package
COPY gallagher gallagher
# README is reference by the package
COPY README.md README.md
RUN poetry build

# Install the package
RUN pip3 install dist/*.whl

# Remove the source
RUN rm -rf gallagher
RUN rm -rf dist
RUN rm README.md

# Copy the files in the src directory which is the app package
# and the dependency matrix dedescribed by pyproject.toml
WORKDIR /opt/gallagher

# Run the CLI
ENTRYPOINT [ "gala" ]