#1.1.Create the file and basic layout
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/processed/patient_level_segmented.csv")
df = pd.read_csv(DATA_PATH)

st.set_page_config(page_title="Geriatric Care Gap & Segmentation", layout="wide")
st.title("Geriatric Care Gap & Patient Segmentation Analytics")
st.markdown("Interactive dashboard for population overview, utilization, segments, and risk modeling.")


#1.2. Section A – Population overview
st.header("A. Population Overview")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Patients", len(df))
with col2:
    st.metric("Average Age", round(df["age"].mean(), 1))
with col3:
    st.metric("Care Gap Rate", round(df["potential_care_gap_flag"].mean(), 3))

col4, col5 = st.columns(2)

with col4:
    st.subheader("Gender Distribution")
    st.bar_chart(df["gender"].value_counts())

with col5:
    st.subheader("Race/Ethnicity Distribution")
    st.bar_chart(df["race"].value_counts())

st.subheader("Age Group Counts")
st.bar_chart(df["age_group"].value_counts().sort_index())


#1.3. Section B – Utilization and burden
st.header("B. Utilization and Burden")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Encounters", int(df["total_encounters"].sum()))
with col2:
    st.metric("Total Hospitalizations", int(df["hospitalization_count"].sum()))
with col3:
    st.metric("Unique Patients with Care Gap", int(df["potential_care_gap_flag"].sum()))

col4, col5 = st.columns(2)

with col4:
    st.subheader("Clinical Burden (Unique Conditions)")
    fig, ax = plt.subplots()
    df["unique_conditions"].hist(bins=20, ax=ax)
    ax.set_xlabel("Unique Conditions")
    ax.set_ylabel("Number of Patients")
    st.pyplot(fig)

with col5:
    st.subheader("Medication Burden (Unique Medications)")
    fig, ax = plt.subplots()
    df["unique_medications"].hist(bins=20, ax=ax)
    ax.set_xlabel("Unique Medications")
    ax.set_ylabel("Number of Patients")
    st.pyplot(fig)


#1.4. Section C – Patient segments
st.header("C. Patient Segments")

st.subheader("Cluster Counts")
st.bar_chart(df["cluster"].value_counts().sort_index())

st.subheader("Care Gap Rate by Cluster")
care_gap_by_cluster = df.groupby("cluster")["potential_care_gap_flag"].mean()
st.bar_chart(care_gap_by_cluster)

if "pca1" in df.columns and "pca2" in df.columns:
    st.subheader("PCA Cluster Visualization")
    fig, ax = plt.subplots()
    scatter = ax.scatter(df["pca1"], df["pca2"], c=df["cluster"], alpha=0.6)
    ax.set_xlabel("PCA 1")
    ax.set_ylabel("PCA 2")
    st.pyplot(fig)



#1.5. Section D – Risk modeling
st.header("D. Risk Modeling")

st.markdown("**Target:** Hospitalization (hospitalization_flag)")

st.subheader("Feature Importance (Random Forest)")
st.image("outputs/figures/feature_importance.png", caption="Feature Importance for Hospitalization Risk Model")
