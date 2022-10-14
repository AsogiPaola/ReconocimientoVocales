# ReconocimientoVocales
Proyecto realizado con el fin de diferenciar vocales y genero (masculino/femenino) según las frecuencias, basandose en las frecuencias altas relacionadas generalmente a la voz Feminina y frecuencias bajas ala masculina.
Marco teórico 

El espectrograma es una herramienta primordial en el estudio de la comunicación acústica en vertebrados. Es básicamente una representación visual del sonido donde muestra la variación en energía, es decir, el poder de densidad espectral en los dominios de frecuencia y tiempo. Los espectrogramas permiten explorar de manera visual la variación acústica que se presenta en nuestro sistema de estudio, facilitando la distinción en las diferencias estructurales a pequeñas escalas temporales/espectrales que nuestros oídos no pueden detectar. El espectrograma se divide en tres dimensiones temporal, frecuencial y amplitud de la distribución de energía de una señal, que se pueden observar en la figura 1

<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/1.png" width="280"/>


# Procedimiento 

Este informe se realizó mediante el método analítico y comparativo, ya que con las diversas voces recolectadas se generaron graficas que permiten analizar los diferentes rangos de voz al pronunciar las vocales en español. Se pidió a diferentes personas que pronunciaran las vocales en español una por una, de manera que cada vocal quedara en un solo audio facilitando más adelante su proceso de reconocimiento. 
Captura de datos 

Para la recolección de datos se utilizó Audacity (2), es una aplicación informática multiplataforma libre, que se puede usar para grabación y edición de audio, y la captura de los datos se realizó con un micrófono YN685, con un periodo de muestreo de 44100 con dos canales, los datos recolectados se almacenaron y graficaron en un programa llamado Spyder3 utilizando la librería Soundfile. (3) 

Cuando se obtuvieron las gráficas de las señales se observó que la señal tenía un tiempo en cero hasta que sonaba la voz de la persona, para eliminar este tiempo cero los audios se recortaron uno por uno con el programa Audacity. 

Al sacar las FFT de las señales, observamos que las señales poseían canal estéreo, es decir, dos matrices; para aplicar la FFT se necesita que el audio sea mono, así que se realizó la conversión de estéreo a mono a través de la plataforma Audacity.  

 
Análisis 

A continuación, se observarán las gráficas de frecuencia que genera una voz masculina al decir las vocales, en la figura 2, en este caso se muestran las gráficas del sujeto N-1.

<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sA.png" width="280"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sE.png" width="280"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sI.png" width="280"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sO.png" width="280"/>
<img src="https://github.com/AsogiPaola/ReconocimientoVocales/blob/main/images/sU.png" width="280"/>




