#!/bin/bash

export ENV=test

.venv/bin/pytest --cov=src tests/ -W ignore::DeprecationWarning --cov-report=xml --cov-report=term-missing
