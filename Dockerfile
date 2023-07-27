# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Uninstall Flask, Jinja2, MarkupSafe, itsdangerous, werkzeug and flask_login
RUN pip uninstall flask jinja2 markupsafe itsdangerous werkzeug flask_login -y
# Upgrade pip
RUN pip install --no-cache-dir -U pip
# Install specific versions of Flask, Jinja2, MarkupSafe, itsdangerous, werkzeug and flask_login
RUN pip install --no-cache-dir flask==1.1.2 jinja2==2.11.3 markupsafe==1.1.1 itsdangerous==1.1.0 werkzeug==1.0.1 flask_login==0.5.0

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
