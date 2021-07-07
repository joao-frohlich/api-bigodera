#!/bin/bash

export $(xargs < configure.env)
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_PORT=5001
