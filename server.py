from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import threading
import time

class MathService:
    def soma(self, a, b):
        print(f"[{threading.current_thread().name}] soma({a}, {b})")
        time.sleep(2)
        return a + b

    def multiplica(self, a, b):
        print(f"[{threading.current_thread().name}] multiplica({a}, {b})")
        time.sleep(2)
        return a * b


class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


if __name__ == "__main__":
    server = ThreadedXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
    server.register_instance(MathService())
    print("Servidor RPC rodando na porta 8000 (multithread)...")
    server.serve_forever()
