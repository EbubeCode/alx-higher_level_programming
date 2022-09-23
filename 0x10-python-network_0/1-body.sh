#!/bin/bash
# query a header
code=$(curl -sL -o tmp -w "%{http_code}" "$1")
if [ "200" == "$code" ]; then
	cat tmp
fi
