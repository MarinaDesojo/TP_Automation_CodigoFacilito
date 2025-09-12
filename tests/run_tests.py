import subprocess
from datetime import datetime
import os

# Crear carpeta 'reports' si no existe
os.makedirs("../reports", exist_ok=True)

# Formatear fecha y hora para el nombre del archivo
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_file = f"reports/report_{timestamp}.html"

# Ejecutar pytest con el nombre generado
subprocess.run([
    "pytest",
    f"--html={report_file}",
    "--self-contained-html"
])
