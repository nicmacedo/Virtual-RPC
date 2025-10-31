import xmlrpc.client

SERVER = "http://192.168.100.10:8000/RPC2" 
proxy = xmlrpc.client.ServerProxy(SERVER, allow_none=True)

def menu():
    print("\n--- Cliente RPC ---")
    print("1 - Soma")
    print("2 - Multiplicação")
    print("0 - Sair")

if __name__ == "__main__":
    while True:
        menu()
        op = input("Opção: ").strip()

        if op == "0":
            break
        elif op == "1":
            a = int(input("A: "))
            b = int(input("B: "))
            print("Resultado:", proxy.soma(a, b))
        elif op == "2":
            a = int(input("A: "))
            b = int(input("B: "))
            print("Resultado:", proxy.multiplica(a, b))
        else:
            print("Opção inválida.")
