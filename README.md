# Job Market Skill Demand Analysis

**Analyze skill demand trends from job postings using NLP**  
This project tracks **rising and falling demand for skills** across industries using scraped job postings (e.g., LinkedIn, Indeed).  
It helps uncover **career insights** and gives recruiters, students, and professionals a better understanding of the **labor market landscape**.

---

## Features
- **Skill Extraction**: Identify key skills/technologies from job descriptions using a curated skills list + NLP (spaCy).
- **Trend Analysis**: Measure demand for skills over time (monthly trends).
- **Cross-Industry Insights**: Track how skills are distributed across different industries.
- **Visualizations**: Generate heatmaps and time-series plots to highlight skill demand patterns.

---

## 📂 Project Structure
job-skill-demand/
├─ data/ # Input data (scraped job postings CSV)
│ ├─ sample_jobs.csv
├─ outputs/ # Outputs (generated trends + plots)
│ ├─ skill_trends.csv
│ ├─ figures/
├─ skills/ # Skill dictionary (curated keywords list)
│ ├─ skills_list.txt
├─ src/ # Source code
│ ├─ main.py # Main pipeline runner
│ ├─ skills_extractor.py # Extracts skills from job text
│ ├─ analysis.py # Demand aggregation and trend calculation
│ ├─ visualize.py # Plotting functions
├─ requirements.txt # Dependencies
├─ README.md # Project documentation
