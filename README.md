# C++ to PlantUML Visualization Toolkit (Arduino-To-PUML)

This toolkit provides a structured methodology and automation pipeline for transforming embedded C/C++ source code (Arduino, STM32, ESP32) into professional-grade PlantUML architecture diagrams.

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| **`arduino_to_graph_instructions.txt`** | The core AI instruction set for parsing code and generating standardized diagrams. |
| **`render_diagrams.py`** | Python automation script to batch-convert `.puml` files to PNG images. |
| **`plantuml.jar`** | Java-based rendering engine (auto-downloaded by script). |
| **`img/`** | Output directory containing generated visual diagrams. |

## 🚀 Workflow

### 1. Analyze & Generate
Use an LLM (like Gemini) with the `arduino_to_graph_instructions.txt` prompt to parse your code files.
*   **Input:** Your `.ino` or `.c` source files.
*   **Action:** Provide the instruction set to the LLM and ask it to apply it to your files.
*   **Output:** Three `.puml` files per system (Hardware, Sequence, DataFlow).

### 2. Render Visuals
Run the automation script to generate high-resolution images:
```bash
python render_diagrams.py
```
*   Ensures **Java** is available.
*   Automatically acquires `plantuml.jar` if missing.
*   Processes all diagrams and saves them to the `img/` directory.

### 3. Review Architecture
Open the `img/` folder to view the professional documentation:
*   **Hardware Architecture:** Physical pinouts, wiring, and component grouping.
*   **Logic Sequence:** Timing-accurate flow of interrupts, state machines, and main loops.
*   **Data Variable Flow:** Byte-level serialization maps of structs and communication packets.

## 📊 Diagram Standards
*   **Hardware:** "Rich Style" featuring embedded pinout tables, component color-coding, and specific chip part numbers.
*   **Sequence:** Strict participant aliasing, logical grouping, and microsecond-level timing notes.
*   **Data Flow:** Comprehensive, non-truncated field lists including exact C data types and transformation logic.

## 🛠 Requirements
*   **Python 3.x**
*   **Java Runtime Environment (JRE)**
