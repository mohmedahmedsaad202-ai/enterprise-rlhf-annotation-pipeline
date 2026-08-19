import numpy as np

def calculate_inter_annotator_agreement(matrix: list) -> float:
    """
    Computes a simplified consensus ratio across human annotators.
    matrix: List of votes per prompt, e.g. [[1, 1, 0], [0, 0, 0]]
    where 1 = Model A preferred, 0 = Model B preferred.
    """
    agreements = []
    for prompt_votes in matrix:
        majority = max(prompt_votes.count(1), prompt_votes.count(0))
        ratio = majority / len(prompt_votes)
        agreements.append(ratio)
    
    return float(np.mean(agreements))

if __name__ == "__main__":
    # 3 Annotators rating 3 prompts
    annotations_data = [
        [1, 1, 1],  # 100% agreement
        [1, 0, 1],  # 66.6% agreement
        [0, 0, 0]   # 100% agreement
    ]
    score = calculate_inter_annotator_agreement(annotations_data)
    print(f"Overall Inter-Annotator Agreement: {score * 100:.2f}%")
