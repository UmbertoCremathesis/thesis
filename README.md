# Offline Reinforcement Learning for Robotic Control — Bachelor's Thesis

This repository contains the code and experiments developed for my Bachelor's thesis in Computer Engineering at the University of Padova. The goal of the project is to explore and evaluate offline reinforcement learning algorithms in robotic simulation environments using datasets from the D4RL suite (accessed via Minari) and training with D3RLPY.

---

## 📁 Repository Structure

```
umbertocrema/
│
├── gifs/                         # rollout visualizations and videos
├── Minari/                       # local helper code (ignored by Git)
│
├── notebooks/                    # Jupyter Notebooks for each phase
│   ├── 00_presentazione.ipynb        # initial dataset exploration (Pen)
│   ├── 01_caricamento_datasets.ipynb # loading and inspecting Pen + Relocate datasets
│   └── 02_algoritmi_d3rlpy.ipynb     # IQL and other offline RL experiments
│
├── results/                      # logs, plots, evaluation metrics
├── environment.yml               # conda environment definition
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository via SSH

```bash
git clone git@github.com:UmbertoCremathesis/umbertocrema.git
cd umbertocrema
```

### 2. Create and activate the environment

```bash
conda env create -f environment.yml
conda activate thesis-env
```

### 3. Register the environment as a Jupyter kernel (once)

```bash
python -m ipykernel install --user --name thesis-env --display-name "Python (thesis-env)"
```

### 4. Launch Jupyter Lab

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

---

## 📦 Environment

Key packages used:

- `minari`, `d3rlpy`, `gymnasium`, `mujoco`, `robosuite`
- `torch`, `wandb`, `pybullet`, `moviepy`, `pygame`
- `jupyterlab`, `numpy`, `pandas`, `matplotlib`

Full details in [`environment.yml`](./environment.yml)

---

## 👤 Author

**Umberto Crema**  
Bachelor's Degree in Computer Engineering  
University of Padova — Academic Year 2024/2025

---

## 📄 License

This project is part of an academic thesis.