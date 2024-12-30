import subprocess
import sys

def install_requirements():
    requirements = [
        'http-server',  # For serving the files
        'live-server'   # For development
    ]

    # Install Node.js packages globally
    print("Installing Node.js packages...")
    for package in requirements:
        subprocess.check_call(['npm', 'install', '-g', package])

    print("\nAll requirements installed successfully!")
    print("\nTo start the server, run:")
    print("http-server")
    print("\nOr for development:")
    print("live-server")

if __name__ == "__main__":
    try:
        install_requirements()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)