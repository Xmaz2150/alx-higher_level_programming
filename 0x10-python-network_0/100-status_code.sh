#!/bin/bash
# sends request to URL and displays stsutus code of response
curl -s -o /dev/null -w "%{http_code}" $1
