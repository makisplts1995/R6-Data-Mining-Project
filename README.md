# 🎮 Rainbow Six Siege: Tactical Data Mining & Win Prediction Analysis

![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Data Mining](https://img.shields.io/badge/Data%20Mining-Research-orange.svg)
![Weka](https://img.shields.io/badge/ML-Weka-blueviolet.svg)

## 🎓 Academic Abstract
This research investigates the tactical landscape of the competitive tactical shooter **Tom Clancy's Rainbow Six Siege** through the lens of data mining. By analyzing a high-dimensional dataset of ranked matches, this study identifies the core determinants of victory, focusing on the interplay between player experience, operator synergy, and tactical role distribution. Our findings challenge the prevailing "psychological momentum" theory, proving instead that match outcomes are predominantly driven by structural tactical alignments and quantified experience gaps.

## 🔬 Research Methodology
The study follows a rigorous Data Science lifecycle:
1. **Data Acquisition**: Processing large-scale CSV dumps from the S5 Ranked season.
2. **Feature Engineering**: Implementation of Bayesian domain knowledge filters and Z-score normalization for experience metrics.
3. **Exploratory Data Analysis**: Using InfoGain and ReliefF algorithms to rank feature importance.
4. **Machine Learning Workflow**: 
    *   **Unsupervised Learning**: Comparative analysis of K-Means, Expectation-Maximization (EM), and Density-Based clustering to identify player archetypes.
    *   **Supervised Learning**: Decision Tree (J48) classification for win prediction.
    *   **Association Rule Mining**: Association Rule discovery for operator synergy.

---

## 📊 Key Research Findings

### 1. Tactical Synergy (Apriori Analysis)
We identified critical operator pairings that significantly impact win rates. 
*   **Micro-Tactical**: Hard Breach synergies (Thermite/Thatcher) and Defensive anchors (Valkyrie/Nitro).
*   **Macro-Tactical**: The "Defensive Backbone" pattern showing a 3.20 Lift for integrated Intel/Trapper setups.

### 2. Player Profiling (Clustering)
Using K-Means and Radar analysis, we categorized players into four distinct tactical profiles, from "Lethal Novices" to "Elite Tacticians".

### 3. Predictive Performance
Our J48 Decision Tree achieved a robust **60.78% accuracy** in predicting round outcomes, validated via ROC curves and cross-validation.

---

## 🛠️ Technical Stack
*   **Data Processing**: [Polars](https://pola.rs/) (High-performance Rust-based DataFrame library)
*   **Machine Learning**: [WEKA 3.8.6](https://www.cs.waikato.ac.nz/ml/weka/)
*   **Visualization**: Matplotlib & Seaborn
*   **Environment**: Python 3.11

---

## 📂 Repository Structure
*   `R6_Data_Mining_Pipeline_Final.ipynb`: Full end-to-end data cleaning and feature engineering.
*   `Visualization_Scripts/`: Python scripts for generating all academic-grade infographics.
*   `Figures/`: High-resolution exports of all analysis results.
*   `results/`: Weka logs and model outputs for reproducibility.

---

## 📥 Data Source
The analysis is based on the [Rainbow Six Siege S5 Ranked Dataset](https://www.kaggle.com/datasets/maxcobra/rainbow-six-siege-s5-ranked-dataset) available on Kaggle.

---

## 🚀 How to Reproduce
1.  Clone this repository.
2.  Install dependencies: `pip install -r requirements.txt`.
3.  Download the raw dataset from Kaggle and place it in the `Raw_Data/` directory.
4.  Run the Jupyter Notebook to generate the ARFF files.
5.  Import the ARFF files into WEKA for analysis.
6.  (Optional) Run scripts in `Visualization_Scripts/` to regenerate the charts.

---
**Author**: makisplts1995 
**Project**: Academic Research in Data Mining & Predictive Analytics
