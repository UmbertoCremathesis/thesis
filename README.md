# Offline Reinforcement Learning for Robotic Control — Bachelor's Thesis

This repository contains the code and experiments developed for my Bachelor’s thesis in Computer Engineering at the University of Padova. The project focuses on exploring and evaluating offline reinforcement learning algorithms in robotic simulation environments using Adroit tasks from the D4RL suite (Pen, Relocate, Door, and Hammer), accessed via Minari and trained with D3RLPY.

---

## ⚙️ Prerequisites
To run this project, make sure the following prerequisites are met:

### 🔹 1. Conda (Anaconda or Miniconda)
**Check if installed:**
```bash
conda --version
```
**If missing:**  
Download and install from [conda.io](https://docs.conda.io/en/latest/miniconda.html)

---

### 🔹 2. Git
**Check if installed:**
```bash
git --version
```
**If missing:**  
Install Git via your system's package manager:

- **Linux (APT):**
  ```bash
  sudo apt update
  sudo apt install git
  ```
- **macOS (Homebrew):**
  ```bash
  brew install git
  ```
  or install Xcode Command Line Tools:
  ```bash
  xcode-select --install
  ```

---

### 🔹 3. C/C++ Build Tools
Required to compile packages like `mujoco-py`, `pybullet`, etc.

**Check if installed:**
```bash
gcc --version
```
**If missing:**

- **Linux:**
  ```bash
  sudo apt update
  sudo apt install build-essential
  ```
- **macOS:**
  ```bash
  xcode-select --install
  ```

---

## 📁 Repository Structure
```
thesis/
│
├── gifs/                             # rollout visualizations and videos
│
├── Minari/                           # local helper code (ignored by Git)
│
├── notebooks/                        # Jupyter Notebooks for each phase
│   ├── 00_presentazione.ipynb        # initial dataset exploration (Pen)
│   ├── 01_caricamento_datasets.ipynb # loading and inspecting Pen + Relocate datasets
│   └── 02_algoritmi_d3rlpy.ipynb     # IQL and other offline RL experiments
│   └── 03_due_dita.ipynb             # Pen task with only wrist, index, and thumb active 
│
├── results/                          # logs, plots, evaluation metrics
│
├── scripts/                          # utility scripts (e.g., download datasets)
│   └── download_datasets.py          # script to download all required D4RL Adroit datasets via Minari
│
├── environment.yml                   # conda environment definition
│
├── .gitignore
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/UmbertoCremathesis/thesis.git
cd thesis
```

### 2. Create and activate the environment
```bash
conda env create --file=environment.yml
conda activate thesis-env
```

### 3. Download required datasets
This project uses datasets from the D4RL suite via Minari. Run the following script **before using the notebooks**:
```bash
python scripts/download_datasets.py
```
This will download all necessary datasets (e.g., Pen, Door, Relocate, Hammer) used throughout the project.  
> Make sure that the `thesis-env` environment is active when you run the script.

### 4. Register the environment as a Jupyter kernel (once)
```bash
python -m ipykernel install --user --name thesis-env --display-name "Python (thesis-env)"
```

### 5. Launch Jupyter Lab
```bash
jupyter lab
```
Then, switch the notebook kernel to `Python (thesis-env)`.

---

## 🧪 Notebooks

| Notebook                         | Description |
|----------------------------------|-------------|
| `00_presentazione.ipynb`         | Initial exploration of Adroit Pen dataset |
| `01_caricamento_datasets.ipynb` | Loads and analyzes Pen and Relocate datasets via Minari |
| `02_algoritmi_d3rlpy.ipynb`     | Trains offline RL policies (e.g., IQL) using D3RLPY |
| `03_due_dita.ipynb`             | Pen task with only wrist, index, and thumb active |

---

## 📦 Environment

Key packages used:

- `minari`, `d3rlpy`, `gymnasium`, `mujoco`
- `jupyterlab`, `numpy`, `matplotlib`

Full details in [`environment.yml`](./environment.yml)

---

## 👤 Author

**Umberto Crema**  
Bachelor's Degree in Computer Engineering  
University of Padova — Academic Year 2024/2025