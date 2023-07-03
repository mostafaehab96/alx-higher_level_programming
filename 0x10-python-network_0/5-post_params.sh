#!/bin/bash
#Sends a Post request with some parameters
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
