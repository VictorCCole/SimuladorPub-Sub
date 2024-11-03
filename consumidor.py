import socket

def consumidor(tipo_desejado):
    # Define o endereço e porta do Difusor
    host = 'localhost'
    porta = 54321

    # Cria o socket TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Conecta ao Difusor
        cliente_socket.connect((host, porta))
        print(f"Conectado ao Difusor na porta {porta}")

        # Envia o tipo de informação desejado ao Difusor
        cliente_socket.send(str(tipo_desejado).encode('utf-8'))
        print(f"Tipo de informação solicitado: {tipo_desejado}")

        # Recebe informações do Difusor
        while True:
            mensagem = cliente_socket.recv(1024)
            if not mensagem:
                break
            print(f"Mensagem recebida: {mensagem.decode('utf-8')}")

    except ConnectionRefusedError:
        print("Não foi possível conectar ao Difusor. Verifique se ele está rodando e a porta está correta.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        cliente_socket.close()
        print("Conexão com o Difusor encerrada.")

# Exemplo de uso: Consumidor deseja receber informações de tipo 2 (por exemplo, "Novidades da Internet")
if __name__ == "__main__":
    consumidor(2)
