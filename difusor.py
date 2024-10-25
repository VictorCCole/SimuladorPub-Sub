import socket
import threading
from queue import Queue


class Difusor:
    def __init__(self, udp_port, tcp_port):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(("localhost", udp_port))

        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.bind(("localhost", tcp_port))
        self.tcp_socket.listen(5)

        self.filas_info = {tipo: Queue() for tipo in range(1, 7)}
        self.seq_num = 0

    def start(self):
        threading.Thread(target=self.recebe_informacoes).start()
        print("Difusor aguardando conexões de consumidores...")

        while True:
            cliente_socket, _ = self.tcp_socket.accept()
            threading.Thread(
                target=self.atende_consumidor, args=(cliente_socket,)
            ).start()

    def recebe_informacoes(self):
        print("Difusor recebendo informações dos geradores...")
        while True:
            mensagem, _ = self.udp_socket.recvfrom(1024)
            tipo, valor = map(int, mensagem.decode("utf-8").split(":"))
            informacao = {"seq": self.seq_num, "tipo": tipo, "valor": valor}
            self.filas_info[tipo].put(informacao)
            print(f"Recebido do gerador: {informacao}")
            self.seq_num += 1

    def atende_consumidor(self, cliente_socket):
        tipo_desejado = int(cliente_socket.recv(1024).decode("utf-8"))
        print(f"Consumidor conectado e deseja receber tipo: {tipo_desejado}")

        while True:
            if not self.filas_info[tipo_desejado].empty():
                info = self.filas_info[tipo_desejado].get()
                cliente_socket.send(
                    f"{info['seq']}:{info['tipo']}:{info['valor']}".encode("utf-8")
                )
                print(f"Enviado para consumidor: {info}")


if __name__ == "__main__":
    difusor = Difusor(udp_port=12345, tcp_port=54321)
    difusor.start()
