#!/bin/bash
#Displays You got me!, in the body of the response.
curl -sLX PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me_3
