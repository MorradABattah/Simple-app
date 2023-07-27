# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Upgrade pip
RUN pip install --no-cache-dir -U pip
# Install Flask, Jinja2, MarkupSafe, itsdangerous, werkzeug, flask_login, and pytz
RUN pip install --no-cache-dir flask jinja2 markupsafe itsdangerous werkzeug flask_login pytz

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
