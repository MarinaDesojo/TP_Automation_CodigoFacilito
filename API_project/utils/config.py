from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv(Path(__file__).parent / ".env")

ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")
