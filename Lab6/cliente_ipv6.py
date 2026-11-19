import socket

HOST = "::1"
PORT = 5000

cliente = socket.socket(
    socket.AF_INET6,
    socket.SOCK_STREAM
)

cliente.connect((HOST, PORT))

mensaje = "Probando cambios de mensaje para corroborar funcionamiento con IPv6."
cliente.sendall(mensaje.encode("utf-8"))

respuesta = cliente.recv(1024).decode("utf-8")
print("Respuesta del servidor:", respuesta)

cliente.close()