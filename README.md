# 📈 Computing Moments from a Stock Price Stream

This project simulates a real-time stream of stock prices and analyzes it using Apache DataSketches' `ebpps_sketch` for reservoir sampling. The goal is to detect abnormal market behaviors by computing the **mean**, **variance**, **skewness**, and **kurtosis** of the stream.

---

## 📦 Project Structure

- `main.py` – Runs the full pipeline: streaming → sampling → AMS → alerts → plot
- `stream_generator.py` – Simulates a live stock price stream using normal or log-normal behavior
- `sampling_RS.py` – Performs reservoir sampling using `ebpps_sketch` (Apache DataSketches)
- `AMS.py` – Computes 1st to 4th moments
- `alert.py` – Generates alert messages with `[INFO]`, `[WARNING]`, and `[CRITICAL]` levels
- `requirements.txt` – Dependencies
---

## 🧠 Techniques Used

- Apache DataSketches (`ebpps_sketch`) for bounded sampling
- AMS Algorithm for moment estimation
- Real-time alerting system for outlier detection
- Matplotlib for visualization

---

## 📌 Notes

> **Due to API limitations in `ebpps_sketch` (v5.2.0)**, we use a parallel list to store streamed values for moment analysis. Sampling is still done via `ebpps_sketch` as required.

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
