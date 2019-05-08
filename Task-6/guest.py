# step 1: import the redis-py client package
import redis

# importing user input detail from host file
# from host import user
# data = user
# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "localhost"
redis_port = 6379
redis_password = ""

def get_data():
    """Example Hello Redis Program"""
    
    # step 3: create the Redis Connection object
    try:
    
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    

        # step 5: Retrieve the hello message from Redis
        for i in range(100):
            msg = r.get(str(i))
            print(msg)        
    
    except Exception as e:
        print(e)

get_data()