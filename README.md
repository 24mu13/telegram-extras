# Telegram extra features

<img src="logo_plus.png" alt="logo" width="64"/>

At the time being there are few features not yet implemented on **Telegram**, neither on *Premium* subscription.

The goal of this repository is providing **containerized module** written in *Python* for having such features: you will need to run the container against your account on your *host* (e.g. NAS) or in the *cloud* (e.g. Azure, AWS, GCP).

## Extra features

- [No voice policy](no-voice-policy/README.md): auto replies to any personal voice message received asking to send a text instead
- [Notify once fragmented text](notify-once/README.md): auto snoozes subsequent messages from the same sender within a certain time frame (e.g. 1 minute)

## How to use

* *Get API ID & hash*, first time only
* *Run the extra*, as a container

### Get API ID & hash

* Go to https://my.telegram.org
* *API development tools*
* Create a new *Telegram Extras* app to get **api_id** & **api_hash**

### Run the extra

Here below few examples in real scenarios.

#### Locally

* Pull the extra image
  
  `docker pull arisedream/telegram-extras-<extra-name>`
* Run interactively for setting up your account
  ```
  docker run -i -t \
    --name telegram-extras-<extra-name> \
    -e TG_API_ID=<your-id> \
    -e TG_API_HASH=<your-hash> \
    -v /your/path/telegram-extras-<extra-name>.session:/telegram-extras-<extra-name>.session \
  telegram-extras-<extra-name>
  ```
* For running as a service
  ```
  docker run -d \
    --name telegram-extras-<extra-name> \
    --restart unless-stopped \
    -e TG_API_ID=<your-id> \
    -e TG_API_HASH=<your-hash> \
    -v /your/path/telegram-extras-<extra-name>.session:/telegram-extras-<extra-name>.session \
  telegram-extras-<extra-name>

  ```

#### NAS (Synology DSM 7)

* Run locally as described above to get **session** file `telegram-extras-<extra-name>.session`
* Create folder `/volume1/docker/telegram-extras/<extra-name>`
* Place the session file on the created folder
* Go to **Container Manager** app
* Create new image from `arisedream/telegram-extras-<extra-name>`
* Create new container `telegram-extras-<extra-name>`
  * Enable *auto-restart*
  * *Environment*:
      * TG_API_ID=\<your-id\>
      * TG_API_HASH=\<your-hash\>
  * *Volume Settings*:
    * `/docker/telegram-extras/<extra-name>/telegram-extras-<extra-name>.session` -> `/telegram-extras-<extra-name>.session`

#### Cloud 

TBD

## FAQ

### Why don't you use bot?

Using [bot](https://core.telegram.org/bots) we can't achieve the same result: it works in fact as long you are texting to it, or when including it on a group. Instead, when using API, we could react with some extra functionality, regardless the sender.

## References

* [Telethon](https://github.com/LonamiWebs/Telethon): API Telegram client library for Python 3
