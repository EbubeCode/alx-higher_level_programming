#!/bin/bash
# query a header
curl -I -sL -X OPTIONS "$1" | grep Allow: | sed -e 's/Allow: //'
