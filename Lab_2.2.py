# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:48:59 2024

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
audio_path1 = 'Audio_1.wav'  # Reemplaza con la ruta de tu archivo de audio 1
audio_path2 = 'Audio_2.wav'  # Reemplaza con la ruta de tu archivo de audio 2
audio_path3 = 'Audio_3.wav'  # Reemplaza con la ruta de tu archivo de audio 3

audio1, sr1 = librosa.load(audio_path1, sr=frecuencia_muestreo, mono=True, duration=tiempo_captura)
audio2, sr2 = librosa.load(audio_path2, sr=frecuencia_muestreo, mono=True, duration=tiempo_captura)
audio3, sr3 = librosa.load(audio_path3, sr=frecuencia_muestreo, mono=True, duration=tiempo_captura)

audios = [audio1, audio2, audio3]
fuente_labels = ['Audio 1', 'Audio 2', 'Audio 3']

# Crear la figura con subplots
fig, axs = plt.subplots(3, 2, figsize=(15, 10))

# Función para realizar la FFT y graficar
def plot_time_and_frequency(ax_time, ax_freq, audio, sr, label):
    # Dominio del Tiempo
    tiempo = np.arange(len(audio)) / sr
    ax_time.plot(tiempo, audio)
    ax_time.set_title(f'Forma de Onda de {label} en el Dominio del Tiempo')
    ax_time.set_xlabel('Tiempo (s)')
    ax_time.set_ylabel('Amplitud')

    # Dominio de la Frecuencia
    N = len(audio)
    fft_audio = np.fft.fft(audio)
    fft_magnitud = np.abs(fft_audio) / N
    fft_magnitud = fft_magnitud[:N//2]  # Tomar solo la mitad positiva del espectro
    frecuencias = np.fft.fftfreq(N, 1/sr)[:N//2]

    ax_freq.plot(frecuencias, 20 * np.log10(fft_magnitud))
    ax_freq.set_title(f'Espectro de Frecuencia de {label}')
    ax_freq.set_xlabel('Frecuencia (Hz)')
    ax_freq.set_ylabel('Amplitud (dB)')
    ax_freq.set_xscale('log')  # Escala logarítmica para frecuencia
    ax_freq.grid(True)

# Graficar para cada audio
for i in range(3):
    plot_time_and_frequency(axs[i, 0], axs[i, 1], audios[i], frecuencia_muestreo, fuente_labels[i])

plt.tight_layout()
plt.show()
