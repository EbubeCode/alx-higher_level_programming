#!/bin/bash
# query a header
curl -sL "$1" -w ", %{http_code}" | grep ", 200" | sed -e 's/, 200//' | tr -d '\n'
