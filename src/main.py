# src/main.py
import argparse
from pathlib import Path
from .analysis import SkillDemandAnalyzer
from .visualize import plot_skill_trend, plot_top_skills_heatmap

def main(args):
    analyzer = SkillDemandAnalyzer(args.skills_file)
    print("Loading jobs...")
    df = analyzer.load_jobs(args.input_csv, date_col=args.date_col)
    print(f"{len(df)} job postings loaded.")
    df = analyzer.annotate_skills(df, text_cols=['title','description'])
    trends = analyzer.compute_skill_trends(df, top_n=args.top_n)
    analyzer.save_trends(trends, args.output_csv)
    print(f"Saved trends to {args.output_csv}")
    out_fig_dir = Path(args.output_fig_dir)
    out_fig_dir.mkdir(parents=True, exist_ok=True)
    # heatmap
    print("Generating heatmap...")
    plot_top_skills_heatmap(trends, out_path=str(out_fig_dir / "top_skills_heatmap.png"))
    top_skills = trends.groupby('skill')['count'].sum().sort_values(ascending=False).head(5).index.tolist()
    for skill in top_skills:
        print("Plotting:", skill)
        plot_skill_trend(trends, skill, out_path=str(out_fig_dir / f"{skill}_trend.png"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_csv", required=True, help="Path to job postings CSV")
    parser.add_argument("--skills_file", default="skills/skills_list.txt", help="Path to skills list")
    parser.add_argument("--date_col", default="date_posted", help="Date column name")
    parser.add_argument("--output_csv", default="outputs/skill_trends.csv", help="Where to save trends CSV")
    parser.add_argument("--output_fig_dir", default="outputs/figures", help="Where to save figures")
    parser.add_argument("--top_n", type=int, default=30, help="Top N skills to track")
    args = parser.parse_args()
    main(args)
