import socket

HOST = "::1"
PORT = 5000

servidor = socket.socket(
    socket.AF_INET6,
    socket.SOCK_STREAM
)

servidor.bind((HOST, PORT))
servidor.listen(1)

print(f"Servidor IPv6 escuchando en [{HOST}]:{PORT}")

conexion, direccion = servidor.accept()

print("Cliente conectado:", direccion)

mensaje = conexion.recv(1024).decode("utf-8")

print("Mensaje recibido:", mensaje)

conexion.sendall(
    b"Conexion establecida correctamente. Mensaje recibido por medio de IPv6 con exito."
)

conexion.close()
servidor.close()