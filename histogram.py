import pandas as pd
import matplotlib.pyplot as plt


def histogram(data_var):
    min_grade = data_var.min()
    max_grade = data_var.max()
    avg_grade = data_var.mean()
    median_grade = data_var.median()
    mode_grade = data_var.mode()[0]

    fig = plt.figure(figsize=(10, 4))
    plt.hist(data_var)
    plt.axvline(x=min_grade, color="gray", linestyle="dashed", linewidth=2)
    plt.axvline(x=avg_grade, color="cyan", linestyle="dashed", linewidth=2)
    plt.axvline(x=median_grade, color="red", linestyle="dashed", linewidth=2)
    plt.axvline(x=mode_grade, color="yellow", linestyle="dashed", linewidth=2)
    plt.axvline(x=max_grade, color="gray", linestyle="dashed", linewidth=2)
    plt.title(str(data_var.name) + " values distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="./data/grades.csv")
    data = data.dropna(axis=0, how="any")

    histogram(data.Grade)
    histogram(data.StudyHours)
    histogram(data[data["StudyHours"] > 2].StudyHours)
