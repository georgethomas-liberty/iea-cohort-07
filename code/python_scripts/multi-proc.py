import os
import multiprocessing
import queue
import time


def worker(q):
    pid = os.getpid()
    while True:
        try:
            next_task = q.get(timeout=1)
        except queue.Empty:
            print("Worker", pid, "quitting.")
            break
        print("Worker", pid, "processing:", next_task)
        time.sleep(1)


# Create work tasks in the main process
# and use a Queue to distribute work to the
# child processes
to_do = multiprocessing.Queue()
for i in range(100):
    to_do.put(f"Record #{i}")

processes = [multiprocessing.Process(target=worker, args=(to_do,)) for i in range(10)]

for proc in processes:
    proc.start()
for proc in processes:
    proc.join()
print("All work complete!")
