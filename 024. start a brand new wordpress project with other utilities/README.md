[⬅️ Back to repo home](https://github.com/Blankscreen-exe/docker-practice) [💻 Back to search](https://blankscreen-exe.github.io/docker-practice/)

# 024. Start a brand new WordPress project with other utilities

## What you will do?

- Setup an ubuntu machine which will host wordpress
- Setup Wordpress
- Setup a Mysql database for use with wordpress
- Setup PhPMyAdmin console and use it to manipulate the DB 

## How to do it?

This can be done easily via `docker compose up` command. The explaination of the `docker-compose.yml` file is as below:

```yml
version: "3"
```

This line specifies the version of the Docker Compose file format being used, which is version 3 in this case.

```yml
  services:
```

The services section defines the different Docker containers or services that will be part of your application.

```yml
    db:
```

This is the definition of the MySQL database service. It is given the name db.

```yml
      image: mysql:5.7
```

This line specifies the Docker image to be used for the db service, which is `mysql:5.7`. It pulls the MySQL 5.7 image from Docker Hub.

```yml
      restart: always
```

This line sets the restart policy for the db service, ensuring that the MySQL container will restart automatically if it stops for any reason.

```yml
    environment:
```

This section sets environment variables for the MySQL container.

```yml
      MYSQL_ROOT_PASSWORD: root_pass
      MYSQL_DATABASE: MyWordPressDB
      MYSQL_USER: MyWordPressUser
      MYSQL_PASSWORD: password
```

These lines define the environment variables for configuring MySQL. `MYSQL_ROOT_PASSWORD` is the root password for the MySQL server, `MYSQL_DATABASE` is the name of the database, `MYSQL_USER` is the username for connecting to the database, and `MYSQL_PASSWORD` is the password for the database user.

```yml
  phpmyadmin:
```

This is the definition of the phpMyAdmin service.

```yml
      image: phpmyadmin/phpmyadmin:latest
```

It specifies the Docker image for the phpMyAdmin service, which is `phpmyadmin/phpmyadmin:latest`, the latest version of phpMyAdmin.

```yml
      restart: always
```

Similar to the MySQL service, this line sets the restart policy for the phpMyAdmin service, ensuring it restarts if it stops.

```yml
      environment:
```

This section sets environment variables for phpMyAdmin.

```yml
        PMA_HOST: db
        PMA_USER: MyWordPressUser
        PMA_PASSWORD: password
```

These lines specify the hostname of the MySQL database (PMA_HOST), the MySQL username (PMA_USER), and the password (PMA_PASSWORD) that phpMyAdmin will use to connect to the MySQL server. db is used as the hostname, which corresponds to the MySQL service defined earlier.

```yml
      ports:
        - "8080:80"
```

This line maps port 8080 on the host machine to port 80 in the phpMyAdmin container, making phpMyAdmin accessible at http://localhost:8080 on the host.

```yml
  wordpress:
```

This is the definition of the WordPress service.

```yml
    depends_on:
      - db
```

This line specifies that the WordPress service depends on the db service, meaning the WordPress container will start only after the MySQL container (db) is up and running.

```yml
    image: wordpress:latest
```

It specifies the Docker image for the WordPress service, using the latest version of the WordPress image from Docker Hub.

```yml
    restart: always
```

Similar to the other services, this line sets the restart policy for the WordPress service.

```yml
    ports:
      - "8000:80"
```

This line maps port 8000 on the host to port 80 in the WordPress container, allowing you to access WordPress at http://localhost:8000 on the host.

```yml
    environment:
```

This section sets environment variables for configuring WordPress.

```yml
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: MyWordPressUser
      WORDPRESS_DB_PASSWORD: password
      WORDPRESS_DB_NAME: MyWordPressDB
```

These lines define the database connection settings for WordPress. `WORDPRESS_DB_HOST` specifies the hostname and port of the MySQL server, `WORDPRESS_DB_USER` is the username to access the database, `WORDPRESS_DB_PASSWORD` is the password for the database user, and `WORDPRESS_DB_NAME` is the name of the database.

```yml
    volumes:
      - ["./:/var/www/html"]
```

This line sets up a volume, allowing the local directory (in this case, the current directory) to be mounted to the `/var/www/html` directory in the WordPress container. This is a common practice to allow data persistence for WordPress.

```yml
volumes:
  mysql: {}
```
This section defines a named volume named mysql. Named volumes are typically used for data storage or data persistence between container restarts. In this case, it's used for the MySQL data.
