#!/bin/bash
#Gets only the status code from url
curl -s -o /dev/null -w "%{http_code}" "$1"
