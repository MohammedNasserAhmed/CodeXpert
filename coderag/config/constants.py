import json
from pathlib import Path

# Load configuration from config.json
CONFIG_PATH = Path(__file__).parent / "config.json"

with open(CONFIG_PATH, "r") as config_file:
    CONFIG = json.load(config_file)

MODEL = CONFIG["model"]
REPO_ID = CONFIG["repo_id"]
EMBEDDING_MODEL = CONFIG["embedding_model"]
CODEBASE_DIR = CONFIG["codebase_dir"]
DOCS_DIR = CONFIG["docs_dir"]
