# Credit Card Fraud Detection 🛡️

This project uses machine learning (Logistic Regression) to detect fraudulent transactions in credit card data.

## 📌 Objectives

- Build a model to classify transactions as fraudulent or not.
- Handle class imbalance using `class_weight='balanced'` in Logistic Regression.
- Evaluate the model with precision, recall, F1-score, and confusion matrix.

## 🛠 How to Run the Project
Data is present in the link provided in requirement.txt

### 1. Clone the repository
```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection

2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Launch the Jupyter Notebook
bash
Copy
Edit
jupyter notebook
5. Run all cells in the notebook
Open the notebook and run it cell by cell. It contains:

Data loading and preprocessing

Feature scaling

Model training

Evaluation (classification report and confusion matrix)

📊 Model Used
Logistic Regression from scikit-learn

Handled class imbalance using class_weight='balanced'
📁 Project Structure
bash
Copy
Edit
credit-card-fraud-detection/
│
├── data/                      # (Optional) Directory to store datasets
├── fraud_detection.ipynb      # Jupyter notebook with all code
├── requirements.txt
└── README.md
🧠 Future Improvements
Try advanced models like Random Forest or XGBoost

🙋‍♂️ Author
Deepanshu Joshi - @deepanshu3012-github



