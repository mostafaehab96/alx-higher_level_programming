#!/bin/bash
#Sends a file with a post request
curl -s -X POST -H "Content-Type: application/json" -T "$2" "$1"
