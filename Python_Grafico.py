import serial
import matplotlib.pyplot as plt
import numpy as np

# Configuração da porta serial
ser = serial.Serial('COM3', 9600)  # Altere 'COM3' para sua porta serial
velocidades = []
direcoes = []

try:
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            vel, direc = map(float, data.split(','))
            velocidades.append(vel)
            direcoes.append(direc)

            # Plotando o gráfico
            plt.clf()
            plt.subplot(2, 1, 1)
            plt.plot(velocidades, label='Velocidade (km/h)')
            plt.legend()

            plt.subplot(2, 1, 2)
            plt.plot(direcoes, label='Direção (graus)', color='orange')
            plt.legend()

            plt.pause(0.1)
        except Exception as e:
            print(f"Erro: {e}")
except KeyboardInterrupt:
    print("Saindo...")
finally:
    ser.close()
