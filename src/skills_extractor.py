# src/skills_extractor.py
from typing import List, Set, Dict
import re
from pathlib import Path
import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "tagger"])  

class SkillExtractor:
    """
    Two-tier extractor:
      - dictionary (exact / case-insensitive) matching of curated skills file
      - plus phrase extraction (noun chunks) to catch multi-word skill mentions
    """
    def __init__(self, skills_file: str):
        self.skills = self._load_skills(skills_file)
        # case-insensitive
        escaped = [re.escape(s) for s in sorted(self.skills, key=len, reverse=True)]
        pattern = r'\\b(' + '|'.join(escaped) + r')\\b'
        self.skill_re = re.compile(pattern, flags=re.IGNORECASE)

    def _load_skills(self, path: str) -> Set[str]:
        p = Path(path)
        skills = set()
        if not p.exists():
            raise FileNotFoundError(f"Skills file not found: {path}")
        for line in p.read_text(encoding='utf8').splitlines():
            s = line.strip()
            if s:
                skills.add(s.lower())
        return skills

    def extract_from_text(self, text: str) -> Set[str]:
        """
        Return a set of matched skills (normalized to lower-case).
        """
        if not isinstance(text, str) or not text.strip():
            return set()

        text = text.lower()
        found = set()

        for m in self.skill_re.finditer(text):
            found.add(m.group(1).lower())

        doc = nlp(text)
        for nc in doc.noun_chunks:
            phrase = nc.text.strip().lower()
            if phrase in self.skills:
                found.add(phrase)

        tokens = re.split(r'[,/;\\n]', text)
        for t in tokens:
            t = t.strip().lower()
            if t in self.skills:
                found.add(t)

        return found
