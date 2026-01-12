\# C++ to PlantUML Visualization Toolkit (CPPTOPUML)



\## 1. Overview

This toolkit provides a structured methodology and automation pipeline for transforming embedded C/C++ source code (Arduino, STM32, ESP32) into professional-grade PlantUML architecture diagrams.



\## 2. Contents

\*   \*\*`arduino\_to\_graph\_instructions.txt`\*\*: The core instruction set. Defines the rules for parsing code and generating standardized Hardware, Sequence, and Data Flow diagrams.

\*   \*\*`render\_diagrams.py`\*\*: A Python automation script that batch-converts all `.puml` files in the directory to PNG images.

\*   \*\*`plantuml.jar`\*\*: The Java-based rendering engine (downloaded automatically by the script if missing).

\*   \*\*`\*.puml` files\*\*: The generated PlantUML source files for your specific systems (SIMPLEVCU, STM32, ESP32).

\*   \*\*`img/`\*\*: The output directory containing the generated visual diagrams.



\## 3. Workflow



\### Step 1: Analyze \& Generate

Use an LLM (like Gemini) with the `arduino\_to\_graph\_instructions.txt` prompt to parse your code files.

\*   \*\*Input:\*\* Your `.ino` or `.c` source files.

\*   \*\*Prompt:\*\* "Apply @arduino\_to\_graph\_instructions.txt to my code."

\*   \*\*Output:\*\* Three `.puml` files per system (Hardware, Sequence, DataFlow).



\### Step 2: Render Visuals

Run the automation script to generate images.

```bash

python render\_diagrams.py

```

\*   The script will check for Java.

\*   It will download `plantuml.jar` if needed.

\*   It will process every `.puml` file and save PNGs to the `img/` folder.



\### Step 3: Review

Open the `img/` folder to view the professional diagrams:

\*   \*\*Hardware:\*\* Pinouts, wiring, and component architecture.

\*   \*\*Sequence:\*\* Timing diagrams of interrupts and main loops.

\*   \*\*DataFlow:\*\* Full serialization maps of structs and packets.



\## 4. Diagram Standards (defined in instructions)

\*   \*\*Hardware:\*\* "Rich Style" with embedded pinout tables and pastel colors.

\*   \*\*Sequence:\*\* Strict participant aliasing and logical grouping.

\*   \*\*Data Flow:\*\* Complete, non-truncated field lists with C data types.



\## 5. Requirements

\*   \*\*Python 3.x\*\*

\*   \*\*Java Runtime Environment (JRE)\*\* (for PlantUML)



