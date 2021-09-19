#!/usr/bin/env python
import main
import pool

if __name__ == "__main__":
    url = "memory://"
    p = pool.main(url, timeout=2, handle_sigterm=False)
    try:
        main.main(url)
    finally:
        p.stop()