# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import matplotlib.pyplot as plt
import librosa

# Definir las posiciones de las fuentes y micrófonos en coordenadas (x, y, z)
fuentes = np.array([
    [0, 0, 0],  # Fuente 1 en el origen
    [5, 3, 2],  # Fuente 2
    [-4, -2, 1]  # Fuente 3
])

microfonos = np.array([
    [2, 2, 0],  # Micrófono 1
    [1, -3, 0],  # Micrófono 2
    [-3, 1, 1],  # Micrófono 3
    [0, -4, 2]  # Micrófono 4
])

# Cargar los audios
audio_path1 = 'ruta/al/audio1.wav'  # Reemplaza con la ruta de tu archivo de audio 1
audio_path2 = 'ruta/al/audio2.wav'  # Reemplaza con la ruta de tu archivo de audio 2
audio_path3 = 'ruta/al/audio3.wav'  # Reemplaza con la ruta de tu archivo de audio 3

audio1, sr1 = librosa.load(audio_path1, sr=None)
audio2, sr2 = librosa.load(audio_path2, sr=None)
audio3, sr3 = librosa.load(audio_path3, sr=None)

audios = [audio1, audio2, audio3]
fuente_labels = ['Fuente 1', 'Fuente 2', 'Fuente 3']

# Crear la figura con subplots
fig = plt.figure(figsize=(15, 10))

# Subplot 1: Configuración 3D de fuentes y micrófonos
ax1 = fig.add_subplot(2, 2, 1, projection='3d')

# Graficar fuentes
ax1.scatter(fuentes[:, 0], fuentes[:, 1], fuentes[:, 2], c='r', label='Fuentes')
for i, (x, y, z) in enumerate(fuentes):
    ax1.text(x, y, z, f'Fuente {i+1}')

# Graficar micrófonos
ax1.scatter(microfonos[:, 0], microfonos[:, 1], microfonos[:, 2], c='b', label='Micrófonos')
for i, (x, y, z) in enumerate(microfonos):
    ax1.text(x, y, z, f'Micrófono {i+1}')

# Configurar etiquetas y leyenda
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend()
ax1.set_title('Configuración de Fuentes y Micrófonos')

# Subplots para las formas de onda de cada audio
for i in range(3):
    ax = fig.add_subplot(2, 2, i + 2)
    ax.plot(audios[i])
    ax.set_title(f'Forma de Onda de {fuente_labels[i]}')
    ax.set_xlabel('Muestras')
    ax.set_ylabel('Amplitud')

plt.tight_layout()
plt.show()

