# 🤚 HandUPI Simulation – Biometric UPI Payments

This is a **proof of concept (PoC)** for a futuristic UPI-based payment system in India where users can authorize payments using a **biometric hand scan** instead of scanning a QR code. No need for mobile phones — just scan your hand on a merchant's device, enter your 4-digit PIN, and you're done.

---

## 🚀 Features

- Simulates biometric (hand) scan
- PIN-based payment authorization
- Merchant-facing payment UI (no QR scan)
- In-memory data storage for simplicity
- Built with Python + FastAPI + basic web frontend

---

## 🖥️ Run Locally

```bash
git clone https://github.com/AmiTSarathi/handupi-simulation.git
cd handupi-simulation
pip install -r requirements.txt
uvicorn main:app --reload
```

Open your browser and navigate to:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📸 UI Screenshot

![Payment Simulation](https://github.com/AmiTSarathi/handupi-simulation/raw/main/IMG1.JPG)

---

## 🌐 Live Demo (Replit)

Try the live version on Replit:  
🔗 [https://replit.com/@AmiTSarathi/handupi-simulation](https://replit.com/@AmiTSarathi/handupi-simulation)

---

## 🛠️ What's Next

- Add real biometric integration (fingerprint/hand)
- Secure user database (SQLite/PostgreSQL)
- Merchant transaction history & analytics
- Notification & voice confirmation
- Scalable cloud deployment

---

## 🙌 Author

Made with ❤️ by [Amit Sarathi](https://github.com/AmiTSarathi)
