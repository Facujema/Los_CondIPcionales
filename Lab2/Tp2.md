# Respuesta al Punto 1 – Trabajo Práctico N°2

## a) ¿Qué fenómeno físico se está representando en la figura? ¿Cuáles son las características principales del mismo?

La figura muestra una onda electromagnética (señal de radio) propagándose desde un barco hacia un satélite. La onda se representa como una sinusoide cuya **longitud de onda disminuye** (las crestas se comprimen) a medida que se acerca al satélite. Esto representa el **efecto Doppler** (o desplazamiento Doppler).

**Características principales:**

- Es un fenómeno ondulatorio que ocurre cuando existe **movimiento relativo entre el emisor y el receptor** de una onda.
- La frecuencia percibida por el receptor cambia: si el emisor se acerca, la frecuencia aparente aumenta; si se aleja, disminuye.
- Para ondas electromagnéticas, el desplazamiento Doppler es proporcional a la frecuencia de la portadora: a mayor frecuencia, mayor desplazamiento absoluto.
- En la figura, el barco se acerca al satélite, por lo que el satélite recibe una frecuencia **mayor** que la emitida por el barco.
- Es un fenómeno relevante en comunicaciones inalámbricas móviles y satelitales, donde los equipos están en movimiento.

---

## b) Recordando las bandas de transmisión vistas en el TP01: ¿A qué tipos de transmisión afecta más este fenómeno? ¿Cuáles son más resilientes al mismo?

- **Afecta más a:**
  - **Transmisiones inalámbricas de alta frecuencia** (UHF, SHF, EHF), como microondas, radioenlaces, comunicaciones satelitales, WiFi, 4G/5G, porque el desplazamiento Doppler es proporcional a la frecuencia de la portadora. En bandas milimétricas (mmWave) el efecto es especialmente notorio.
  - **Sistemas con modulaciones sensibles a la frecuencia**, como QAM de alto orden, OFDM, o modulaciones coherentes, que requieren una frecuencia de portadora muy estable.

- **Son más resilientes:**
  - **Transmisiones guiadas** (fibra óptica, cable coaxial, par trenzado), ya que no existe movimiento relativo entre emisor y receptor en el medio físico.
  - **Transmisiones de baja frecuencia** (VLF, LF, MF), donde el desplazamiento Doppler absoluto es pequeño.
  - **Sistemas con modulación robusta**, como FSK (modulación por desplazamiento de frecuencia) o técnicas de **espectro ensanchado** (DSSS, FHSS), que toleran pequeñas variaciones de frecuencia.
  - **Receptores con ecualización Doppler o corrección de frecuencia** (común en LTE/5G), que estiman y compensan el desplazamiento.

---

## c) Investigar: ¿Cuáles son las razones por las cuales no se debe encender el celular arriba de un avión? ¿Tiene algo que ver el fenómeno descrito en los puntos anteriores?

Las razones principales son:

1. **Interferencia electromagnética** con los sistemas de navegación y comunicación de la aeronave (radioaltímetros, ILS, VOR, etc.). El celular emite señales de radio en bandas que pueden solaparse o interferir con los equipos críticos del avión.
2. **Ráfagas de transmisión de alta potencia**: al volar, el celular intenta conectarse a múltiples estaciones base terrestres, generando ráfagas que pueden saturar los enlaces ascendentes y causar interferencia en la red celular.
3. **Efecto Doppler**: el avión se mueve a alta velocidad, por lo que las señales del celular experimentan desplazamientos Doppler significativos. Esto degrada la calidad de los enlaces y puede contribuir a interferencias con los receptores de a bordo.

**Relación con el fenómeno descrito:** Sí, el efecto Doppler está involucrado. Durante el vuelo, el celular se mueve a gran velocidad, lo que provoca variaciones de frecuencia (Doppler) en las señales que emite y recibe. Esto puede afectar las comunicaciones con las torres terrestres y, en cierta medida, generar interferencias. Sin embargo, la razón principal de la prohibición es la **interferencia electromagnética intencionada/no intencionada** con los sistemas críticos de la aeronave, más que el efecto Doppler en sí mismo. Las aeronaves modernas suelen estar blindadas, pero las regulaciones de seguridad mantienen la restricción para minimizar cualquier riesgo.


# Respuesta al Punto 2 – Trabajo Práctico N°2

## a) ¿Qué fenómeno físico se está representando en la figura? ¿Cuáles son las características principales del mismo?

La figura muestra una onda electromagnética (señal de radio) que se propaga desde una torre transmisora hacia un teléfono móvil. En el trayecto, la señal atraviesa una zona donde se encuentra una persona con un dispositivo (posiblemente una fuente de ruido o interferencia). La onda presenta una **degradación y distorsión** en el punto donde interactúa con ese obstáculo o fuente.

El fenómeno representado es la **interferencia electromagnética (EMI)** o **ruido electromagnético**, que es una perturbación no deseada que se superpone a la señal útil. También puede interpretarse como una **degradación por obstáculos (atenuación / difracción)** que distorsiona la forma de onda.

**Características principales:**

- Es un fenómeno **aleatorio** e impredecible: el ruido o la interferencia varía en el tiempo y en el espacio.
- Puede ser **aditivo**: se suma a la señal original, lo que modifica su amplitud, fase o forma de onda.
- Puede ser de dos tipos:
  - **Ruido continuo** (ruido blanco térmico): afecta a todo el ancho de banda de manera uniforme.
  - **Ruido impulsivo** (ráfagas): son picos de corta duración y alta amplitud, que causan distorsiones puntuales como las que parecen observarse en la figura.
- El efecto principal es la **reducción de la relación señal/ruido (SNR)** en el receptor, lo que puede provocar errores en la recuperación de la información.
- La presencia de un **obstáculo físico** también puede causar **atenuación** (pérdida de potencia) y **difracción**, lo que distorsiona la señal a nivel espacial.

---

## b) Recordando las bandas de transmisión vistas en el TP01: ¿A qué tipos de transmisión afecta más este fenómeno? ¿Cuáles son más resilientes al mismo?

- **Afecta más a:**
  - **Transmisiones inalámbricas de alta frecuencia** (UHF, SHF, EHF): las ondas con longitudes de onda cortas son más vulnerables a la atenuación por obstáculos y a la interferencia de fuentes cercanas. Además, al tener mayor ancho de banda, captan más ruido térmico (potencia de ruido proporcional al ancho de banda: \(P_{ruido} = kTB\)).
  - **Sistemas con modulaciones de alta eficiencia espectral** (QAM, OFDM): son muy sensibles a distorsiones y ruido, pues requieren una SNR elevada para mantener bajas tasas de error.
  - **Transmisiones analógicas**: el ruido e interferencia se suman directamente a la señal, produciendo degradación perceptible sin posibilidad de corrección.
  - **Equipos de baja potencia** (celulares, sensores IoT): las señales débiles son fácilmente enmascaradas por interferencias.

- **Son más resilientes:**
  - **Transmisiones guiadas** (fibra óptica, cable coaxial, par trenzado blindado): el medio físico está protegido contra interferencias externas y no existe propagación libre.
  - **Transmisiones en bandas bajas** (VLF, LF, MF): las ondas largas difractan mejor alrededor de obstáculos y la potencia de ruido térmico en anchos de banda pequeños es menor.
  - **Sistemas con espectro ensanchado** (DSSS, FHSS): toleran mejor la interferencia y el ruido incidental.
  - **Sistemas digitales con códigos correctores de errores** y **entrelazado** (interleaving): pueden recuperar información incluso en presencia de ráfagas de ruido.
  - **Receptores con diversidad** (antenas múltiples, MIMO) que ayudan a mitigar los efectos del desvanecimiento/interferencia.

---

## c) ¿Qué es la SNR? ¿Tiene algo que ver con el concepto de BER que vimos en el TP01?

- **SNR (Signal-to-Noise Ratio, Relación Señal/Ruido):** es la relación entre la **potencia de la señal útil** y la **potencia del ruido** presente en el canal. Se expresa normalmente en decibeles (dB):

  $[ \text{SNR} = 10 \log_{10}\left(\frac{P_{señal}}{P_{ruido}}\right) \ \ [dB]]$




**3) Resumir brevemente y para ir pensando: ¿Cómo ayudan los sistemas de transmisión digital a detectar y corregir errores producidos por ruido en el canal? ¿Y a compensar cambios en la frecuencia?**

## a) Detección y corrección de errores

Los sistemas de transmisión digital emplean diversas técnicas para garantizar la integridad de la información a pesar del ruido e interferencias del canal:

1. **Detección de errores:**
   - Se agregan **bits de redundancia** a la trama para que el receptor pueda verificar si los datos recibidos son correctos.
   - Los métodos más comunes son:
     - **Paridad (par/impar):** agrega un bit para que el número de unos en la trama sea par o impar.
     - **Checksum:** suma de control (por ejemplo, en IP).
     - **CRC (Cyclic Redundancy Check):** polinomios generadores que detectan errores en ráfagas con alta probabilidad.
   - Si se detecta un error, el receptor puede solicitar retransmisión (protocolos ARQ: Stop-and-Wait, Go-Back-N, Selective Repeat).

2. **Corrección de errores (FEC - Forward Error Correction):**
   - Se agregan bits redundantes que permiten al receptor **reconstruir** los datos originales sin necesidad de retransmisión.
   - Ejemplos:
     - **Códigos de bloque:** Hamming, BCH, Reed-Solomon.
     - **Códigos convolucionales** con decodificación Viterbi.
     - **LDPC (Low-Density Parity-Check) y Turbo códigos**, usados en 5G, DVB, WiFi.
   - Para combatir **ráfagas de errores** se utiliza **entrelazado (interleaving)**: se dispersan los bits de forma que una ráfaga quede repartida y pueda ser corregida.

3. **Protocolos de capa de enlace:**
   - Además de los códigos, se usan **tramas** con números de secuencia y confirmaciones para lograr entrega confiable.

## b) Compensación de cambios en la frecuencia

Los cambios de frecuencia pueden deberse al **efecto Doppler**, **deriva del oscilador** o **desplazamiento de portadora**. Los sistemas digitales los compensan mediante:

1. **Modulaciones robustas:**
   - **FSK** (Frequency Shift Keying) y variantes son menos sensibles a pequeños desplazamientos de frecuencia, ya que la información va en la frecuencia instantánea.
   - **PSK / QAM** requieren una frecuencia de portadora precisa, por lo que se emplean técnicas de **recuperación de portadora**.

2. **Recuperación de portadora (Carrier Recovery):**
   - El receptor estima y corrige el error de frecuencia/fase mediante lazos de seguimiento:
     - **PLL (Phase-Locked Loop):** ajusta continuamente el oscilador local.
     - **Costas Loop:** para modulaciones PSK.
     - **Bucles de decisión (decision-directed).**

3. **Ecualización Doppler:**
   - En sistemas móviles (LTE, 5G), se estima el desplazamiento Doppler usando **señales de referencia (pilotos)** y se corrige en el dominio del tiempo o la frecuencia.
   - En **OFDM**, se utilizan **subportadoras piloto** y un **prefijo cíclico (CP)** para mitigar el ISI y estimar el canal, incluyendo variaciones Doppler.

4. **Sincronización de frecuencia:**
   - Se realizan **estimaciones de offset de frecuencia** (CFO) antes de la demodulación, usando secuencias de preámbulo conocidas.

**En resumen:** los sistemas digitales añaden redundancia para detectar/corregir errores (códigos FEC, CRC, ARQ) y emplean circuitos de recuperación de portadora, ecualizadores y esquemas de modulación robustos para compensar desplazamientos de frecuencia.


# Respuesta al Punto 4 – Trabajo Práctico N°2

## a) ¿Qué significa sincronización en una comunicación digital? Diferencia entre sincronización de bits y sincronización de trama.

**Sincronización digital:** es el proceso mediante el cual el receptor ajusta su reloj/tiempo de muestreo para alinearse con la señal recibida. Sin sincronización, el receptor no sabe cuándo muestrear los símbolos ni dónde comienza/termina cada unidad de datos.

**Sincronización de bits:**
- El receptor necesita determinar los instantes exactos para muestrear cada bit.
- Se logra mediante:
  - Relojes independientes (menos preciso).
  - **Sincronización por transiciones:** el receptor detecta cambios de nivel en la señal para ajustar su reloj.
  - Técnicas como el **PLL** (lazo de seguimiento de fase) o **recovery de clock** usando preámbulos/patrones de entrenamiento.
- Si falla, se producen errores de muestreo (bits corridos o mal interpretados).

**Sincronización de trama:**
- El receptor necesita identificar dónde empieza y dónde termina cada trama (conjunto de bits que constituyen una unidad de datos).
- Se logra mediante:
  - **Preámbulo/sync word:** secuencias conocidas al inicio de la trama (ej. `01111110` en HDLC).
  - **Delimitadores:** campos especiales que marcan el inicio/fin.
  - **Contadores de bytes/bit** o uso de patrones para rellenado (bit stuffing).
- Si falla, el receptor no puede agrupar correctamente los bits en unidades de datos, lo que impide procesar la información.

**Diferencia clave:** la sincronización de bits opera a nivel de símbolo/bit individual, mientras que la sincronización de trama opera a nivel de agrupación de bits en estructuras de datos.

---

## b) ¿Qué es una trama (frame)? ¿Qué diferencias existen entre header, payload y trailer?

**Trama (frame):** es la unidad básica de datos en la capa de enlace. Consiste en una secuencia de bits organizada con estructura definida, que incluye encabezado, datos y tráiler.

| Parte | Función |
|-------|---------|
| **Header (encabezado)** | Contiene información de control: direcciones origen/destino, tipo de protocolo, números de secuencia, flags, etc. Es **metadata** que permite al receptor procesar correctamente el payload. |
| **Payload (carga útil)** | Son los datos reales que se desean transmitir (por ejemplo, un segmento de red). Puede ser de longitud variable, dependiendo del protocolo. |
| **Trailer (tráiler)** | Contiene información de verificación de errores, como el **CRC** o checksum. A veces incluye bits de relleno o delimitadores de fin. Permite al receptor detectar si la trama llegó íntegra. |

**Ejemplo:** en Ethernet, el header incluye MAC destino, MAC origen, tipo; el payload son los datos IP; el trailer incluye el FCS (Frame Check Sequence, CRC-32).

---

## c) ¿Qué función puede cumplir un preámbulo antes de una trama? ¿Es necesariamente parte de la información que se quiere transmitir?

**Función del preámbulo:**
- **Sincronización de reloj:** permite al receptor ajustar su reloj antes de leer los bits.
- **Detección de inicio de trama:** mediante una secuencia de sincronización conocida, el receptor sabe que después vendrá el header.
- **Recuperación de portadora:** en algunos sistemas ayuda a estimar la frecuencia/fase de la señal.
- **Ajuste de ganancia (AGC):** permite que el receptor ajuste la ganancia del amplificador de RF antes de los datos.

**Ejemplo concreto:** en **Ethernet** (IEEE 802.3), antes de cada trama se envía un **preámbulo de 7 bytes** con el patrón `10101010` repetido, seguido de un **byte de delimitación de inicio de trama (SFD)** con el patrón `10101011`.  
- El receptor usa los primeros 7 bytes para sincronizar su reloj y detectar el nivel de señal.  
- El SFD (`10101011`) le indica que el siguiente byte será el primer byte del header (dirección MAC destino).  
- **No es información útil**: el preámbulo no se entrega a las capas superiores, es overhead de la capa física.

**¿Es necesariamente parte de la información que se quiere transmitir?**  
- **No**, el preámbulo no es parte del payload. Es una secuencia de control que pertenece a la estructura de la trama, pero no transmite datos de usuario. Es un costo adicional (overhead) necesario para lograr una correcta recepción.

---

## d) Investigar al menos tres formas mediante las cuales un protocolo puede determinar dónde termina una trama

### 1. Longitud fija (Fixed-length framing)

- Todas las tramas tienen la **misma longitud** en bits o bytes.
- El receptor simplemente cuenta hasta ese número fijo y sabe que la trama terminó. La siguiente trama comienza inmediatamente después.
- **Ventajas:** no se necesita ningún campo extra en el header para indicar longitud; el procesamiento es muy rápido y simple.
- **Desventajas:** si los datos no llenan la trama, se desperdicia espacio (padding). Además, no se pueden transmitir tramas de tamaño variable, lo que es ineficiente para tráfico de longitudes muy dispares.
- **Ejemplo:** **ATM (Asynchronous Transfer Mode)** usa celdas de tamaño fijo de **53 bytes** (5 de header + 48 de payload). El receptor sabe exactamente cuándo termina una celda.

### 2. Campo de longitud (Length field in header)

- El header incluye un **campo numérico** que indica cuántos bytes (o bits) de payload contiene la trama.
- El receptor lee ese campo, calcula el fin de la trama y sabe cuándo debe comenzar a buscar la siguiente.
- **Ventajas:** permite tramas de longitud variable sin desperdiciar espacio; es muy flexible.
- **Desventajas:** el campo de longitud ocupa bits en el header; si el campo se corrompe, el receptor puede perder la sincronización de trama. Además, a veces se requiere un tamaño mínimo de trama (por ejemplo, en Ethernet se agrega padding para llegar a 64 bytes).
- **Ejemplo:** en **Ethernet II** existe un campo `Type/Length` de 2 bytes. En el modo IEEE 802.3, ese campo indica la **longitud del payload** (si el valor es menor que 0x0600). En el modo Ethernet II, ese campo indica el **tipo de protocolo** (por ejemplo, 0x0800 para IPv4). Otro ejemplo: en **PPP** (Point-to-Point Protocol), se puede usar un campo `Length` en algunas variantes (aunque PPP normalmente usa delimitadores).

### 3. Caracteres / secuencias delimitadoras (Delimiter-based framing)

- Se utilizan **patrones especiales** (secuencias de bits o caracteres) para marcar el **inicio** y el **fin** de la trama.
- Para que esos patrones no aparezcan dentro de los datos de forma accidental, se aplica una técnica de **escape/stuffing**:
  - **Bit stuffing:** en protocolos orientados a bits, como **HDLC**, se usa el flag `01111110` como delimitador. Si dentro de los datos aparecen cinco `1` consecutivos, el emisor inserta un `0` después de ellos. Así, el flag original solo aparece como delimitador.
  - **Byte stuffing:** en protocolos orientados a bytes, como **PPP**, se usa el carácter `0x7E` como flag. Si un byte de datos es igual a `0x7E`, se reemplaza por `0x7D 0x5E` (escape + XOR). El receptor invierte el proceso.
- **Ventajas:** no se necesita conocer la longitud de antemano; es ideal para canales asíncronos y tramas de longitud variable.
- **Desventajas:** el stuffing agrega overhead (bits/bytes extra) que debe ser eliminado en el receptor; si el patrón delimitador se pierde por ruido, la trama se pierde y se necesita re-sincronización.

**Ejemplo de bit stuffing en HDLC:**  
Supongamos que los datos son `01111110` (que es el patrón de flag). Para evitar que se confunda con el delimitador, el emisor inserta un `0` después de cinco `1` consecutivos:

- Datos originales: `0 1 1 1 1 1 1 0`
- Se inserta un `0` después del quinto `1` consecutivo (después del bit 6): `0 1 1 1 1 1 0 1 0`

El receptor recibe `011111010`, elimina el `0` insertado y reconstruye los datos originales `01111110`. El flag real (sin stuffing) solo aparece delimitando la trama.
