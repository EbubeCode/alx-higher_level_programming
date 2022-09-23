#!/bin/bash
# query a header

length=$(curl -sI $1 | grep Content-Length | cut -d : -f2| sed -e 's/^[[:space:]]*//')
echo "${length##*( )}"
