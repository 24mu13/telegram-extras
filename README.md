# Telegram extra features

At the time being those featuxes are not there!
Docker image to run with app id/hash and text (+ optional .ogg file)

If you have a NAS follow the procedure, you could also use another device or even the cloud (Azure ACI or AKS?)

## How to use

* my.telegram.org
* API development tools
* api_id & api_hash

## Extra features

- [No voice policy](no-voice-policy/README.md)
- [Notify only once for multiple messages](notify-once/README.md)

## How to build

Build:

`docker build -t telegram-extras-<extra-name> .`

Run interactively:

`docker run -i -t telegram-extras-<extra-name>`

Run with volume:

`docker run -d --name tgext -v /your/path/tgext-<extra-name>.session:/tgext-<extra-name>.session tgext-<extra-name>`

See: https://docs.docker.com/storage/volumes/

## FAQ

### Why you don't use bot?

It's different, here we want to react in some extra way regardless the sender..