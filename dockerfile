# Use Python 3.10 as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Install pytest
RUN pip install pytest

# Set the entrypoint
ENTRYPOINT ["python"]