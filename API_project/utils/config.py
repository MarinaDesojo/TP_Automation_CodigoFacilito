from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv(Path(__file__).parent / ".env")

ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")




# tambien se utuliza os.environ que permite reescribir los datos de la variables, o incluso eliminarlos