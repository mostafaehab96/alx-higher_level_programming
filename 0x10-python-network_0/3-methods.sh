#!/bin/bash
#Get the methods allowed from url
curl -s -I "$1" | grep Allow | awk -F ': ' '{print $2}'
