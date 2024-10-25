import random
import socket
import time
import threading


class Informacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def empacota(self):
        """Empacota a informação em uma string para enviar via socket."""
        return f"{self.tipo}:{self.valor}"


# Tipos de informação definidos no enunciado
TIPOS_INFORMACAO = {
    1: "Esportes",
    2: "Novidades da Internet",
    3: "Eletrônicos",
    4: "Política",
    5: "Negócios",
    6: "Viagens",
}


def gerador_informacao(
    tipo, min_valor, max_valor, tmin, tmax, difusor_ip, difusor_port
):
    # Criação do socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Gerar um valor aleatório entre min_valor e max_valor
        valor = random.randint(min_valor, max_valor)
        info = Informacao(tipo, valor)

        # Empacota e envia para o difusor
        mensagem = info.empacota().encode("utf-8")
        sock.sendto(mensagem, (difusor_ip, difusor_port))

        print(f"Informação enviada: {info.tipo} - Valor: {info.valor}")

        # Dorme por um tempo aleatório entre tmin e tmax (em milissegundos)
        dorme = random.uniform(tmin, tmax) / 1000  # Converte para segundos
        time.sleep(dorme)


# Exemplo de uso:
# gerador_informacao(tipo=1, min_valor=10, max_valor=50, tmin=1000, tmax=5000, difusor_ip='localhost', difusor_port=12345)


def iniciar_geradores(
    qtd_geradores, tipos, min_valor, max_valor, tmin, tmax, difusor_ip, difusor_port
):
    threads = []
    for i in range(qtd_geradores):
        tipo = random.choice(tipos)  # Escolhe um tipo aleatoriamente
        thread = threading.Thread(
            target=gerador_informacao,
            args=(tipo, min_valor, max_valor, tmin, tmax, difusor_ip, difusor_port),
        )
        threads.append(thread)
        thread.start()

    # Espera todas as threads terminarem (teoricamente, elas rodarão indefinidamente)
    for thread in threads:
        thread.join()


# Exemplo de uso com dois geradores
iniciar_geradores(
    qtd_geradores=2,
    tipos=[1, 2, 3],
    min_valor=10,
    max_valor=100,
    tmin=1000,
    tmax=5000,
    difusor_ip="localhost",
    difusor_port=12345,
)
