1. **b)** A partir del gráfico, identificamos la periodicidad espacial de la onda y aplicamos la relación fundamental de la propagación electromagnética.

* **Longitud de onda:** $\lambda = 60\text{ mm} = 0{,}06\text{ m}$
* **Frecuencia ($f$):**
  * **Fórmula:** $c = \lambda \cdot f \implies f = \frac{c}{\lambda}$
  * **Datos:**
    * Velocidad de la luz: $c = 3 \times 10^8\text{ m/s}$
    * Longitud de onda: $\lambda = 0{,}06\text{ m}$

$$
f = \frac{3 \times 10^8\text{ m/s}}{0{,}06\text{ m}} = 5\text{ GHz}
$$

c) 
La onda se puede clasificar dentro del grupo de lo que se denomina **Microondas** y corresponde a la banda **SHF** (*Super Alta Frecuencia*) la cual está definida por ITU como la banda 10. Este grupo abarca frecuencias en el rango de **3 a 30 GHZ**.


d)  
* Routers y puntos de acceso Wi-Fi
* Equipos de enlace punto a punto.

Un ejemplo puede ser el Router TP-Link Archer C80 AC1900 que trabaja bajo el estándar Wi-Fi 5 (802.11ac) en la frecuencia de 5 GHZ.


e)
El fenomeno representado es el de **Atenuación**. Esta suele seguir un decaimiento exponencial con respecto a la distancia.



f)
Sí. De hecho, las señales en la banda de 5 GHz sufren mayor atenuación por la distancia y absorción de materiales que las frecuencias más bajas (como 2,4 GHz). 
Una experiencia cotidiana puede ser que al moverse a una habitación lejana del router la señal Wi-Fi pierde intencidad ocacionando disminución de la velocidad.

g)

* Telefonía celular: Sí. Las ondas que viajan desde la antena de celular hasta el teléfono sufren atenuación por la distancia, la atmósfera y las estructuras urbanas (edificios, paredes).
* Cable coaxial: Sí. La señal eléctrica pierde potencia al desplazarse debido a la resistencia eléctrica del conductor metálico y las pérdidas dieléctricas del cable.
* Fibra óptica: Sí. Aunque su atenuación es extremadamente baja comparada con los cables de cobre o el aire, los pulsos de luz sufren pérdidas de intensidad debido a la absorción del material y la dispersión Rayleigh en trayectos largos.

2.
    a)

* Según su direccionalidad: Transmisión unidireccional, ya que la información fluye exclusivamente desde el módulo emisor hacia el módulo receptor.
* Según sus características temporales: Transmisión Síncrona, debido a que se envía una señal de reloj (clock) dedicada a través de una línea independiente para sincronizar la lectura de los bits en el receptor.
* Modo de transmisión: Transmisión en Serie, puesto que los bits de datos se envían de forma secuencial, uno detrás de otro, sobre una única línea de transmisión.

b)
No. Ya que este modelo representa una transmisión **Simplex** y para ser bidireccional se necesitaría del modelo **Half Duplex** o **Full Duplex**. Para mejorar la velocidad se podría eliminar la linea física del clock embebiendolo dentro de la misma señal de datos.

c)
La cuarta letra, o caracter, de nuestro grupo es "_". En código ASCII corresponde a 0x5F, su equivalente en binario 0b01011111

d) 
La señal debería ser medida en el flanco descendente del clock, ya que para ese momento, el voltaje habría pasado el estado de transición, tomando un valor estable.
