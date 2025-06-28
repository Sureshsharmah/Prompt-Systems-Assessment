import subprocess
import sys

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_main():
    from main import main
    main()

if __name__ == "__main__":
    print("Installing requirements...")
    install_requirements()
    print("Running Prompt Engineer Test...")
    run_main()
