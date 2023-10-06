# Run and connect to a postgres DB instance

I have established a postgres database instance withing a docker container and have accessed it using a simple python script. For now I am just printing the version(and other detials) of the database, but you are able to run full fledged queries.

## How To Use It?

First we need to pull a Postgres image

```shell
docker pull postgres
```

Then we will create a docker container from thet image

```shell
docker run --name postgres-container -e POSTGRES_PASSWORD=yourpassword -d -p 5432:5432 postgres
```

`-p 5432:5432` maps the port on the docker environment to our local system's environment, so we can access it on port `5432`

You can check the running container with

```shell
docker ps
```

Before you connect your python script file with the database instance, you need to install a driver for it.

```shell
pip install psycopg2-binary
```

## Create Backup Files From The Database Inside The Container

First make sure that the container with `--name psotgres-container` is running.

create a directory where you will be storing your backups

```shell
docker exec postgres-container mkdir /db_backup
```

Use `postgres` to generate a backup `.sql` file

```shell
docker exec -it --privileged --workdir /db_backup postgres-container pg_dump -U postgres -w -F p -d <db_name> > <output_file>.sql
```

Then copy the backup file from within the `/db_backup` directory to the current working directory of your host machine

```shell
docker cp postgres-container:/db_backup/<output_file>.sql <your_host_machine_path>
```

Then you will see that a `.sql` has been generated in the current directory.

For this you can also use the `create_backup.sh` file.

Following is a sample usage of this file:

```shell
./create_backup.sh <your_db_name>
```

If you successfully run it you will see something like this:

```shell
PostgreSQL container is already running...
db_backup_testdb001_2023-10-06_18:39.sql was copied to:
/workspaces/docker-practice/002. run and connect to a Postgres instance
```

> **NOTE:** description of how this file works is given inside the file itself

## Loading A Backup File To The Database Inside Docker 

First make sure that the container with `--name psotgres-container` is running.

Then copy the backup file from your host machine to the backup directory inside the container called `/db_backup`. Create this directory if it does not already exists.

```shell
docker cp <backup_file> <container_name>:/db_backup/<backup_file>
```

Then use `psql` to load the backup to your DB (inside the container)

```shell
docker exec -it <container_name> psql -U <db_username> -d <db_name> -a -f /db_backup/<backup_file> 
```

For this you will use the `load_backup.sh` file.

Following is a sample usage of this file:

```shell
./load_backup.sh <your_db_name> <backup_file_name>
```

If you successfully run it you will see something like this:

```shell
PostgreSQL container is already running...
db_backup_testdb001_2023-10-06_18:39.sql was copied to:
/workspaces/docker-practice/002. run and connect to a Postgres instance
```

> **NOTE:** description of how this file works is given inside the file itself