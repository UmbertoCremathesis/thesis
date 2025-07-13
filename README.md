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
├── notebooks/                    
│   ├── compare_rollout.ipynb
│   ├── dataset_selection.ipynb
│   ├── offline_training.ipynb
│   ├── track_performance.ipynb
│   └── visualize_policy.ipynb
│
├── datasets/                       # Processed datasets used for training (e.g., .npz files)
│
├── performance/                    # Line plots of policy performance during training
│
├── policies/                       # Trained policies (.d3) for offline and models
│
├── rollout/                        # Boxplots comparing policies across tasks and algorithms
│
├── training_logs/                 # Training logs for offline and fine-tuning experiments
│
├── scripts/                        # Utility scripts
│   └── download_datasets.py
│
├── environment.yml                # Conda environment definition
├── README.md
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

| Notebook                     | Description |
|------------------------------|-------------|
| `dataset_selection.ipynb`    | Selection of balanced episodes using clustering |
| `offline_training.ipynb`     | Offline RL training loop for multiple tasks and algorithms |
| `visualize_policy.ipynb`     | Visual inspection of trained policies and rollouts |
| `compare_rollout.ipynb`      | Side-by-side comparison of policy behaviors |
| `track_performance.ipynb`    | Performance tracking and aggregation of training results |


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