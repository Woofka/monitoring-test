import prometheus_client as prom
import time
import signal


class GracefulShutdown:
    def __init__(self):
        self._status = False

    def set(self):
        self._status = True

    def is_set(self):
        return self._status


GRACEFUL_SHUTDOWN = GracefulShutdown()


def main():
    i = 0
    while not GRACEFUL_SHUTDOWN.is_set():
        time.sleep(1)
        counter.inc()
        i += 1
        print(i)


def graceful_shutdown():
    GRACEFUL_SHUTDOWN.set()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, GRACEFUL_SHUTDOWN.set)
    signal.signal(signal.SIGTERM, GRACEFUL_SHUTDOWN.set)

    counter = prom.Counter('test_counter', 'Test counter')

    prom.start_http_server(8000)
    main()
