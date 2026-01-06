### Multithreading
### When to use

## I/o bound tasks: Tasks that spend more time waiting for I/O operations (e.g. file operations, network request)

### concurent execution: When you want to improve throughput of your application by performing multiple operations concurrently

# import threading
# import time

# def print_number():
#     for i in range(5):
#         time.sleep(2)
#         print(f"Number: {i}")


# def print_letters():
#     for letter in 'abcde':
#         time.sleep(2)
#         print(f"Letter: {letter}")


# t = time.time()

# print_number()
# print_letters()

# fin_t = time.time()-t
# print(fin_t)

## Output v1
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Letter: a
# Letter: b
# Letter: c
# Letter: d
# Letter: e
# 20.01015019416809


import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")


def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter: {letter}")

## create 2 threads
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letters)


t = time.time()

## start the threads
t1.start()
t2.start()

### Wait for the threads to complete
t1.join()
t2.join()

fin_t = time.time()-t
print(fin_t)

## Output v2
# Number: 0
# Letter: a
# Number: 1
# Letter: b
# Number: 2
# Letter: c
# Number: 3
# Letter: d
# Number: 4
# Letter: e
# 10.005976676940918