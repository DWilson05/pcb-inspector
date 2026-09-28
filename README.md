# PCB Inspection Verifier

A local PCB visual inspection chatbot that uses **Ollama and Qwen3-VL:4B** to verify whether a suspected defect is visible in a PCB image.

The current version allows a user to upload a PCB image, select a suspected defect, and receive a `PASS`, `FAIL`, or `REVIEW` result.

> **Note:** YOLO is not implemented yet. It will be added in a future version to automatically detect and locate defects.

---

## Tech Stack

* Python
* Gradio
* Ollama
* Qwen3-VL:4B

---

## Project Structure

```text
pcb-inspector/
│
├── README.md            # Project documentation
├── Modelfile            # Configuration for the custom Ollama model
├── app.py               # Gradio UI and application logic
├── requirements.txt     # Python dependencies
│
└── test_images/         # PCB images used for testing
```

### File Descriptions

**`Modelfile`**
Creates the custom `pcb-inspector` Ollama model and contains the model's PCB inspection instructions.

**`app.py`**
Runs the Gradio interface and sends PCB images to the Ollama model.

**`requirements.txt`**
Contains the Python packages required to run the application.

**`test_images/`**
Contains PCB images that can be used to test the application.

---

## Setup

### 1. Install Python

Download Python:

https://www.python.org/downloads/

Make sure **Add Python to PATH** is selected during installation.

Verify the installation:

```powershell
python --version
```

---

### 2. Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify:

```powershell
ollama --version
```

---

### 3. Download the Qwen Vision Model

```powershell
ollama pull qwen3-vl:4b
```

Check installed models:

```powershell
ollama list
```

---

### 4. Download/Clone the Project

If using Git:

```powershell
git clone <REPOSITORY_URL>
cd pcb-inspector
```

Or open the downloaded project folder in VS Code.

---

### 5. Install Python Dependencies

From inside the project folder:

```powershell
python -m pip install -r requirements.txt
```

---

### 6. Create the Custom Ollama Model

From the project folder:

```powershell
ollama create pcb-inspector -f Modelfile
```

Verify:

```powershell
ollama list
```

You should see:

```text
qwen3-vl:4b
pcb-inspector
```

---

## Running the Project

From the project folder:

```powershell
python app.py
```

Then open the Gradio URL shown in the terminal, usually:

```text
http://127.0.0.1:7860
```

---

## How It Works

```text
PCB Image
    ↓
Gradio
    ↓
Suspected Defect + Image
    ↓
Ollama
    ↓
Qwen3-VL:4B
    ↓
PASS / FAIL / REVIEW
```

The user provides the suspected defect. Qwen3-VL examines the image and determines whether the defect is visibly present.

---

## Future Implementation

The next major step is integrating **YOLO**.

```text
PCB Image
    ↓
YOLO
    ↓
Detect Defect
    ↓
Qwen3-VL
    ↓
Verify Defect
    ↓
PASS / FAIL / REVIEW
```

YOLO will handle defect detection and localization, while Qwen3-VL will verify the detected defect.
