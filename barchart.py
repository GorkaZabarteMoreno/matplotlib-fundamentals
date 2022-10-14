import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="./data/grades.csv")
    data = data.dropna(axis=0, how="any")
    passes = pd.Series(data.Grade >= 60)
    data = pd.concat([data, passes.rename("Pass")], axis=1)

    fig = plt.figure(figsize=(8, 3))

    plt.bar(x=data.Name, height=data.Grade)
    plt.title("Student Grades")
    plt.xlabel("Students")
    plt.ylabel("Grade")
    plt.grid(color="#95a5a6", linestyle='--', linewidth=2, axis='y', alpha=0.9)
    plt.xticks(rotation=90)  # Rotate the x markers
    plt.show()
