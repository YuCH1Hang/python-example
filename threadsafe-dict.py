#!/usr/bin/env python3

import threading

class ThreadSafeDict(dict) :
    def __init__(self, * p_arg, ** n_arg) :
        dict.__init__(self, * p_arg, ** n_arg)
        self._lock = threading.Lock()

    def __enter__(self) :
        self._lock.acquire()
        return self

    def __exit__(self, type, value, traceback) :
        self._lock.release()

if __name__ == '__main__' :

    u = ThreadSafeDict()
    with u as m :
        m[1] = 'foo'
    print(u)