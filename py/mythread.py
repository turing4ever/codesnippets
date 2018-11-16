import threading
import time

def worker(*args):
    time.sleep(1)
    tid = threading.current_thread()
    print(f"{tid}, {args}")

tasks = list(range(10))
threads = []
for i in range(4):
    t = threading.Thread(target=worker, args=(tasks[4*i: 4*(i+1)],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"{threading.main_thread()}, all done")
