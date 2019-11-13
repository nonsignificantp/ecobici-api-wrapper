========================
Ecobici API v1.0 wrapper
========================

.. contents:: Table of Contents
.. section-numbering::

Description
===========

``Ecobici API v1.0 wrapper`` is a fastAPI wrapper around Buenos Aires' ecobici API found on the original ecobici status map. **Since 2019 a new system was put in place together with a clean fresh API**, however the old API is still in place and running. The main purpose of this wrapper was to implement a cleaner way of making apy calls and querys mixed with corrected data types in each field.

Installation
============

First step is to clone the repository::

    git clone https://github.com/nonsignificantp/ecobici-api-wrapper.git

Makefile
--------

Inside the root folder type the following on the command line::

    make build && make run

This command will build a docker image from the Dockerfile and the run a container mapping port 8000.

Dockerfile
----------

Build the docker image using::

    docker build -t ecobici:latest .

Followed by::

    docker run -p 8000:8000 ecobici:latest

API
===

:``/estaciones/{numero}``  Returns information of station.






