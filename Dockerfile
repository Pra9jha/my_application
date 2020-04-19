FROM python:3.7-alpine
MAINTAINER Prashant Devops

ENV PYTHONUNBUFFERED 1

#Adding ssh-key
ARG SSH_KEY
#RUN apt-get update -y && apt-get install git

ENV APP_HOME /apps
RUN mkdir $APP_HOME

# Make ssh dir
RUN mkdir /root/.ssh/ && touch id_rsa

# Copy ssh
#RUN echo "$SSH_KEY" > /root/.ssh/id_rsa && \
#    chmod 0600 /root/.ssh/id_rsa

# Create known_hosts
RUN touch /root/.ssh/known_hosts

# Add bitbuckets key
#RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure

WORKDIR $APP_HOME
COPY ./app/ $APP_HOME
RUN chmod -R 666 $APP_HOME

#RUN adduser -D user
#USER user