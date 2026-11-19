# Laboratorio 5 - Comunicaciones de Datos

## 1.  a) ¿Qué es ICMP y para qué se usa? ¿Transporta datos de aplicaciones como lo hacen TCP o UDP?
ICMP (Internet Control Message Protocol) es un protocolo de control utilizado en redes IP para comunicar errores, informar condiciones de la red y realizar tareas de diagnóstico.
Entre sus principales funciones se encuentran:
- Notificar errores: por ejemplo, cuando un destino es inalcanzable.
- Realizar diagnósticos: mediante herramientas como ping, que permiten comprobar la conectividad entre dispositivos.
- Informar condiciones de la red: por ejemplo, cuando un paquete agota su tiempo de vida (TTL).
ICMP no está diseñado para transportar datos de aplicaciones como TCP o UDP. Su función principal es intercambiar mensajes de control y diagnóstico. Aunque puede incluir datos en sus mensajes, no proporciona un servicio general de transporte entre aplicaciones.

## 1. b) ¿Qué relación tiene con IP? ¿Viaja dentro de IP, al lado de IP o debajo de IP? ¿Cómo sabe el receptor que el contenido de un paquete IP es ICMP?
ICMP es un protocolo estrechamente relacionado con IP, ya que se utiliza para comunicar información sobre el funcionamiento de la red.
Los mensajes ICMP viajan encapsulados dentro de paquetes IP, es decir, forman parte de la carga útil (payload) del paquete IP.
La encapsulación es la siguiente:

<p align="center">
  <img src="img/2_0.png" alt="">
</p>

## 1. c) ¿Qué hace ping? ¿Qué son un Echo Request y un Echo Reply? ¿Qué campos de ICMP permiten distinguirlos?
ping es una herramienta de diagnóstico que permite comprobar si existe conectividad IP entre dos dispositivos de una red.
Para hacerlo, utiliza dos tipos de mensajes ICMP:
      -Echo Request (tipo 8): mensaje enviado por el dispositivo de origen para solicitar una respuesta.
      -Echo Reply (tipo 0): mensaje enviado por el dispositivo de destino en respuesta al Echo Request.

<p align="center">
  <img src="img/2_0.png" alt="">
</p>

Los campos principales de ICMP que permiten distinguir ambos mensajes son:

| Campo | Echo Request | Echo Reply |
|  ---  |      ---     |     ---    |
|  Type |   8  | 0 |
|  Code |   0  | 0 |
| Identifier | identifica la solicitud | Se mantiene |
| Sequence Number | identifica el número de solicitud | Se mantiene |

El campo Type es el que permite distinguir directamente los dos mensajes.
Además, ping utiliza el tiempo transcurrido entre el envío del Request y la recepción del Reply para calcular el tiempo de ida y vuelta, denominado RTT (Round-Trip Time).

## 1. d) ¿Qué información mínima contiene un mensaje ICMP de tipo Echo?


| Campo | Tamaño | Función |
| --- | --- | --- |
| Type | 1 byte | Indica si es Request (8) o Reply (0). |
| Code | 1 byte | Para los mensajes Echo tiene valor 0. |
| Checksum | 2 bytes | Permite detectar errores en el mensaje ICMP. |
| Identifier | 2 bytes | Permite asociar las respuestas con sus solicitudes. |
| Sequence Number | 2 bytes | Permite identificar y ordenar las solicitudes enviadas. |

El encabezado ICMP Echo tiene un tamaño de 8 bytes.

El mensaje también puede contener un campo de datos o payload, de longitud variable, que normalmente utiliza ping para enviar información de prueba. El Echo Reply devuelve esos mismos datos.
Conclusión: ICMP es un protocolo de control y diagnóstico que funciona encapsulado en IP. La herramienta ping utiliza mensajes Echo Request y Echo Reply para verificar conectividad y medir tiempos de respuesta. Estos mensajes se identifican principalmente mediante el campo Type y contienen un encabezado mínimo de 8 bytes.


<p align="center">
  <img src="img/2_0.png" alt="">
</p>

## ipconfig

<p align="center">
  <img src="img/2_0.png" alt="">
</p>

## Echo request y Wireshark


| Capa | Dirección/Identificador origen | Dirección/identificador destino | ¿Qué campo indica qué protocolo viene "adentro"? |
| :---: | :---: | :---: | :---: |
| Ethernet II | **1C:1B:0D:E9:4E:96** | **3A:17:E1:C2:D3:1D** | **0x0800 (IPv4)** |
| Internet Protocol Version 4 | **192.168.0.118** | **8.8.8.8** | **1 (ICMP)** |
| Internet Control Message Protocol | **Identifier = 0x0001, Sequence = 71** | **No tiene dirección de destino propia.** | **Type = 8, Code = 0** |
| Datos / payload | **No tiene origen propio.** | **No tiene origen propio.** | **No hay otro protocolo; son datos del ping.** |

## a)	Dirección MAC destino del Echo Request
La dirección MAC destino del Echo Request enviado a 8.8.8.8 no corresponde al servidor de Google, sino a la interfaz del gateway de nuestra red local, cuya dirección IP es 192.168.0.1.
Las direcciones MAC permiten identificar interfaces dentro de un enlace de red local, mientras que las direcciones IP permiten identificar el origen y el destino de los paquetes a través de múltiples redes. Las direcciones MAC pueden cambiar en cada salto del recorrido, mientras que las direcciones IP de origen y destino normalmente se mantienen.

## b)	Request y Reply. Entre los paquetes 731 (request) y 739 (reply) se invierten las MAC de origen y destino, y también las IP (192.168.0.118 ↔ 8.8.8.8).
La MAC de origen del Reply es la del gateway, porque es el equipo que nos entrega esa trama en nuestra red. En ICMP, el campo Type cambia de 8 (Echo Request) a 0 (Echo Reply), mientras que el identificador y el número de secuencia permanecen iguales.
El identificador y el número de secuencia se mantienen porque permiten relacionar cada Echo Reply con el Echo Request que lo originó, incluso cuando se realizan múltiples solicitudes consecutivas.

## c)	El payload de ping se encuentra dentro del mensaje ICMP, después de su encabezado de 8 bytes. En nuestra captura de Wireshark, específicamente en el paquete 739 (Echo Reply), se observa un payload de 32 bytes, que contiene la siguiente secuencia de caracteres ASCII: abcdefghijklmnopqrstuvwabcdefghi.
El Echo Reply devuelve los mismos datos enviados en el Echo Request, permitiendo comprobar que la información recibida coincide con la enviada. En nuestro caso, el paquete 739 corresponde a la respuesta del paquete 731.
El contenido del payload puede variar según el sistema operativo y la implementación de ping. Por ejemplo, Windows utiliza normalmente 32 bytes de datos, mientras que Linux suele utilizar 56 bytes por defecto. Esto demuestra que ICMP no establece un contenido fijo para los datos del mensaje Echo, por lo que cada implementación puede utilizar distintos tamaños y patrones.

## d)	La diferencia entre ambos TTL se debe a que los dispositivos pueden utilizar distintos valores iniciales y a que los routers disminuyen el TTL durante el recorrido.
Por lo tanto, el TTL recibido depende tanto de su valor inicial como de la cantidad de saltos realizados.

## e) Trama Ethernet: 74 bytes
        └── Cabecera Ethernet II: 14 bytes
            └── Paquete IPv4: 60 bytes
                ├── Cabecera IPv4: 20 bytes
                └── Mensaje ICMP: 40 bytes
                    ├── Cabecera Echo Request: 8 bytes
                    └── Datos del ping: 32 bytes

## 2. a)  ¿Qué problema resuelve ARP? ¿En qué capa lo ubicarían y por qué es discutible?
ARP (Address Resolution Protocol) es un protocolo que permite obtener la dirección MAC asociada a una dirección IPv4 dentro de una red local.
Su función principal es resolver el problema de cómo enviar una trama Ethernet cuando se conoce la dirección IP del siguiente dispositivo, pero se desconoce su dirección MAC.
ARP suele ubicarse en la capa de enlace de datos (capa 2 del modelo OSI), ya que sus mensajes se transportan directamente en tramas Ethernet, sin utilizar un encabezado IP.
Sin embargo, su clasificación es discutible porque relaciona direcciones de dos capas diferentes: las direcciones IP de la capa de red (capa 3) y las direcciones MAC de la capa de enlace (capa 2). Por este motivo, también se considera un protocolo que funciona entre ambas capas.

## 2. b) ¿Qué es un ARP Request y un ARP Reply? ¿A quién se envía cada uno?
ARP utiliza dos tipos principales de mensajes para resolver direcciones:
- ARP Request: es una solicitud que envía un dispositivo cuando necesita conocer la dirección MAC asociada a una dirección IPv4. Generalmente se envía mediante broadcast, utilizando la dirección MAC FF:FF:FF:FF:FF:FF, para que todos los dispositivos del segmento local puedan recibirla.
- ARP Reply: es la respuesta enviada por el dispositivo que posee la dirección IP solicitada. Contiene su dirección MAC y normalmente se envía mediante unicast, directamente al dispositivo que realizó la solicitud.
Por ejemplo, si nuestra computadora (192.168.0.118) necesita conocer la MAC del gateway (192.168.0.1), el intercambio sería:

```text
PC (192.168.0.118)
|
├── ARP Request (Broadcast)
|   "¿Quién tiene 192.168.0.1?"

|               |
|               ▼
|            Gateway
|          192.168.0.1

|               |
└── ARP Reply (Unicast)
    "192.168.0.1 tiene la MAC
     3A:17:E1:C2:D3:1D"
```
La dirección MAC indicada es la que observamos como destino en tu captura ICMP anterior; todavía debemos confirmar su asociación con el gateway mediante la caché ARP.

## 2. c)¿Qué es la caché ARP y por qué existe?
La caché ARP es una tabla que mantiene el sistema operativo y que almacena temporalmente las asociaciones entre direcciones IPv4 y direcciones MAC de los dispositivos de la red local.

Su objetivo es evitar que la computadora tenga que realizar una nueva solicitud ARP cada vez que necesita comunicarse con un dispositivo cuya dirección MAC ya conoce.

Esto permite reducir el tráfico broadcast y mejorar la eficiencia de la comunicación.

Las entradas de la caché ARP pueden actualizarse o eliminarse después de cierto tiempo, evitando mantener indefinidamente asociaciones que podrían dejar de ser válidas.

## 2. d) Tengo la IP de una máquina de mi red local. ¿Cómo sé a qué dirección MAC debo enviarle la trama?
Primero, la computadora consulta su caché ARP para verificar si ya conoce la dirección MAC asociada a la IP de destino.
Si encuentra una entrada válida, utiliza directamente esa dirección MAC para construir la trama Ethernet.
Si no encuentra la dirección MAC, envía un ARP Request mediante broadcast preguntando qué dispositivo tiene la IP buscada.
El dispositivo que reconoce esa dirección IP responde con un ARP Reply, indicando su dirección MAC. La computadora almacena esta asociación en su caché ARP y utiliza la MAC obtenida para enviar la trama Ethernet.
Este procedimiento permite transformar una dirección IPv4 conocida en la dirección MAC necesaria para comunicarse dentro de la red local.

## 2. e) Ver la caché ARP de su computadora y buscar la entrada del gateway:

<p align="center">
  <img src="img/2_0.png" alt="">
</p>

Sí, la dirección MAC asociada al gateway coincide con la dirección MAC destino observada anteriormente en Wireshark.

## 2. f) Generar tráfico ARP y capturarlo


| Campo | ARP Request (paquete 992) | ARP Reply |
| --- | --- | --- |
| MAC destino (Ethernet) | `FF:FF:FF:FF:FF:FF` | Pendiente |
| MAC origen (Ethernet) | `1C:1B:0D:E9:4E:96` | Pendiente |
| Opcode | `1` (Request) | `2` (Reply) |
| Sender MAC address | `1C:1B:0D:E9:4E:96` | Pendiente |
| Sender IP address | `192.168.0.118` | Pendiente |
| Target MAC address | `00:00:00:00:00:00` | Pendiente |
| Target IP address | `192.168.0.253` | Pendiente |
