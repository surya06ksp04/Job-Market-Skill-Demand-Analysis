# src/visualize.py
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import seaborn as sns

def plot_skill_trend(trends_df: pd.DataFrame, skill: str, out_path: str = None):

    df = trends_df[trends_df['skill'] == skill].copy()
    if df.empty:
        print(f"No data for skill: {skill}")
        return
    df = df.sort_values('date_month')
    plt.figure(figsize=(10, 4))
    plt.plot(df['date_month'], df['count'], marker='o')
    plt.title(f"Trend for: {skill}")
    plt.xlabel("Month")
    plt.ylabel("Count of Postings")
    plt.grid(True)
    plt.tight_layout()
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out_path)
    plt.show()

def plot_top_skills_heatmap(trends_df: pd.DataFrame, out_path: str = None):

    pivot = trends_df.pivot_table(index='skill', columns='date_month', values='count', fill_value=0)
    # optional: sort skills by total count descending
    pivot['total'] = pivot.sum(axis=1)
    pivot = pivot.sort_values('total', ascending=False).drop(columns=['total'])
    plt.figure(figsize=(12, max(4, 0.25 * pivot.shape[0])))
    sns.heatmap(pivot, cmap='viridis')
    plt.title("Skill counts by month (top skills)")
    plt.xlabel("Month")
    plt.ylabel("Skill")
    plt.tight_layout()
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out_path)
    plt.show()
