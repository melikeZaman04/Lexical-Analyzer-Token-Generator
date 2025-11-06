import os
from typing import Set, Dict


def load_keywords(paths=None) -> Dict[str, str]:
    """
    Try multiple candidate locations for keywords.csv and return a set of keywords.
    Default search order:
      - src/main/resources/keywords.csv
      - target\classes\keywords.csv
      - keywords.csv (cwd)
      - this module's directory
    """
    candidates = []
    if paths:
        candidates.extend(paths)
    # common Maven resource location
    candidates.append(os.path.join('src', 'main', 'resources', 'keywords.csv'))
    # compiled classes resource location (Windows slashes OK)
    candidates.append(os.path.join('target', 'classes', 'keywords.csv'))
    # cwd
    candidates.append('keywords.csv')
    # same directory as this module
    candidates.append(os.path.join(os.path.dirname(__file__), 'keywords.csv'))

    mapping = {}
    for p in candidates:
        try:
            if os.path.isfile(p):
                with open(p, 'r', encoding='utf-8') as f:
                    lines = [ln.strip() for ln in f.read().splitlines() if ln.strip()]
                    for ln in lines:
                        parts = [x.strip() for x in ln.split(',') if x.strip()]
                        if len(parts) == 1:
                            mapping[parts[0].lower()] = 'KEYWORD'
                        elif len(parts) >= 2:
                            mapping[parts[0].lower()] = parts[1].upper()
                if mapping:
                    return mapping
        except Exception:
            pass
    return mapping
