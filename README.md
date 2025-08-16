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

## Example Workflow
1. Place your **job postings dataset** in `data/` (CSV format).  
   Required columns:
   - `title`, `description`, `date_posted`, `industry` (optional).

2. Add/modify **skills** in `skills/skills_list.txt`.

3. Run the analysis:
   ```bash
   python -m pip install -r requirements.txt
   python -m spacy download en_core_web_sm

   python -m src.main \
       --input_csv data/sample_jobs.csv \
       --skills_file skills/skills_list.txt \
       --output_csv outputs/skill_trends.csv
---

## View results:

outputs/skill_trends.csv → CSV of monthly skill demand.

outputs/figures/ → Heatmaps and trend plots for top skills.

## Tech Stack

Python (pandas, numpy, matplotlib, seaborn)

NLP: spaCy for tokenization and noun-chunking

Data Analysis: pandas groupby, trend aggregation

Visualization: matplotlib + seaborn

## Future Improvements

Add fuzzy matching for skill variations (ML vs. Machine Learning).

Use topic modeling or embeddings to discover new emerging skills.

Build a dashboard (Streamlit/Dash) for interactive exploration.

Add industry-level comparisons for deeper insights.

---

## License

This project is released under the MIT License – feel free to use and modify for learning or research.

