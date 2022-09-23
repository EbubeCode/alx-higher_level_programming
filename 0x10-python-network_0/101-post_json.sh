#!/bin/bash
# query a header
curl -sL -X Post -H "Content-Type: application/json" -d @"$2" "$1"
