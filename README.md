# Offline Reinforcement Learning for Robotic Control — Bachelor's Thesis

This repository contains the code and experiments developed for my Bachelor's thesis in Computer Engineering at the University of Padova. The goal of the project is to explore and evaluate offline reinforcement learning algorithms in robotic simulation environments using datasets from the D4RL and Minari libraries.

## 📁 Repository Structure

```
thesis-offline-rl/
│
├── gifs/                         # rollout visualizations and GIFs
├── Minari/                       # scripts or utilities related to dataset handling
│
├── notebooks/                    # Jupyter Notebooks for exploration and experimentation
│   ├── 00_presentazione.ipynb        # early exploration of the Pen dataset for internal discussion
│   ├── 01_caricamento_datasets.ipynb # loading and analyzing Pen and Relocate datasets
│   └── 02_algoritmi_d3rlpy.ipynb     # implementation of IQL and other offline RL algorithms
│
├── src/                          # (optional) reusable Python code for agents, utils, etc.
├── results/                      # evaluation logs, metrics, plots
│
├── .gitignore
├── environment.yml
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-org/thesis-offline-rl.git
cd thesis-offline-rl
```

### 2. Set up the Conda environment
```bash
conda env create -f environment.yml
conda activate thesis-rl
```

### 3. Launch Jupyter Lab
```bash
jupyter lab
```

## 🧪 Notebooks

| Notebook                         | Description |
|----------------------------------|-------------|
| `00_presentazione.ipynb`         | Initial notebook for presenting dataset insights (Pen) |
| `01_caricamento_datasets.ipynb` | Loads and analyzes datasets `pen` and `relocate` using Minari |
| `02_algoritmi_d3rlpy.ipynb`     | Trains offline RL policies (e.g., IQL) using D3RLPY |

## 📦 Dependencies

Main libraries used:
- `minari`
- `d3rlpy`
- `gymnasium`
- `mujoco`
- `wandb`
- `numpy`, `matplotlib`, `pandas`, etc.

All dependencies are listed in the `environment.yml` file.

## 👤 Author

**Umberto Crema**  
Bachelor's Degree in Computer Engineering  
University of Padova — Academic Year 2024/2025