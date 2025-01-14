# emby-sync

Running the server in docker:

`docker run --name emby-sync -e EMBY_SERVER='<emby_url>' -e SECRET_KEY='<emby_api_key>' -p 5000:5000 lastelement21/emby-sync:latest`


Runs on port 5000 in the container, publish to whatever you want


Requires several ENV variables to be passed to the container:

SECRET_KEY: This should be an API key for your emby server.

EMBY_SERVER: This should be the URL used to connect to your server.

(Optional) DEFAULT_ROOM: A room name which always exists. Default is 'Bacon Bar'

(Optional) INTERVAL: The interval of the synchronization loop, in seconds. Default '3.0' seconds.
Setting this shorter will yield a higher load on the Emby server, but on a low latency connection can give very good synchronization results.

Known Issue: Chromecasts cannot follow, but can lead.  Workaround by controlling the device casting to the Chromecast.

# Troubleshooting
## Local players can sync, but Internet players can't:
Even if Emby can normally play over the internet, your reverse proxy might be configured wrong.
In the developer console on your browser you might see `wss://` related errors.
This means that your reverse proxy isn't correctly configured.
See [https://emby.media/community/index.php?/topic/47508-how-to-nginx-reverse-proxy/](https://emby.media/community/index.php?/topic/47508-how-to-nginx-reverse-proxy/) to correct your setup. 

# Development
API reference:
[http://swagger.emby.media/?staticview=true#/SessionsService/](http://swagger.emby.media/?staticview=true#/SessionsService/)

## Start Development Server
```
python dev_start.py
```
For the dev server, the host and port can be defined by using environment variables:  
```
export HOST="0.0.0.0"
export PORT="5000"
python dev_start.py
```