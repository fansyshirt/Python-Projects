from timeit import default_timer as timer
print("this should take 50 seconds, don't close the project")
start = timer()
for item in range(1, 1000000000):
    time = item
stop = timer()
print(stop-start)
