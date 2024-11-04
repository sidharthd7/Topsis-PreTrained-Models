# Conversational Model Selection Using TOPSIS

This project aims to apply the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method to evaluate and rank pre-trained conversational models based on various performance metrics. TOPSIS helps to identify the best model by comparing each model's performance with an ideal solution.

## Assignment Overview

As per the assignment requirements, we are tasked to apply TOPSIS to find the best pre-trained model for conversational tasks. The evaluation criteria include metrics like response relevance, fluency, diversity, latency, and memory usage. The results include detailed descriptions, graphs, tables, and rankings based on the TOPSIS scores.

### Criteria & Weights
- **Response Relevance** (Beneficial)
- **Fluency** (Beneficial)
- **Diversity** (Beneficial)
- **Latency** (Non-Beneficial)
- **Memory Usage** (Non-Beneficial)

Weights for each criterion were predefined for this project but can be adjusted as needed.

## Getting Started

### Prerequisites

To run this project, you'll need:
- Python 3.7 or later
- Required libraries listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sidharthd7/Topsis-PreTrained-Models.git
   cd Topsis-Pretrained_Models
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

1. Open the Python script `main.py`.
2. Modify the scores array if using actual evaluation data, or keep the sample data for testing.
3. Run the script:
   ```bash
   python main.py
   ```

### Results

The script outputs a table with each model's TOPSIS score and rank. A sample CSV file `topsis_results.csv` is generated containing these results.

## TOPSIS Methodology

1. **Normalization**: Each criterion's scores are normalized to create a uniform scale.
2. **Weighted Normalization**: Each normalized score is multiplied by the corresponding weight of its criterion.
3. **Ideal and Anti-Ideal Solutions**: Based on the criteria, the ideal and anti-ideal solutions are determined.
4. **Distance Calculation**: For each model, the Euclidean distance from the ideal and anti-ideal solutions is calculated.
5. **TOPSIS Score Calculation**: The TOPSIS score is computed for each model, ranking them based on how close they are to the ideal solution.

### Sample Hypothetical Results

| Model              | TOPSIS Score | Rank |
|--------------------|--------------|------|
| GPT-3              | 0.85         | 1    |
| DialoGPT           | 0.75         | 2    |
| BlenderBot         | 0.72         | 3    |
| T5 Conversational  | 0.65         | 4    |
| BERT Dialogue      | 0.60         | 5    |

The generated CSV file (`topsis_results.csv`) will contain these results.

## Additional Notes

- **Testing**: Due to technical limitations, testing was conducted on a smaller set of hypothetical scores and models. The results reflect these test conditions.
