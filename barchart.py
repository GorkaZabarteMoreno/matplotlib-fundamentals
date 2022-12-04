import matplotlib.pyplot as plt
import pandas as pd


def minmaxscaler(x):
    minimum = x.min()
    maximum = x.max()
    return (x - minimum) / (maximum - minimum)


def barchart(x):
    fig = plt.figure(figsize=(8, 3))

    var_data = x.value_counts()
    plt.bar(x=var_data.index, height=var_data.values)
    plt.title(str(x.name))
    plt.xlabel(str(x.name))
    plt.ylabel("Number")
    plt.xticks(x.unique())
    plt.grid(color="#95a5a6", linestyle='--', linewidth=2, axis='y', alpha=0.9)
    plt.xticks(rotation=90)  # Rotate the x markers
    plt.show()


def barchart_comparison(dataframe, x1, x2):
    dataframe.sort_values(ascending=True, by=str(x1.name))
    dataframe.plot(x='Name', y=[str(x1.name), str(x2.name)], kind='bar', figsize=(8, 5))
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="./data/grades.csv")
    data = data.dropna(axis=0, how="any")
    passes = pd.Series(data.Grade >= 60)
    data = pd.concat([data, passes.rename("Pass")], axis=1)

    barchart(x=data.Pass)
    barchart_comparison(dataframe=data, x1=data.StudyHours, x2=data.Grade)  # Different scales make different to compare
    gradesNormalized = minmaxscaler(data.Grade)
    studyHoursNormalized = minmaxscaler(data.StudyHours)
    data["Grade"] = gradesNormalized
    data["StudyHours"] = studyHoursNormalized
    barchart_comparison(dataframe=data, x1=data.StudyHours, x2=data.Grade)
