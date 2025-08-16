# src/analysis.py
import pandas as pd
from datetime import datetime
from typing import List, Dict
from pathlib import Path
from tqdm import tqdm
from .skills_extractor import SkillExtractor

class SkillDemandAnalyzer:
    def __init__(self, skills_file: str):
        self.extractor = SkillExtractor(skills_file)

    def load_jobs(self, csv_path: str, date_col: str = "date_posted") -> pd.DataFrame:
        df = pd.read_csv(csv_path, parse_dates=[date_col], low_memory=False)
        if date_col not in df.columns:
            raise KeyError(f"Date column '{date_col}' not found in CSV")
        df['date_month'] = df[date_col].dt.to_period('M').dt.to_timestamp()
        if 'industry' not in df.columns:
            df['industry'] = 'Unknown'
        if 'description' not in df.columns:
            df['description'] = df.get('title', '').astype(str)
        return df

    def annotate_skills(self, df: pd.DataFrame, text_cols: List[str] = ['title', 'description']) -> pd.DataFrame:

        skills_list = []
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Extracting skills"):
            text = " ".join([str(row.get(c, "")) for c in text_cols])
            found = self.extractor.extract_from_text(text)
            skills_list.append(sorted(found))
        df = df.copy()
        df['skills'] = skills_list
        # also create a 'skill_count'
        df['skill_count'] = df['skills'].apply(len)
        return df

    def compute_skill_trends(self, df: pd.DataFrame, top_n: int = 30) -> pd.DataFrame:

        exploded = df.explode('skills').dropna(subset=['skills'])
        exploded['skill'] = exploded['skills'].str.lower()
        grp = exploded.groupby(['date_month', 'skill']).size().reset_index(name='count')
        totals = df.groupby('date_month').size().reset_index(name='total_postings')
        merged = grp.merge(totals, on='date_month', how='left')
        merged['pct_of_postings'] = merged['count'] / merged['total_postings']
        overall = merged.groupby('skill')['count'].sum().reset_index()
        top_skills = overall.sort_values('count', ascending=False).head(top_n)['skill'].tolist()
        merged = merged[merged['skill'].isin(top_skills)]
        return merged.sort_values(['date_month','count'], ascending=[True, False])

    def save_trends(self, trends_df: pd.DataFrame, out_csv: str):
        p = Path(out_csv)
        p.parent.mkdir(parents=True, exist_ok=True)
        trends_df.to_csv(p, index=False)
