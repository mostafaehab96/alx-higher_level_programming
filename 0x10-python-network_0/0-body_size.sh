#!/bin/bash
#Gets the content-length header value with curl command
curl -s -I "$1"| grep Content-Length | cut -d ' ' -f2
