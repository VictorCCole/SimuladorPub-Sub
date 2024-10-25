import socket


def consumidor(tipo_desejado):
    # Conecta ao Difusor via TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(("localhost", 54321))

    # Envia o tipo desejado
    cliente_socket.send(str(tipo_desejado).encode("utf-8"))

    # Recebe informações do tipo desejado
    while True:
        mensagem = cliente_socket.recv(1024).decode("utf-8")
        print(f"Consumidor recebeu: {mensagem}")


# Exemplo de execução: Consumidor quer receber tipo 2
consumidor(3)
