FROM python:3.7.16

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

# Run the application
COPY .env /app
COPY githubforker/ /app
CMD . /opt/venv/bin/activate