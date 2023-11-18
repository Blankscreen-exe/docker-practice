[⬅️ Back to repo home](https://github.com/Blankscreen-exe/docker-practice) ▪️ [↗️ Back to search](https://blankscreen-exe.github.io/docker-practice/)

# Host An Existing Wordpress Project

This is for when you have an existing wordpress project either half done finished product and you want to dockerize that so that it will run anywhere along with the associated database.

## What You Will Do?

- [x] Import a wordpress project into a docket container volume.
- [x] Setup volume for storing the project and associated files.
- [x] Setup a Mysql database (*with a backup file*) and connect it with PhpMyadmin interface.
- [x] Import environment variables from a .env file to the container.

## Good To Know Beforehand

- The docker compose script used here will look for a database backup (MySql) exported file in the same directory as `docker-compose.yml`.
- Sensitive information will be set inside the `.env` file such as database host name and passwords.

## How To Do It?

This Docker Compose file defines three services: `wordpress`, `db` (MySQL), and `phpmyadmin`. Here is an explaination of the docker compose file:

### WordPress Service
- **Depends On:** This service depends on the `db` service, ensuring that `db` starts before `wordpress`.
- **Image:** Uses the official `wordpress:latest` Docker image.
- **Volumes:** Mounts local directories to the WordPress container, specifically `./site/wp-content` to `/var/www/html/wp-content` and `./init/prep.sh` to `/usr/local/bin/prep.sh`.
- **Ports:** Maps port `80` on the host machine to port `80` within the `wordpress` container.
- **Restart Policy:** Configured to always restart in case of failure.
- **Environment Variables:** Sets various environment variables needed for WordPress, including database connection details (`WORDPRESS_DB_HOST`, `WORDPRESS_DB_USER`, `WORDPRESS_DB_PASSWORD`), table prefix (`WORDPRESS_TABLE_PREFIX`), debugging mode (`WORDPRESS_DEBUG`), and disabled plugins (`DISABLED_PLUGINS`).

### MySQL Service (db)
- **Image:** Uses the `mysql:5.7` Docker image.
- **Platform:** Specifies the platform as `linux/x86_64`.
- **Volumes:** Mounts local directories to the MySQL container, such as `./database` to `/var/lib/mysql`, `./backup.sql.gz` to `/docker-entrypoint-initdb.d/backup.sql.gz`, and `./init/migrate.sh` to `/docker-entrypoint-initdb.d/migrate.sh`.
- **Ports:** Maps port `3306` on the host machine to port `3306` within the `db` container (MySQL default port).
- **Restart Policy:** Configured to always restart.
- **Environment Variables:** Sets MySQL-specific environment variables, including the root password (`MYSQL_ROOT_PASSWORD`), database name (`MYSQL_DATABASE`), user (`MYSQL_USER`), user password (`MYSQL_PASSWORD`), WordPress table prefix (`WORDPRESS_TABLE_PREFIX`), and production URL (`PRODUCTION_URL`).

### phpMyAdmin Service
- **Image:** Uses the `phpmyadmin/phpmyadmin:latest` Docker image.
- **Restart Policy:** Configured to always restart.
- **Environment Variables:** Sets phpMyAdmin configuration variables like the database host (`PMA_HOST`), user (`PMA_USER`), and password (`PMA_PASSWORD`).
- **Ports:** Maps port `8080` on the host machine to port `80` within the `phpmyadmin` container, allowing access to phpMyAdmin through `localhost:8080` on the host machine.

This setup launches a WordPress site, a MySQL database, and phpMyAdmin for database management, allowing you to access and manage your WordPress database through phpMyAdmin on port `8080`, while the WordPress site itself will be accessible on port `80`.

## Resources

- [stephenafamo.com: moving a wordpress site into a docker container](https://stephenafamo.com/blog/posts/moving-a-wordpress-site-into-a-docker-container)
- [wirelessmoves.com: dockerizing an existing wordpress site](https://blog.wirelessmoves.com/2021/03/dockerizing-an-existing-wordpress-site.html)
- [Lumonald's Github Repository](https://github.com/lumonald/existing-wordpress-development-docker/blob/master/docker-compose.yml)
- [A discussion on reddit](https://www.reddit.com/r/docker/comments/tj8qp2/containerize_an_existing_wordpress_site/)
