import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def performance_demo():

    try:

        df = pd.read_csv("student_performance.csv")

        print("\n=== Student Data ===")
        print(df)

        scores = df[["Math", "Science", "English"]].to_numpy()

        mean_scores = np.mean(scores, axis=0)

        print("\nAverage Scores:")
        print(mean_scores)

        subjects = ["Math", "Science", "English"]

        plt.bar(subjects, mean_scores)

        plt.title("Average Scores")

        plt.show()

    except FileNotFoundError:
        print("CSV file not found!")

    except Exception as e:
        print("Error:", e)