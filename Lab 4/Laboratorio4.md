# Laboratorio 4 - Comunicaciones de Datos

## 1.  a) Clasificación de las redes según su alcance

Las redes pueden clasificarse según el área geográfica o el alcance que cubren. Están clasificadas de la siguiente forma: 
**<div align="center">**PAN → LAN → MAN → WAN**</div>**
  
  - PAN — Personal Area Network: Red de Área Personal. Es una red de alcance muy reducido alrededor de una persona. Un ejemplo típico es una conexión Bluetooth entre dispositivos personales.
  - LAN — Local Area Network: Red de Área Local.Abarca una zona relativamente limitada, como una oficina, un edificio o un campus. Se caracteriza por altas velocidades de transmisión y baja latencia. Cisco define una LAN como una colección de dispositivos conectados en una ubicación física limitada. 
  - MAN — Metropolitan Area Network: Red de Área Metropolitana. Cubre un área geográfica más amplia que una LAN, como una ciudad o un área metropolitana. Se utiliza para interconectar varias LANs dentro de la misma región. IBM la describe como una red mayor que una LAN pero menor que una WAN.
  - WAN — Wide Area Network: Red de Área Amplia. Se extiende sobre grandes distancias geográficas, como países o continentes. Internet es el ejemplo más conocido de una WAN, permitiendo la comunicación entre redes locales y metropolitanas a nivel global.
  
## 1.  b) VLAN: Virtual Local Area Network (Red de Área Local Virtual). 

Una VLAN permite dividir lógicamente una red física en diferentes redes independientes.<div align="center">

                 SWITCH
                │
                ┌─────────────┼─────────────┐
                │             │             │
              VLAN 10       VLAN 20       VLAN 99
              Turistas      Business       Admin
</div>
Aunque todos los dispositivos estén conectados físicamente al mismo switch, las VLAN permiten separarlos lógicamente. Cisco describe las VLAN como una forma de segmentar la red y agrupar dispositivos de acuerdo con necesidades administrativas.

_¿Cómo se clasifican las VLAN?_
Según su utilización se pueden diferenciar distintos tipos de VLAN:
*   Data VLAN: tráfico de usuarios.
*   Voice VLAN: tráfico de voz/telefonía IP.
*   Management VLAN: administración de dispositivos.
*   Native VLAN: VLAN cuyo tráfico se transmite sin etiqueta en un trunk 802.1Q.
   
## 1. c) IEEE 802.1Q 
Es el estándar utilizado para identificar VLANs mediante etiquetado de tramas Ethernet, especialmente cuando varias VLAN atraviesan un enlace trunk.
Un enlace trunk es un enlace entre dispositivos de red que permite transportar tráfico de varias VLAN simultáneamente por un mismo cable/enlace físico.El trunk permite que por el mismo cable entre Switch 1 y Switch 2 viajen las VLAN 10, 20, 99, etc. ¿Cómo sabe el switch a qué VLAN pertenece cada trama? **Mediante 802.1Q.**. Cuando una trama atraviesa un enlace trunk, el switch puede agregarle una etiqueta (tag) que indica a qué VLAN pertenece.

## 1. d) Tagging
Es el proceso mediante el cual se agrega, a una trama Ethernet, información que permite identificar la VLAN a la que pertenece. El switch receptor utiliza ese identificador para saber que la trama pertenece a VLAN 10.
El estándar 802.1Q inserta un tag de 4 bytes en la trama Ethernet; la VLAN nativa es una excepción habitual, ya que su tráfico puede circular sin tag por el trunk.

## 2. a) Packet Tracer.

<p align="center">
  <img src="img/2_0.png" alt="diagrama logico">
</p>

## 2. b) Configuración Inicial.

<p align="center">
  <img src="img/2_1.png" alt="Configuración inicial">
</p>




   

