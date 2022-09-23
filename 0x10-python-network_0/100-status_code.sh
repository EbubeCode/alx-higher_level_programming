#!/bin/bash
# query a header
curl -sL -o /dev/null "$1" -w "%{http_code}"
