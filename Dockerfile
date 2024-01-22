# Use the official Python image as the base image
FROM python:3.11

# add user (change to whatever you want)
# prevents running sudo commands
RUN useradd -r -s /bin/bash aubrey-mccutchan

# set current env
ENV HOME /app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

RUN chown -R aubrey-mccutchan:aubrey-mccutchan /app
USER aubrey-mccutchan

# set app config option
ENV FLASK_ENV=production

# set argument vars in docker-run command
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION
ARG MYSQL_HOST
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_DB

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
ENV MYSQL_HOST $MYSQL_HOST
ENV MYSQL_USER $MYSQL_USER
ENV MYSQL_PASSWORD $MYSQL_PASSWORD
ENV MYSQL_DB $MYSQL_DB

# # Install necessary dependencies using Homebrew
# RUN brew update 
# #&& \
# #    brew upgrade && \
# #    brew install mysql-client && \
# #    brew install mysql-connector-c

# Avoid cache purge by adding requirements first
ADD ./requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r ./requirements.txt --user

# Add the rest of the files
COPY . /app
WORKDIR /app

# start web server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers=5", "--debugger", "--reload" ]
