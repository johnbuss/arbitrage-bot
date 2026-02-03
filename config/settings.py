import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

PLAYWRIGHT_HEADLESS = True
COLLECTOR_TIMEOUT = 30000
REQUEST_TIMEOUT = 10

SITES = {
    "flashscore": {
        "base_url": "https://www.flashscore.com",
        "matches_endpoint": "/match/",
    },
    "bet365": {
        "base_url": "https://www.bet365.com",
    },
    "betano": {
        "base_url": "https://www.betano.com",
    },
}

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(__asctime__)s - %(name)s - %(levelname)s - %(message)s"