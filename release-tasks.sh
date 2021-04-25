#!/bin/bash

heroku run bash
cd src 
python manage.py migrate