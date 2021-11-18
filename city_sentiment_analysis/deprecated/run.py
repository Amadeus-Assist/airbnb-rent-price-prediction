import os
import threading
from config import CITY_LIST


def exec_cmd(cmd):
    try:
        print("run {}".format(cmd))
        os.system(cmd)
    except:
        print("Failed {}".format(cmd))


if __name__ == '__main__':

    threads = []
    for city in CITY_LIST:
        cmd = "python main.py \"{}\"".format(city)
        th = threading.Thread(target=exec_cmd, args=(cmd, ))
        # th.start()
        threads.append(th)

    print("Load success.")
    for th in threads:
        # th.setDaemon(True)
        th.start()
