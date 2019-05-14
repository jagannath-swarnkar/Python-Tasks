# Discuss - Multi-processing and Multi-threading in Python
## MULTI-THREADING 
MultiThreading is the ability of a processor to perform more than two threads(moltiple threads) concurrently within the same process.

ex- when we have to make multiple requests like 1000 requests using api then in python as it is synchronous programe so it will execute one by one and it will take much more time to execute the whole programe
    beside this we can use multithreading, with using multithreading we can make multiple requests in same time and it will execute the whole process in less time.

## MULTI-PROCESSING
Multiprocessing is the ability of a system to support more than one processor at the same time.
more than one cpu are added to the system to increase the computing speed of the programe

## GIL
GIL stands for Global Interpreter Lock, It is a mechanism to synchronise the execution of threads,
This essentially means is a process can run only one thread at a time. When a thread starts running,
it acquires GIL and when it waits for I/O, it releases the GIL, so that other threads of that process can run.
