# Arduino 2.0
## Sensori e protocolli di comunicazione

Giorgio Colomban
`gcolomban@gmail.com`

![Logo POuL](lib/img/logo-text-white.svg)

----

# Cos'è un sensore?

> Un sensore è un componente che fisicamente effettua la trasformazione della grandezza
> d'ingresso in un segnale di altra natura
> -- Wikipedia

---

# Tipologie di sensori

Esistono due diversi tipologie di sensori:

* __Sensori analogici__
* __Sensori digitali__

----

## Sensori analogici

I __sensori analogici__ leggono un valore di __tensione proporzionale__ alla grandezza misurata.

In Arduino (ed altri microcontrollori simili) il valore di tensione viene letto tra il __GND__ ed il __pin di output__ del sensore tramite l'utilizzo di un __pin analogico__ del microcontrollore (guardare il datasheet per vedere quanti e quali sono i pin analogici)

---

## Sensori analogici
### Analog to Digital Converter

La conversione dal valore di tensione ad un valore digitale viene effettuata tramite un __ADC__ (Analog to Digital Converter), che permette di discretizzare la tensione (tipicamente compresa tra 0 e 5 volt) su __2^n livelli__, dove `n` è il __numero di bit__ dell'ADC (10, nel caso di un Arduino Uno, che quindi può discretizzare la tensione su 1024 livelli)

---

## Sensori analogici
### Comunicazione

Per utilizzare un sensore è necessario anzitutto collegarlo al circuito, __seguendo le specifiche del datasheet__

Per leggere il valore di tensione trasmesso dal sensore analogico con l'IDE Arduino basta usare la funzione `analogRead(inputPin)`

----

## Sensori digitali

I __sensori digitali__ comunicano con la scheda tramite __protocolli standard__, basati su __bus__, __indirizzi__ ed __interrupts__.

L'utilizzo di sensori digitali permette di trasmettere __dati già elaborati__ lungo lo stesso "filo di comunicazione" (bus).

---

## Sensori digitali
### Comunicazione

Per comunicare con un sensore digitale va scaricata ed installata la libreria dedicata, che fornirà tutte le funzioni necessarie ad acquisire i dati letti dal sensore.

Se non esiste una libreria per un sensore, sarà necessario implementarla (ad esempio con la libreria __wire.h__ per i sensori I2C)

----

# Protocolli di comunicazione

Fortunatamente, i principali standard di comunicazione per sensori sono solo 3:

* __UART__
* __SPI__
* __I2C__

---

## Protocolli di comunicazione
### UART

---

## Protocolli di comunicazione
### SPI

---

## Protocolli di comunicazione
### I2C

----

# Fonti e risorse utili

* [Slides](https://slides.poul.org/2018/corsi-arduino/sensori/) di Raffaele Di Campli - corsi Arduino 2018
* [Tutorial](https://www.deviceplus.com/how-tos/arduino-guide/arduino-communication-protocols-tutorial/) esteso sui protocolli di comunicazione

----

# Grazie per l'attenzione!
![creative commons](lib/img/creativecommons-by-nc-sa.svg)
