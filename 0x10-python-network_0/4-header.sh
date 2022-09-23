#!/bin/bash
# query a header
curl -sL -X GET -H "X-School-User-Id: 98" "$1"
