import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv(filepath_or_buffer="./data/grades.csv")
    data = data.dropna(axis=0, how="any")
    passes = pd.Series(data.Grade >= 60)
    data = pd.concat([data, passes.rename("Pass")], axis=1)

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    ax[0].bar(x=data.Name, height=data.Grade)
    ax[0].set_title("Grades")
    ax[0].set_xticklabels(data.Name, rotation=90)

    pass_counts = data.Pass.value_counts()
    ax[1].pie(pass_counts, labels=pass_counts)
    ax[1].set_title("Passing grades")
    ax[1].legend(pass_counts.keys().tolist())

    fig.suptitle("Students data")
    plt.show()
