#!/bin/bash
# sends a JSON POST request to URL passed as first argument, and displays body of response
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
