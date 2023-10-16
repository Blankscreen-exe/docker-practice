# Host Tor Browser 

## How To Do It?

We can do this with only one singe `docker-compose.yml` file. This file is officially provided [here](https://hub.docker.com/r/domistyle/tor-browser)

Here's an explanation of each line in it:

```yml
version: '3.9'
```

This line specifies the version of Docker Compose being used. In this case, it's version `3.9`.

```yml
services:
  tor:
```

This section defines a Docker service named "*tor*" The service will be based on the Docker image specified and will have the configurations defined within this section.

```yml
    image: domistyle/tor-browser
```

This line specifies the Docker image to use for the "*tor*" service. The image "*domistyle/tor-browser*" is used as the base image to create the container.

```yml
    restart: always
```

This line instructs Docker to restart the container automatically if it exits or encounters an error. The "*always*" keyword ensures that Docker will restart the container regardless of the exit status.

```yml
    ports:
      - 5800:5800
      - 5900:5900
```

This section maps container ports to host ports. It allows you to access the container's services over specific ports on your host machine. In this case, it maps port `5800` and `5900` from the container to the same ports on the host.

```yml
    environment:
      DISPLAY_WIDTH: 1920
      DISPLAY_HEIGHT: 1080
      KEEP_APP_RUNNING: 1
      TZ: Europe/Vienna
```

These environment variables are set within the container:

`DISPLAY_WIDTH` and `DISPLAY_HEIGHT` define the display resolution of the Tor Browser within the container.
`KEEP_APP_RUNNING` is set to `1`, which might be a custom configuration used by the image author to ensure the Tor Browser remains running.
TZ sets the timezone to "*Europe/Vienna*" within the container.

```yml
    volumes:
      - /srv/tor:/app/Browser/TorBrowser/Data/Tor
```

This line sets up a Docker volume, which is a directory on the host machine that gets mounted inside the container. In this case, it maps the directory `/srv/tor` on the host to the path `/app/Browser/TorBrowser/Data/Tor` within the container. This volume mapping is typically used for persisting data and configurations, so the data from the Tor Browser can be stored and accessed across container restarts.

==================
### scratch stuff

https://av.tib.eu/media/54515

```yml
version: "2" services:
  tor:
    image: goldy/tor-hidden-service:latest
    links:
      -wordpress
    restart: always
# Keep keys in volumes
    volumes:
      - ./tor:/var/lib/tor/hidden_service
    environment:
# Set mapping ports
      WORDPRESS_PORTS: "80:80"

  db:
    image: mariadb
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress123
    volumes:
      - ./mysql:/var/lib/mysql

    wordpress:
      depends_on:
        - db
      image: wordpress:latest
      links:
        - db
      restart: always
      environment:
        WORDPRESS_DB_HOST: db:3306
        WORDPRESS_DB_USER: wordpress
        WORDPRESS_DB_PASSWORD: wordpress123
```
