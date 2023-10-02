# Run and connect to a postgres DB instance

I have established a postgres database instance withing a docker container and have accessed it using a simple python script. For now I am just printing the version(and other detials) of the database, but you are able to run full fledged queries.

# How To Use It?

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