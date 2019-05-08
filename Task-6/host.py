# step 1: import the redis-py client package
import redis
from random import random

# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

def set_data():
    """Example Hello Redis Program"""
    
    # step 3: create the Redis Connection object
    try:
    
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    
        # step 4: Set the hello message in Redis 
        for i in range(100):
            value = int(random()*10000)
            r.set(i, value)
            # print(r.get(i))

        # # step 5: Retrieve the hello message from Redis
        # msg = r.get("msg:hello")
        # print(msg)        
        for i in range(100):
            # msg = r.get(i)
            # print(msg)     
            print(r.get(i))   
    
    except Exception as e:
        print(e)

set_data()