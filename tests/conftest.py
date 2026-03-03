import sys
from pathlib import Path

# ajoute le dossier src au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))