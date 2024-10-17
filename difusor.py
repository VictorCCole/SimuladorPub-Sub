import socket


def difusor_teste(porta):
    # Criação do socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("localhost", porta))

    print(f"Difusor escutando na porta {porta}...")

    while True:
        # Recebe a mensagem (tamanho máximo de 1024 bytes)
        mensagem, endereco = sock.recvfrom(1024)
        print(f"Mensagem recebida de {endereco}: {mensagem.decode('utf-8')}")


# Exemplo: Difusor escutando na porta 12345
difusor_teste(12345)
