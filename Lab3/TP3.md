
### 1. Organización dentro de una red local

- **a) Función de la capa de enlace y tipo de comunicación:**
    
    La capa de enlace de datos (Capa 2 del modelo OSI) se encarga de la transferencia confiable de datos a través de un medio físico o enlace directo entre dos nodos de una misma red. Su función principal es organizar los bits en bloques lógicos llamados tramas (_frames_), gestionar el control de acceso al medio (MAC) y proveer detección de errores. Resuelve la comunicación **nodo a nodo** o **local** dentro de una misma red de área local (LAN).

![Trama1](https://github.com/Facujema/Los_CondIPcionales/blob/main/Lab3/res/Pasted%20image%2020260916223004.png)
En la imagen obsevamos claramente que wireshark indentifico los vendors de las placas del PC y router.
Tambien se observa claramente el ethertType.
- **b) Dirección MAC vs. Dirección IP:**
-
    - La **dirección MAC** (Media Access Control) es una dirección física de 48 bits, grabada de fábrica en la tarjeta de red (NIC). Opera en la Capa 2 y su alcance es estrictamente local (dentro de la misma red).

- **c) Trama Ethernet y sus campos principales:**
    
    - **Preámbulo y SFD (Start of Frame Delimiter):** Sincronizan los relojes del emisor y receptor.

    - **Dirección MAC de Destino y Origen:** Identifican físicamente al receptor y al emisor en la red local.

    - **EtherType (o Longitud/Tipo):** Indica qué protocolo de capa de red (Capa 3) viene encapsulado en la carga útil (por ejemplo, IPv4 o IPv6).

    - **Carga Útil (Payload):** Los datos encapsulados que provienen de las capas superiores (generalmente un paquete IP).

    - **FCS (Frame Check Sequence):** Un valor de comprobación (CRC) utilizado para detectar si la trama sufrió corrupción de bits durante el viaje.

- **d) Determinación del protocolo de capa superior:**
	 el campo **EtherType** dentro de la cabecera de la trama Ethernet es el responsable de identificar qué protocolo está encapsulado en el payload. Por ejemplo, el valor hexadecimal `0x0800` indica que transporta un paquete IPv4.
### 2. Análisis de Tráfico Base (Trama Ethernet y Paquete IP)

Para observar cómo se organiza la información en una red local, se capturó tráfico generado por la computadora hacia internet utilizando Wireshark.

**Análisis de las capturas:**

- **Identificación de Dispositivos (Capa 2):** En la cabecera Ethernet II, la MAC de origen `24:26:d6:42:b5:25` (Huawei) y la de destino `d0:50:99:01:b5:a7` (ASRock) indican que, a nivel físico local, el paquete fue enviado desde el router hacia la computadora.
    
- **Direcciones IP (Capa 3):** La cabecera IPv4 muestra que la IP de destino es `192.168.1.6` (IP privada local). La IP de origen corresponde a un servidor externo ubicado en Estados Unidos.
    
- **Diferencia funcional:** Queda en evidencia que las direcciones IP dirigen el tráfico de extremo a extremo (EE.UU. a la PC local), mientras que las direcciones MAC dirigen el tráfico salto a salto (del router a la PC).
    
- **Encapsulamiento:** El campo EtherType con valor `0x0800` en la Capa 2 indica el transporte de un paquete IPv4. A su vez, el campo _Protocol_ de IPv4 con valor `6` indica que transporta un segmento TCP.
### 3. Transporte de información mediante TCP
![paquete](https://github.com/Facujema/Los_CondIPcionales/blob/main/Lab3/res/Pasted%20image%2020260916225025.png)
- **a) Problemas que resuelve TCP:**
    
    Ethernet (Capa 2) e IP (Capa 3) ofrecen un servicio de entrega de "mejor esfuerzo" y sin conexión, lo que significa que los paquetes pueden perderse, llegar desordenados o duplicarse. TCP (Transmission Control Protocol) opera en la Capa de Transporte (Capa 4) y resuelve esto al proporcionar una comunicación **confiable y orientada a la conexión**. Introduce mecanismos para garantizar la entrega íntegra (retransmisiones), el orden secuencial de los datos, el control de flujo (para no saturar al receptor) y el control de congestión (para no saturar la red).

- **b) Campos importantes en el segmento TCP:**

    - **Puertos de Origen y Destino:** Identifican las aplicaciones específicas (procesos) que se están comunicando en los hosts de extremo.

    - **Número de Secuencia:** Permite ordenar los segmentos en el destino y detectar pérdida de datos.

    - **Número de ACK (Acuse de recibo):** Indica el próximo número de secuencia que el receptor espera recibir, confirmando la entrega exitosa de los anteriores.

    - **Banderas (Flags - SYN, ACK, FIN, PSH, etc.):** Controlan el estado de la conexión (establecimiento, transmisión, cierre).

    - **Tamaño de Ventana (Window Size):** Fundamental para el control de flujo; el receptor le dice al emisor cuántos bytes está dispuesto a recibir en ese momento.

- **c) Establecimiento y cierre de conexión en TCP:**
  
    - **Three-way Handshake (Apertura):** Es el proceso para establecer la sesión.

        1. El cliente envía un segmento con el flag **SYN** (Synchronize).

        2. El servidor responde con **SYN-ACK** (reconoce la petición y sincroniza su propio contador).

        3. El cliente responde con un **ACK** finalizando el acuerdo. A partir de aquí, fluyen los datos.

    - **Four-way Handshake (Cierre):** Es el proceso para terminar la conexión de forma ordenada y liberar recursos.

        1. Un nodo (ej. el cliente) envía un flag **FIN** (Finish).

        2. El otro nodo (servidor) responde con un **ACK**.

        3. Cuando el servidor termina de enviar los datos residuales, envía su propio **FIN**.

        4. El cliente responde con el último **ACK** y la conexión se cierra.
            

Para analizar la capa de transporte, se utilizó Packet Sender apuntando a un servidor remoto y se filtró el tráfico en Wireshark para observar el comportamiento de la máquina cliente (`192.168.1.6`).

![Analisis wireshark](https://github.com/Facujema/Los_CondIPcionales/blob/main/Lab3/res/Pasted%20image%2020260916225651.png)

**Análisis del estado de conexión:**

- **Three-way Handshake:** En el paquete N° 1017, el cliente inicia la conexión enviando un segmento con el flag **`[SYN]`**. La apertura de la sesión se consolida en el paquete N° 1059, donde el cliente acusa recibo con un **`[ACK]`** tras recibir la respuesta del servidor.
    
- **Intercambio de Datos:** A lo largo de la conexión, los comandos se envían utilizando la bandera **`[PSH, ACK]`**, indicando que la carga útil debe ser procesada inmediatamente.
    
- **Four-way Handshake:** Tras enviar los comandos, el cliente cierra la sesión en el paquete N° 2956 con los flags **`[FIN, ACK]`**. Finalmente, en el paquete N° 2958 envía el **`[ACK]`** definitivo para cerrar la conexión ordenadamente.
    
- **Conclusión de Seguridad:** Se observa que la carga útil de los paquetes viaja sin cifrar. En redes compartidas, la falta de protocolos seguros permite que cualquier analizador de paquetes intercepte y lea el contenido del tráfico.

 ### 4. Interacción con Servidor Remoto en la Nube

Se estableció una conexión TCP persistente al servidor provisto por la cátedra (`34.136.251.235` en el puerto `5555`) utilizando Packet Sender. Se enviaron comandos terminados en el caracter `\r` y se documentaron las respuestas.


Como se corroboró en el análisis de Wireshark previo, cada comando enviado correspondía a un tamaño específico en bytes en el campo de longitud (Len) de la carga útil TCP (por ejemplo, el paquete N° 1243 de longitud 7 corresponde a los 6 caracteres de "status" más el salto de línea `\r`). Las respuestas obtenidas permiten confirmar la correcta comunicación bidireccional y el cierre exitoso de la práctica.

![envio mensaje con el nombre de grupo](https://github.com/Facujema/Los_CondIPcionales/blob/main/Lab3/res/Pasted%20image%2020260916230207.png)
Enviamos nombre de grupo


![recibo respuesta del servidor](https://github.com/Facujema/Los_CondIPcionales/blob/main/Lab3/res/Pasted%20image%2020260916230217.png)
recibimos respuesta. 

![recibimos respuesta random de servidor](https://github.com/Facujema/Los_CondIPcionales/blob/main/Lab3/res/Pasted%20image%2020260916230059.png)
observamos los chistes que devuelve el servidor  :) 
