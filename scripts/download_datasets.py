import minari

datasets = [
    "D4RL/hammer/human-v2",
    "D4RL/hammer/cloned-v2",
    "D4RL/hammer/expert-v2",
    "D4RL/door/human-v2",
    "D4RL/door/cloned-v2",
    "D4RL/door/expert-v2",
    "D4RL/relocate/human-v2",
    "D4RL/relocate/cloned-v2",
    "D4RL/relocate/expert-v2",
    "D4RL/pen/human-v2",
    "D4RL/pen/cloned-v2",
    "D4RL/pen/expert-v2",
]

for dataset_id in datasets:
    print(f"Downloading: {dataset_id}")
    minari.download_dataset(dataset_id)

print("\nAll datasets downloaded successfully.")