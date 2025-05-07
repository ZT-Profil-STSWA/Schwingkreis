# 🔁 Schwingkreis Simulator (RLC Circuit)

A Python-based simulation of a sinusoidal-driven RLC circuit. It numerically solves and plots:

- 📈 Capacitor Voltage (Uₚ)
- ⚡ Current (I)
- 💾 Charge (Q)

Visualized using `matplotlib`, this is perfect for physics classes, tinkering, or just vibing with resonance.

---

## 🚀 Installation

Clone the repo and run it locally using Python 3.10+.

### 1. 📦 Clone the project

```bash
git clone https://github.com/ZT-Profil-STSWA/Schwingkreis.git
cd Schwingkreis

2. 🐍 Set up virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. 📥 Install requirements

pip install -r requirements.txt

▶️ Usage

Run the simulation:

python main.py

This will open a plot showing:

    Capacitor voltage over time

    Circuit current over time

    Charge on the capacitor over time

All based on fixed time-step numerical integration.
🧪 What’s Going On?

We simulate an RLC series circuit driven by a sine wave voltage:

    U(t)=A⋅sin⁡(ωt)U(t)=A⋅sin(ωt)

    Discretized with Euler method

    Time step: 1e-5 s

    Duration: 1 s

Modifiable constants:

    Resistance (R)

    Capacitance (C)

    Inductance (L)

    Frequency (ω)

You’ll find them at the top of main.py.
