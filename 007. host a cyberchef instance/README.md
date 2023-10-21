[⬅️ Back to repo home](https://github.com/Blankscreen-exe/docker-practice) [💻 Back to search](https://blankscreen-exe.github.io/docker-practice/)

# Host a CyberChef Instance

> CyberChef is a simple, intuitive web app for carrying out all manner of "cyber" operations within a web browser. These operations include simple encoding like XOR and Base64, more complex encryption like AES, DES and Blowfish, creating binary and hexdumps, compression and decompression of data, calculating hashes and checksums, IPv6 and X.509 parsing, changing character encodings, and much more.
>
> -- from https://github.com/gchq/CyberChef

## What You Will Do?

- Host a cyber chef instance

## How To Do It?

It is a very simple task that can be done via a simple `docker-compose.yml` script.

Simply run the following inside the directory of the yaml file. 

```shell
docker compose up
```

The contents of the provided docker-compose.yml are described as below:

```yml
services:
  cyber-chef:
    image: mpepping/cyberchef:latest
```

The image we are using comes from `mpepping` on docker hub.

```yml
    ports:
      - "8000:8000"
```

We are mapping the ports so that we can access the app through our host machine.

Since you will mainly be downloading your results through the "Save" button, therefore you won't need to set up a volume for this container.