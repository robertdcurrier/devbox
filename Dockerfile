# GCOOS DMAC Application Docker File
FROM robertdcurrier/devbox:latest
MAINTAINER Bob Currier <robertdcurrier@gmail.com>
ENV REFRESHED_AT 2020-09-17

# Set the working directory to the name of the app /sban, /habscope, etc
WORKDIR /devbox
# No requirements.txt -- all in the base image. This is the way of the Monkey.
USER 1000:1000
