# 🌌 Gravity Simulation

A simple and interactive real-time **gravity simulation** built with Python and Pygame. A massive central object attracts lighter particles using Newtonian gravity, and the result is a mesmerizing particle dance!

## 🚀 Features

- Intuitive GUI to set simulation parameters:
  - Center mass and size
  - Particle mass and count
- Dynamic animation based on gravitational force
- ESC key support to return to the menu without restarting the app
- Clean UI with custom fonts and visuals

## 📦 Installation
```bash
git clone https://github.com/your-username/gravity-simulation.git
cd gravity-simulation
pip install -r requirements.txt
```

## 🧪 How to Run
```bash
python main.py
```

## 📂 Project Structure
```bash
gravity-simulation/
├── assets/
│   └── images/              # Object visuals (e.g. planet.png, particle.png)
├── fonts/
│   └── Quicksand-Light.ttf  # Custom font for UI
├── menu.py                  # User input screen (GUI menu)
├── main.py                  # Entry point of the application
├── simulation.py            # Simulation logic and rendering
├── particle.py              # Physics classes and movement logic
├── requirements.txt
└── README.md
```

## 🔧 Requirements
```bash
Python 3.8+
pygame
numpy
```

All required packages are listed in requirements.txt.

## 🎮 Controls
ESC: Return to the menu during the simulation
