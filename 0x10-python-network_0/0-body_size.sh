#!/bin/bash
# query a header

length=$(curl -sI localhost:5000 | grep Content-Length | cut -d : -f2| sed -e 's/^[[:space:]]*//')
echo "${length##*( )}"
