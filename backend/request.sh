#!/bin/bash

CURL="/usr/bin/curl"

ARCHWAIFU="http://127.0.0.1:8000"
ENDPOINT="/api/v1/icons/image/"

JSON_CONTENT="Content-Type: application/json"
FORM_CONTENT="Content-Type: multipart/form-data"

$CURL\
    -X "POST"\
    -H "$FORM_CONTENT"\
    -F "image=@/home/hireki/Downloads/985056.jpg"\
    "${ARCHWAIFU}$ENDPOINT"

