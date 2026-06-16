# Geriatric Care Gap & Patient Segmentation Analytics

## Objective
Identify care gaps, segment geriatric patient populations, and predict hospitalization risk using simulated healthcare data.

## Dataset
Synthetic multi‑table healthcare records integrated into a patient‑level dataset (`data/processed/patient_level_segmented.csv`).

## Methods
- Data integration and cleaning  
- Exploratory data analysis (EDA)  
- Patient segmentation (K‑Means clustering)  
- Predictive modeling (Logistic Regression, Random Forest)  
- Interactive dashboard (Streamlit)

## Key Findings
- Four distinct patient segments identified by utilization and burden patterns  
- Cluster 2 shows potential care gaps (moderate burden, low utilization)  
- Hospitalization risk strongly linked to utilization and condition burden  
- Segment membership adds predictive value to risk modeling  
- Dashboard enables real‑time exploration of population insights

## Relevance to Mount Sinai
Supports population‑health analytics, geriatric risk stratification, and clinical decision support.

## Relevance to Pfizer
Highlights unmet need and care‑gap analytics for high‑burden, under‑utilizing cohorts.

## Repository Structure
geriatric-care-gap-analytics/
├── data/
├── notebooks/
│   ├── 01_data_integration.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_patient_segmentation.ipynb
│   └── 04_risk_modeling.ipynb
├── dashboard/
│   └── streamlit_app.py
├── outputs/
│   ├── figures/
│   └── tables/
├── README.md
└── requirements.txt

---