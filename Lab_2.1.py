# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:12:34 2024

@author: Santiago
"""

import numpy as np
import matplotlib.pyplot as plt
import librosa

# Parámetros de digitalización
frecuencia_muestreo = 48000  # Frecuencia de muestreo en Hz (48 kHz)
niveles_cuantificacion = 24  # Niveles de cuantificación (24 bits)
tiempo_captura = 60  # Tiempo de captura en segundos (60 segundos)
SNR_dB = 100  # Relación Señal a Ruido en dB
num_canales = 2  # Número de canales (estéreo)

# Cargar los audios con los parámetros definidos
audio_path1 = 'ruta/al/audio1.wav'  # Reemplaza con la ruta de tu archivo de audio 1
audio_path2 = 'ruta/al/audio2.wav'  # Reemplaza con la ruta de tu archivo de audio 2
audio_path3 = 'ruta/al/audio3.wav'  # Reemplaza con la ruta de tu archivo de audio 3

audio1, sr1 = librosa.load(audio_path1, sr=frecuencia_muestreo, mono=False, duration=tiempo_captura)
audio2, sr2 = librosa.load(audio_path2, sr=frecuencia_muestreo, mono=False, duration=tiempo_captura)
audio3, sr3 = librosa.load(audio_path3, sr=frecuencia_muestreo, mono=False, duration=tiempo_captura)

# Graficar formas de onda de los audios
fig, axs = plt.subplots(3, 1, figsize=(15, 10))

# Graficar Audio 1
axs[0].plot(audio1)
axs[0].set_title('Forma de Onda del Audio 1')
axs[0].set_xlabel('Muestras')
axs[0].set_ylabel('Amplitud')

# Graficar Audio 2
axs[1].plot(audio2)
axs[1].set_title('Forma de Onda del Audio 2')
axs[1].set_xlabel('Muestras')
axs[1].set_ylabel('Amplitud')

# Graficar Audio 3
axs[2].plot(audio3)
axs[2].set_title('Forma de Onda del Audio 3')
axs[2].set_xlabel('Muestras')
axs[2].set_ylabel('Amplitud')

plt.tight_layout()
plt.show()
