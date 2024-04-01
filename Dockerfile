FROM python:3.11 as compiler

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

RUN python3 -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt


# Run app.py when the container launches
CMD ["uvicorn", "run:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]