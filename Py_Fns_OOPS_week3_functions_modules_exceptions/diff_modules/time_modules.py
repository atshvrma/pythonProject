import time

print("Current timestamp:", time.time())
#
print("Readable time:", time.ctime())
#
#
# print("Waiting for 5 seconds...")
# time.sleep(5)
# print("Done!")
#
start = time.time()

# Code block to measure
# for i in range(1000000):
#     pass

print("Revision")
time.sleep(1*30)
# print("Diff Modules ")
# time.sleep(15*60)


end = time.time()
print("Execution time:", end - start, "seconds")

total_time_in_sec = end-start

print(total_time_in_sec/60)


