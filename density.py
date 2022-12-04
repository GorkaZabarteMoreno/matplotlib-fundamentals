import pandas as pd
import matplotlib.pyplot as plt


def show_density(var_data):
    fig = plt.figure(figsize=(10, 4))

    var_data.plot.density()
    plt.title('Data Density')
    plt.axvline(x=var_data.mean(), color='cyan', linestyle='dashed', linewidth=2)
    plt.axvline(x=var_data.median(), color='red', linestyle='dashed', linewidth=2)
    plt.axvline(x=var_data.mode()[0], color='yellow', linestyle='dashed', linewidth=2)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="./data/grades.csv")
    data = data.dropna(axis=0, how="any")
    grades = data.Grade
    studyHours = data[data["StudyHours"] > 2].StudyHours
    show_density(grades)
    show_density(studyHours)
