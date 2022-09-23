#!/bin/bash
# query a header
curl -sL -X POST -d email=test@gmail.com -d subject="I will always be here for PLD" "$1"
