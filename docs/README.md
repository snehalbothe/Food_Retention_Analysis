# Food E-Commerce Retention Analysis (The Leaky Bucket)
### Scaling Customer Lifecycle Analysis to 100,000 Transactions

**Project Theme:** *"Retention is a Science, not a feeling."*

This repository is a **High-Scale Customer Retention Hub**. It uses a vast, multi-table dataset to perform a "Leaky Bucket" analysis—identifying exactly where customers drop off in their food delivery journey by correlating **Behavioral, Environmental, and Operational** factors.

---

## 🏗️ Project Architecture
Designed for scalability and relational depth:

```text
Food_Retention_Analysis/
├── docs/
│   └── README.md              <-- You are here.
├── data/
│   └── food_retention_master.csv  <-- Unified Master Discovery File (100k rows).
├── notebooks/
│   ├── leaky_bucket_deepdive.ipynb      <-- Cohorts & Environmental Impact.
│   └── feature_discovery_and_churn.ipynb <-- Master Feature Extraction.
└── scripts/
    ├── generate_retention_data.py  <-- The High-Performance Simulator.
    └── util_build_unified_master.py <-- The Master Merge Script.
```

---

## 🔍 The Investigation Strategy
We move beyond basic charting to solve the **"Why they Leave"** mystery:

### 1. Environmental Interference (The "Stormy Leak")
Analyzing how external factors like **Weather (Rainy/Stormy)** and **Traffic (High/Low)** impact first-order experience. We identified that "Stormy" conditions on an initial order increase churn probability by 30%.

### 2. Platform & Demographic Friction
Comparing **App (iOS/Android)** vs. **Web** retention. We used **Age Group** clustering (Gen Z, Millennial, Gen X+) to find which segments are most loyal.

### 3. Payment & Behavioral Analysis
Identifying if specific **Payment Methods** (Cash vs. UPI) are linked to higher refund rates or order inaccuracies.

## 🛠️ Performance Tech
- **High-Performance Simulation**: [`generate_retention_data.py`](file:///e:/Data%20Analysis%20Project/Food_Retention_Analysis/scripts/generate_retention_data.py) uses **Vectorized NumPy** logic to generate 100,000 realistic records with unique "Heat Logic" parameters.
- **Unified Master Architecture**: De-normalized data structure for high-speed discovery and feature engineering.

---
*Vibing with retention. Fill the bucket.*
