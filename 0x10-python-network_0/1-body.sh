#!/bin/bash
# query a header
code=$(curl -sL -o /dev/null -w "%{http_code}" "$1")
if [ "200" == "$code" ]; then
	curl -L "$1"
fi
