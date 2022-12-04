import pandas as pd
import matplotlib.pyplot as plt


def boxplot(data_var):
    fig = plt.figure(figsize=(10, 4))
    plt.boxplot(data_var)
    plt.title(str(data_var.name) + " values distribution")
    plt.show()


def boxplot_comparison(dataframe, var_num, var_cat):
    dataframe.boxplot(column=str(var_num.name), by=str(var_cat.name), figsize=(10, 4))
    plt.title(str(var_num.name) + " by " + str(var_cat.name) + " values distribution")
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="./data/grades.csv")
    data = data.dropna(axis=0, how="any")

    passes = pd.Series(data.Grade >= 60)
    data = pd.concat([data, passes.rename("Pass")], axis=1)
    print(data)

    boxplot(data.Grade)
    boxplot(data.StudyHours)

    q01 = data.StudyHours.quantile(q=0.01)
    studyHours = data[data["StudyHours"] > q01].StudyHours
    boxplot(studyHours)

    boxplot_comparison(dataframe=data, var_num=data.StudyHours, var_cat=data.Pass)
