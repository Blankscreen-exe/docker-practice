[⬅️ Back to repo home](https://github.com/Blankscreen-exe/docker-practice) ▪️ [↗️ Back to search](https://blankscreen-exe.github.io/docker-practice/)

# Create A Persistent Data Storage Area To Store Backup Files

Docker volumes are a way to share storage area (e.g. a folder of your choice) and use it with the host machine. In this way the application running inside the container can be made to depend on the files you directly edit from within your host machine. 

## What You Will Do?

- [x] Create a docker volume and attach it to a container.
- [x] Use the volume to store files from within the contain and access it with the host machine.

## How To Do It?

Here's an example of creating a Docker volume and using it to store backup files:

1. **Create a Docker volume:**

```bash
docker volume create backup_data
```

This command creates a Docker volume named `backup_data`. You can replace `backup_data` with your desired volume name.

2. **Run a container with the volume attached to store backup files:**

For instance, if you have a container that needs to create or access backup files, you can mount the volume to that container:

```bash
docker run -d --name backup_container -v backup_data:/backup your_image_name
```

Replace `your_image_name` with the image name of the container that requires access to the volume for storing backup files. `-v backup_data:/backup` flag mounts the `backup_data` volume to the `/backup` directory inside the container.

3. **Use the volume for backup storage:**

Once the `backup_container` is running, any files written to `/backup` inside the container will be stored in the `backup_data` volume on the host machine. For example, your backup script or application within the container can write backup files to `/backup`:

```bash
docker exec -it backup_container bash
# Now, inside the container
touch /backup/my_backup_file.txt
```

This creates a file `my_backup_file.txt` within the `/backup` directory of the `backup_container`, and it will be stored persistently in the `backup_data` volume on the host machine.

Remember, Docker volumes persist even if the container using them is removed, allowing data to be retained across container restarts or recreations.

You can easily back up or retrieve these files by mounting the same volume to another container or by accessing the volume directly on the host machine using the path where Docker volumes are stored (typically under `/var/lib/docker/volumes/` on Linux).

