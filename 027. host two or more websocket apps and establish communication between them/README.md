[⬅️ Back to repo home](https://github.com/Blankscreen-exe/docker-practice) ▪️ [↗️ Back to search](https://blankscreen-exe.github.io/docker-practice/)

# Host two websocket apps

We are going to use a simple websocket *server* and *client* applications and containerize them. Then we will host two identical instances of the *client* application with one instance of *server* and make them communicate with each other.

## What You Will Do?

- [x] Write a simple websocket script to work as a server which recieves JSON messages from clients and responds with "Pong!"
- [x] Write a simple websocket script to work as a client which overtime sends JSON messages "Ping!" to server
- [x] Containerize both the applications/scripts
- [x] Host two or more identical intances of the client application/script
- [x] Enable networking between the application clones to communicate with each other

## How To Do It?

### Server Script

First up we will write a server script in Python which can be found in `/server/` folder.

This server is designed to give out only one response i.e. "Pong!" to every client requests.

The structure of this script is simple. There is a function named `server` which accepts two arguments: `websocket` and `path`.

While `path` is an argument passed in this function, it is not used anywhere. If you were to print it out you would see `/` as your output, because it only represents the URI the clients are using to access the server.

`websocket` argument on the other hand is an object which contains information about the two-way communication that the client initiated. This object contains a message that is in JSON string format (sent by client).

To respond to the client's message I used `websocket.send("Pong!")` which sends a string response back to the client who initiated the communication.

To serve this script and make ready to accept connections from clients I added `websockets.serve()` which accepts three arguments: the function's name which in this case is `server`, the host name where it should be serving `0.0.0.0` and the port number `8765`.

The server is able to keep a log file named `server_logs.txt` which will be created as soon as the server recieves its first request. A sample view of the text file would be like this:

```
[19-12-2023 12:43:12] Recieved from client ("Client-300"): Ping!
[19-12-2023 12:43:13] Recieved from client ("Client-100"): Ping!
[19-12-2023 12:43:14] Recieved from client ("Client-200"): Ping!
[19-12-2023 12:43:16] Recieved from client ("Client-100"): Ping!
[19-12-2023 12:43:17] Recieved from client ("Client-300"): Ping!
[19-12-2023 12:43:18] Recieved from client ("Client-200"): Ping!
[19-12-2023 12:43:19] Recieved from client ("Client-100"): Ping!
[19-12-2023 12:43:22] Recieved from client ("Client-200"): Ping!
[19-12-2023 12:43:23] Recieved from client ("Client-300"): Ping!
[19-12-2023 12:43:24] Recieved from client ("Client-100"): Ping!
```

### Client Script

The client script can be found inside the `/client/` folder.

This client is designed to repeatedly (after fixed amount of intervals as defined by `LAG_TIME`) send a JSON message to the server with the `CLIENT_NAME` as it's identity and the string message "Ping!".

The client script uses `websockets.connect(uri)` to establish a connection with the server we created above. The `uri` is the indicator of where the server is serving from. in this case it is `ws://server:8765`. 

> **Note**: Here the name `server` in the URI represents the service name as written in `docker-compose.yml` file.

We convert our message (which is a python dictionary) into string so that it can be sent over the network using `json.dumps()` and then send it using `websocket.send()`.

The `await` keyword waits for the response to come back before executing the client function any further.

We then get the response from the server with `websocket.recv()` and print out its message.

### Containerizing the both the Applications

Dockerizing both of them is pretty simple as well as identical.

First we copy the script file inside the container and install the script dependencies using `pip install`.

When that is done we run the command to execute the script file e.g. `python name-of-file.py`

### Host Two or more instance of the Client Applications

Inside the `docker-compose.yml` file, under every service name there is a parameter named `build`. This parameter defines the location of the `Dockerfile` which contains information on how the container for this particular service should be built.

Since clients are designed to have some environment variables which makes them easier to identify and differentiate between we also passed in `CLIENT_NAME` which is the identity of the client and `LAG_TIME` the time(in seconds) it should wait before sending the next request.

The `depends_on` parameter shows that the client containers should only be started AFTER the server container is up and running. Otherwise it would cause the clients apps to blow up since they won't find the server they want to connect with.

Since all of the communication is going within the Docker environment we do not need to expose and ports to our host machine.

### Checking the server logs

The server script stores its logs in a file named as `server_logs.txt` present in the same directory as `server.py`.

To check in on the continuously increasing logs, you can run the following from your terminal:

```shell
docker logs websockets-server-1
```

Where `websockets-server-1` is the name of the server container.

To check the `server_logs.txt` file from within the container, you can run:

```shell
# get into container shell
docker exec -it websockets-server-1 bash

# go into the /app directory
cd /app

# open the server_logs.txt to view its contents
cat server_logs.txt
```

## Resources

- [Building an instant messaging application using Python and WebSockets](https://medium.com/@abderraoufbenchoubane/building-a-real-time-websocket-server-using-python-d557c43a3ff3)

