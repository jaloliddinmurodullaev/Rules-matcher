FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy   the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run app.py when the container launches
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]