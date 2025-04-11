# Hand-Based UPI Payment Simulator

This is a mock prototype of a futuristic UPI system where users pay by scanning their **hand fingerprint** and entering a **4-digit PIN**, without needing their phone.

## Features
- FastAPI backend
- Frontend UI simulating merchant terminal
- Fingerprint scan simulation
- In-memory user & merchant accounts
- PIN and amount validation
- Sound feedback on success/failure

## Run Locally

```bash
git clone https://github.com/AmiTSarathi/handupi-simulation.git
cd handupi-simulation
pip install -r requirements.txt
uvicorn main:app --reload


![Payment Simulation](https://github.com/AmiTSarathi/handupi-simulation/raw/main/IMG1.JPG)






