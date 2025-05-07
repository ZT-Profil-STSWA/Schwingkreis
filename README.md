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
```

### 2. 🐍 Set up virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. 📥 Install requirements

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the simulation:

```bash
python main.py
```

This will open a plot showing:

- Capacitor voltage over time
- Circuit current over time
- Charge on the capacitor over time

All based on fixed time-step numerical integration.

---

## 🧪 What’s Going On?

We simulate an RLC series circuit driven by a sine wave voltage:

- \( U(t) = A \cdot \sin(\omega t) \)
- Discretized with Euler method
- Time step: `1e-5 s`
- Duration: `1 s`

Modifiable constants:
- Resistance (R)
- Capacitance (C)
- Inductance (L)
- Frequency (ω)

You’ll find them at the top of `main.py`.

---

## 📂 Project Structure

| File              | Description                         |
|-------------------|-------------------------------------|
| `main.py`         | Core simulation + plotting logic    |
| `requirements.txt`| Python dependencies                 |
| `README.md`       | This doc 💬                         |

---

## 🤝 Contribute

Feel free to fork, PR, or suggest features. Ideas welcome:
- Real-time animation with `FuncAnimation`
- Exporting data to CSV
- GUI controls (Tkinter or PyQt)

---

## 📜 License

MIT — do whatever, just don’t sue.

---

