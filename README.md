# Taller de programación: Tarea Programada 2

#### M. Sc. Saúl Calderón Ramírez
#### Instituto Tecnológico de Costa Rica,
#### Area de Ingeniería en Computadores.
#### 16 de abril de 2016

El presente trabajo práctico pretende continuar con el estudiante el proceso de análisis, diseño e implementación de un sistema de software orientado objetos, usando estructuras de datos básicas (árbol y listas), además de funciones de entrada salida con archivos, para un fin práctico: la compresión de archivos de texto.

* **Modo de trabajo:** en parejas.
* **Fecha de entrega:** Martes 17 de Mayo del 2016
* **Tipo de entrega:** digital, por medio de la plataforma TEC-digital.

### Parte I
## Motivación
Los sistemas de almacenamiento y comunicación digitales con múltiples propósitos, necesitan optimizar el uso de recursos (energéticos, temporales, de espacio, etc.). Para cumplir con tal objetivo de manera efectiva, desde múltiples disciplinas (ciencias de la computación, ingenieria eléctrica, matemática, etc.) se han formulado múltiples algoritmos para **comprimir y descomprimir** la información contenida en una señal. La compresion de una señal digital (compuesta por 1’s y 0’s) consiste en aplicar algún método que permita disminuir el tamaño original de la señal. Los algoritmos de compresión **sin pérdida** son capaces de aplicar una serie de pasos para construir la señal comprimida, para posteriormente, cuando la señal original necesite ser leída, se descomprima y recupere la señal original completamente idéntica. Los algoritmos de compresión **con pérdida** en cambio, cuando implementan la descompresión de la señal, no logran recuperar al 100 % la señal original. El algoritmo de Huffman a implementar en la presente tarea programada fue propuesto por científico computacional estadounidense David A. Huffman en 1952, como un enfoque de compresión sin pérdida de datos [1].

### Parte II
## Compresión de un archivo de texto: el algoritmo de Huffman
#### 1. Introducción al algoritmo de Huffman
El algoritmo de Huffman fue diseñado para comprimir una señal digital. La señal digital a comprimir está compuesta por un conjunto finito de símbolos, donde cada símbolo está definido por una cadena específica de bits (1’s y 0’s). Así por ejemplo, para el caso de la presente tarea programada, en el que se implementará el algoritmo de Huffman para comprimir **archivos de texto** (de extensión .txt), un símbolo está definido por una **palabra o token**. Para ilustrar el funcionamiento del algoritmo, tomaremos el siguiente texto como ejemplo para ejecutar la compresión con el algoritmo de Huffman:

| lorem ipsum dolor sed amet consectetur ipsum elit sed do lorem dolor incididunt sed labore et dolor amet aliqua do enim ad enim veniam, et nostrud consectetur sed labore nisi ut sed et et lorem consectetur |
| :-------: |

El algoritmo de Huffman busca construir para cada símbolo (en este caso, palabra o «token»), una cadena de bits o código de Huffman, que al reemplazarse por cada «token» correspondiente, reduzca el tamaño total del texto. La codificación de Huffman define entonces un diccionario, donde por cada palabra existirá un código correspondiente. Para construir tal diccionario, el algoritmo de Huffman analiza todo el texto, para construir el **diccionario de frecuencias de aparición, o histograma de tokens**, el cual define una entrada por «token», donde tal «token» constituye la llave, y el valor de tal entrada es definido por el número de veces que el «token» sucede en el texto. Así para el ejemplo, anterior, el histograma de tokens está definido como se ve en el Cuadro 1 :

| **Token** | **número de apariciones** |
| :-------: | :-----------------------: |
| sed | 5 |
| et | 4 |
| lorem | 3 |
| dolor | 3 |
| ipsum | 2 |
| amet | 2 |
| consectetur | 3 |
| elit | 1 |
| do | 2 |
| incididunt | 1 |
| aliqua | 1 |
| nostrud | 1 |
| nisi | 1 |
| labore | 2 |
| ut | 1 |
Cuadro 1: Histograma de «tokens» del texto de ejemplo.

**El algoritmo de Huffman busca generar el código más corto para el símbolo con la mayor cantidad de repeticiones**. Para ello es necesario asegurarse que la codificación de todos los tokens no sea ambigua, es decir, sea posible reconstruir el texto original a partir de la señal codificada. Para ello el algoritmo de Huffman utiliza el árbol binario como estructura de datos. Tal estructura se explica en la sección 1.1.

