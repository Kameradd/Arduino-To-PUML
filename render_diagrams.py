import os
import subprocess
import sys
import glob
import urllib.request
import shutil

# Configuration
PLANTUML_URL = "https://github.com/plantuml/plantuml/releases/download/v1.2024.1/plantuml-1.2024.1.jar"
JAR_NAME = "plantuml.jar"

def check_java():
    """Check if Java is installed and in PATH"""
    try:
        subprocess.run(["java", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except (OSError, subprocess.CalledProcessError):
        return False

def check_or_download_jar():
    """Find plantuml.jar or download it"""
    if os.path.exists(JAR_NAME):
        return True
    
    # Check parent dirs just in case
    if os.path.exists(f"../{JAR_NAME}"):
        shutil.copy(f"../{JAR_NAME}", JAR_NAME)
        return True

    print(f"'{JAR_NAME}' not found in current directory.")
    print("Downloading latest PlantUML jar (approx 10MB)...")
    try:
        # User-Agent header is sometimes needed for GitHub/SourceForge
        req = urllib.request.Request(PLANTUML_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(JAR_NAME, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("Download complete.")
        return True
    except Exception as e:
        print(f"Error downloading: {e}")
        return False

def render_files():
    """Batch render all .puml files"""
    puml_files = glob.glob("*.puml")
    if not puml_files:
        print("No .puml files found to render.")
        return

    print(f"Found {len(puml_files)} diagrams. Starting render...")

    # Create output directory
    os.makedirs("img", exist_ok=True)

    success_count = 0
    
    for puml in puml_files:
        print(f"Processing: {puml}...")
        
        # Command: java -jar plantuml.jar -tpng -o img input.puml
        cmd = [
            "java", "-jar", JAR_NAME,
            "-tpng",           # Output PNG only
            "-o", "img",       # Output to 'img' folder
            puml
        ]
        
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print(f"  [OK] {puml}")
                success_count += 1
            else:
                print(f"  [FAIL] {puml}")
                print("  Error:", result.stderr)
        except Exception as e:
            print(f"  [ERR] Failed to run java: {e}")

    print("-" * 30)
    print(f"Finished. Successfully rendered {success_count}/{len(puml_files)} diagrams.")
    print("Images are in the 'img' folder.")

if __name__ == "__main__":
    print("--- PlantUML Batch Renderer ---")
    
    if not check_java():
        print("Error: 'java' is not installed or not in your PATH.")
        print("Please install Java Runtime Environment (JRE).")
        sys.exit(1)
        
    if not check_or_download_jar():
        print(f"Error: Could not find or download {JAR_NAME}.")
        sys.exit(1)
        
    render_files()
