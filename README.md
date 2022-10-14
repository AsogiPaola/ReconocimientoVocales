# ReconocimientoVocales
Proyecto realizado con el fin de diferenciar vocales y genero (masculino/femenino) según las frecuencias, basandose en las frecuencias altas relacionadas generalmente a la voz Feminina y frecuencias bajas ala masculina.
Marco teórico 

El espectrograma es una herramienta primordial en el estudio de la comunicación acústica en vertebrados. Es básicamente una representación visual del sonido donde muestra la variación en energía, es decir, el poder de densidad espectral en los dominios de frecuencia y tiempo. Los espectrogramas permiten explorar de manera visual la variación acústica que se presenta en nuestro sistema de estudio, facilitando la distinción en las diferencias estructurales a pequeñas escalas temporales/espectrales que nuestros oídos no pueden detectar. El espectrograma se divide en tres dimensiones temporal, frecuencial y amplitud de la distribución de energía de una señal, que se pueden observar en la figura 1

<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/1.png" width="280"/>
Figura 1: Dimensiones de un espectrograma 

# Procedimiento 

Este informe se realizó mediante el método analítico y comparativo, ya que con las diversas voces recolectadas se generaron graficas que permiten analizar los diferentes rangos de voz al pronunciar las vocales en español. Se pidió a diferentes personas que pronunciaran las vocales en español una por una, de manera que cada vocal quedara en un solo audio facilitando más adelante su proceso de reconocimiento. 
Captura de datos 

Para la recolección de datos se utilizó Audacity (2), es una aplicación informática multiplataforma libre, que se puede usar para grabación y edición de audio, y la captura de los datos se realizó con un micrófono YN685, con un periodo de muestreo de 44100 con dos canales, los datos recolectados se almacenaron y graficaron en un programa llamado Spyder3 utilizando la librería Soundfile. (3) 

Cuando se obtuvieron las gráficas de las señales se observó que la señal tenía un tiempo en cero hasta que sonaba la voz de la persona, para eliminar este tiempo cero los audios se recortaron uno por uno con el programa Audacity. 

Al sacar las FFT de las señales, observamos que las señales poseían canal estéreo, es decir, dos matrices; para aplicar la FFT se necesita que el audio sea mono, así que se realizó la conversión de estéreo a mono a través de la plataforma Audacity.  

 
Análisis 

A continuación, se observarán las gráficas de frecuencia que genera una voz masculina al decir las vocales, en la figura 2, en este caso se muestran las gráficas del sujeto N-1.

<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sA.png" align="left" width="380"/> 
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sE.png" align="left" width="380"/> 
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sI.png" align="left" width="380"/> 
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sO.png" align="left" width="380"/> 
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sU.png" width="380"/>

Figura 2: Señal de las vocales pronunciadas por un hombre. 

Se puede observar que la figura 2, de cada vocal tiene señales donde su amplitud varia, por ejemplo, en la vocal U, la quinta grafica de la figura 2, la amplitud de la onda es mayor en comparación de las otras vocales, en todas estas podemos observar un área donde la onda no es tan marcada, se cree que esta puede ser producida por el micrófono o el eco que se puede generar por el ambiente en el que se grabó.  

Observándolas de cerca se puede observar que cada una lleva una secuencia diferente, unas son similares como la I y U, algunas son más finas que otras en este caso la vocal U y la A son más finas que el resto. Esto se puede observar en la figura 3. 

<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/SMa.png" align="left" width="380"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/SME.png" align="left" width="380"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/SMI.png" align="left" width="380"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/SMO.png" align="left" width="380"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/SMU.png" width="380"/>

Figura 3: Señales de la voz masculina ampliadas 

A continuación, se observan las gráficas de frecuencia que genera una voz femenina, en la figura 4, en este caso se muestran las gráficas del sujeto N-2. Se puede apreciar que la gráfica de cada vocal, al igual que las gráficas de voz masculina, tienen señales donde su amplitud varia, como en la vocal A la amplitud de la onda es mayor a la de las otras vocales, se puede ver que en las gráficas hay áreas donde la onda se marca más a comparación con las gráficas de la voz masculina, se cree que esto se debe al tono del sujeto.  

<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/SMUJER.png" width="480"/>
Figura 4: Señal de las vocales pronunciadas por una mujer 

al realizar el análisis entre la voz femenina y la masculina se dedujo que la voz femenina tiene mayor amplitud dado a que tiende a ser más aguda y la masculina más grave. 

Luego de haber realizado el análisis de las señales de las voces, se precedió aplicar a cada señal la FFT (Transformada de Fourier) en la figura 5. 

<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/TF9.png" align="left" width="580"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/TF9-2.png" align="right" width="380"/>

Figura 5: FFT de las vocales pronunciadas por el sujeto N-9 

Se tomó los audios de sujeto N-9 se les aplico la FFT y se realizaron análisis donde se observó que la señal posee dos picos altos que se generan cuando el sujeto habla, en las gráficas se observa que las señales generan pico alto en 0.0 y al finalizar la onda, pero hay vocales que no generan el pico exactamente en ese punto, se piensa que esto se debe a que el sujeto al pronunciar estas vocales puedo haberlas dicho de una manera más larga de lo habitual.  

Se cree que esa señal distorsionada que se encuentra en las FFT por fuera del pico alto o sobre la superficie es ruido, ya que los audios no fueron tomados en lugares libres de ruido externo, se piensa que este ruido puede generar que la señal no fea fina, si no que tienda a distorsionarse, un ejemplo claro de esto es la vocal A, donde pareciera que su señal tiene ruido y esto puede generar picos que no deberían estar. Se puede observar que la vocal más fina en este sujeto es la O, aunque presenta un poco de ruido, sin embargo, es la más limpia en este caso.  

Luego de aplicar la FFT se realiza el espectrograma a cada señal, tomando los datos de cada matriz ya armada con los datos de la FFT, se cogió muestra por muestra para ejecutar el espectrograma; Ya obtenido el primer espectrograma se prosiguió a obtener el resto de los espectrogramas. En la figura 6 se puede apreciar uno de los espectrogramas 

<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/ESPECTOGRAM.png" width="380"/>

Ya teniendo todos los espectrogramas se realizó un análisis de estos para sacar las características de las señales se prosiguió a sacar un promedio del valor máximo de cada matriz respectiva a cada vocal, luego de sacar el promedio se construye un rango en el que se encuentra cada vocal, un rango entre en el promedio del valor máximo, esta se tomará como una característica. Se puede observar en el cuadro 1. 





