import matplotlib.pyplot as plt
import math

L = 5 * 10 ** (-3)
C = 2* 10 ** (-6)
omega = 10 ** 4

initial_amplitude = 1

resistance = 5

step_size = 10 ** (-5)
duration = 0.01

step_amount = int(duration / step_size) + 1


t = 0
I = 0
Q = 0

time_values = []
voltage_values = []
current_values = []
generator_values = []

def step(delta_time):
    global t, I, Q
    input_voltage = initial_amplitude * math.sin(omega * t)
    capacitor_voltage = Q/C
    delta_I = (input_voltage / L - Q / (L * C) - resistance * I / L) * delta_time

    I += delta_I
    Q += I * delta_time
    t += delta_time

    return capacitor_voltage, I, input_voltage


for i in range(0,step_amount):
    voltage, current, generator = step(step_size)
    time_values.append(t)
    voltage_values.append(voltage)
    current_values.append(current)
    generator_values.append(generator) 

plt.plot(time_values, voltage_values, label="Capacitor Voltage (V)")
plt.plot(time_values, current_values, label="Current (I)")
plt.plot(time_values, generator_values, label="Generator voltage (U)")

plt.title("RLC Circuit Simulation 📈")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
