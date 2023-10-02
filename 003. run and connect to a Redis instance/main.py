import redis

# Redis server configuration
redis_config = {
    'host': 'localhost',  # If your Redis container is running locally
    'port': 6379,         # Default Redis port
}

# Create a Redis client
client = redis.StrictRedis(**redis_config)

# Set a key-value pair
client.set('Key_1', 'Hello, Redis!')
client.set('Key 2', 'Another Hello')
client.set('3', 'Thrice the Helloes')
keys = [   
    client.get('Key_1'),
    client.get('Key 2'),
    client.get('3')
]

# Get the value by key
for index, item in enumerate(keys):
    print(f"Value for key_{index+1}: {item.decode('utf-8')}")

# Increment a counter
client.incr('mycounter')
counter_value = client.get('mycounter')
print(f"Counter Value: {counter_value.decode('utf-8')}")

# Close the Redis client connection
client.close()