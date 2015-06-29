websocket_messager
==================

A HTTP service allow server push message to browsers. Based on websocket.

## Install:

1. pip install tornado
1. Edit config.py. If server and client both at localhost, skip this step.
1. Run service: `python websocket_messager.py`

## Test:

1. Open the example page with browser: `http://localhost:8100/example`.
1. Try to post some `msg` to messager url: `dev.wis.com:8100/msg`. Note: The example page only detect `msg` argument in post data. This can be change in your app.
1. See the msg on your browser.

## Usage:
1. Browser chat.
2. Push message to browser from server.
