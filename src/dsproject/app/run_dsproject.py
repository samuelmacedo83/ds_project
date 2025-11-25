import subprocess

def run_dsproject_app():
    cmd = ["streamlit", "run", "./src/dsproject/app/app.py"]
    subprocess.run(cmd, check=True)