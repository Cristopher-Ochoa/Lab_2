# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:17:55 2024

@author: Santiago
"""

import numpy as np
import matplotlib.pyplot as plt
import librosa

# Parámetros de digitalización
frecuencia_muestreo = 48000  # Frecuencia de muestreo en Hz (48 kHz)
tiempo_captura = 60  # Tiempo de captura en segundos (60 segundos)

# Configuración del sistema: posiciones y orientaciones
# Coordenadas (x, y, z) de las fuentes sonoras
fuentes = np.array([
    [0, 0, 0],  # Fuente 1 en el origen
    [5, 3, 2],  # Fuente 2
    [-4, -2, 1]  # Fuente 3
])

# Coordenadas (x, y, z) de los micrófonos
microfonos = np.array([
    [2, 2, 0],  # Micrófono 1
    [1, -3, 0],  # Micrófono 2
    [-3, 1, 1]  # Micrófono 3
])

# Orientaciones de las fuentes (azimut y elevación en grados)
orientaciones_fuentes = np.array([
    [45, 30],  # Orientación Fuente 1
    [60, 15],  # Orientación Fuente 2
    [120, 45]  # Orientación Fuente 3
])

# Orientaciones de los micrófonos (azimut y elevación en grados)
orientaciones_microfonos = np.array([
    [90, 0],   # Orientación Micrófono 1
    [45, 10],  # Orientación Micrófono 2
    [0, 20]    # Orientación Micrófono 3
])

# Visualizar la configuración del sistema
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(fuentes[:, 0], fuentes[:, 1], fuentes[:, 2], c='r', label='Fuentes')
for i, (x, y, z) in enumerate(fuentes):
    ax.text(x, y, z, f'Fuente {i+1}')

ax.scatter(microfonos[:, 0], microfonos[:, 1], microfonos[:, 2], c='b', label='Micrófonos')
for i, (x, y, z) in enumerate(microfonos):
    ax.text(x, y, z, f'Micrófono {i+1}')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('Configuración de Fuentes y Micrófonos')
plt.show()

# Cargar las señales capturadas por cada micrófono
mic_path1 = 'Audio_1.wav'  # Reemplaza con la ruta de tu archivo de audio del micrófono 1
mic_path2 = 'Audio_2.wav'  # Reemplaza con la ruta de tu archivo de audio del micrófono 2
mic_path3 = 'Audio_3.wav'  # Reemplaza con la ruta de tu archivo de audio del micrófono 3

# Función para cargar audios utilizando librosa
def cargar_audio(ruta, sr, duracion):
    try:
        audio, sr = librosa.load(ruta, sr=sr, mono=True, duration=duracion)
        return audio, sr
    except Exception as e:
        print(f"Error al cargar el archivo {ruta}: {e}")
        return None, sr

mic1, sr1 = cargar_audio(mic_path1, frecuencia_muestreo, tiempo_captura)
mic2, sr2 = cargar_audio(mic_path2, frecuencia_muestreo, tiempo_captura)
mic3, sr3 = cargar_audio(mic_path3, frecuencia_muestreo, tiempo_captura)

mic_signals = [mic1, mic2, mic3]
mic_labels = ['Micrófono 1', 'Micrófono 2', 'Micrófono 3']

# Crear la figura con subplots para graficar los resultados del análisis
fig, axs = plt.subplots(3, 2, figsize=(15, 10))

def plot_time_and_frequency(ax_time, ax_freq, signal, sr, label):
    if signal is None:
        print(f"No se pudo graficar {label} porque la señal no fue cargada correctamente.")
        return

    # Análisis en el Dominio del Tiempo
    tiempo = np.arange(len(signal)) / sr
    ax_time.plot(tiempo, signal)
    ax_time.set_title(f'{label} - Dominio del Tiempo')
    ax_time.set_xlabel('Tiempo (s)')
    ax_time.set_ylabel('Amplitud')

    # Análisis en el Dominio de la Frecuencia usando FFT
    N = len(signal)
    fft_signal = np.fft.fft(signal)
    fft_magnitud = np.abs(fft_signal) / N
    fft_magnitud = fft_magnitud[:N//2]
    frecuencias = np.fft.fftfreq(N, 1/sr)[:N//2]

    ax_freq.plot(frecuencias, 20 * np.log10(fft_magnitud))
    ax_freq.set_title(f'{label} - Dominio de la Frecuencia')
    ax_freq.set_xlabel('Frecuencia (Hz)')
    ax_freq.set_ylabel('Amplitud (dB)')
    ax_freq.set_xscale('log')  # Escala logarítmica para frecuencia
    ax_freq.grid(True)

# Graficar para cada micrófono
for i in range(3):
    plot_time_and_frequency(axs[i, 0], axs[i, 1], mic_signals[i], frecuencia_muestreo, mic_labels[i])

plt.tight_layout()
plt.show()
