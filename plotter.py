import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse

def make_box_plot(dataframe, column_names, y_label, title):
    """
    Name:
    Parameters:
    Returns:
    """
    plt.boxplot(dataframe[column_names],labels=column_names)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    plt.savefig('make_box_plot.png')
    return 0

def make_scatter_plot(dataframe, x_label, y_label, title):
    """
    Name:
    Parameters:
    Returns:
    """
    for species_name in set(dataframe[title]):
        iris_subset = dataframe[dataframe[title] == species_name]
        plt.scatter(iris_subset[x_label], iris_subset[y_label],
                    label=species_name, s=5)
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    #save fig
    plt.savefig('make_scatter_plot.png')
    return

def make_multi_panel_figure(suptitle, dataframe, column_names,
                            x_labels, y_labels, title_scatter,
                            title_box):
    """
    Name:
    Parameters:
    Returns:
    """
    fig, axes = plt.subplots(1,2)
    fig.suptitle(suptitle)
    for species_name in set(dataframe[title_scatter]):
        iris_subset = dataframe[dataframe[title_scatter] == species_name]
        axes[0,0].scatter(iris_subset[x_labels[0]], iris_subset[y_labels[0]],
                    label=species_name, s=5)
    plt.boxplot(dataframe[column_names],labels=column_names)
    plt.ylabel(y_labels[1])
    plt.title(title_box)
    plt.show()
    plt.savefig('make_multi_panel_figure.png')
    return 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="the name of the file to read from (string)")
    parser.add_argument("column_names", help="the name of the columns to plot (string)")
    parser.add_argument("y_label_box", help="the name of the y label (string)")
    parser.add_argument("title_box", help="the name of the title (string)")
    parser.add_argument("x_label_scatter", help="the name of the x label (string)")
    parser.add_argument("y_label_scatter", help="the name of the y label (string)")
    parser.add_argument("title_scatter", help="the name of the title (string)")
    parser.add_argument("suptitle", help="the name of the suptitle (string)")
    args = parser.parse_args()
    iris = pd.read_csv(args.file_name)
    column_names = args.column_names.split(',')
    make_box_plot(iris, column_names, args.y_label_box, args.title_box)
    make_scatter_plot(iris, args.x_label_scatter,
                      args.y_label_scatter, args.title_scatter)
    make_multi_panel_figure(args.suptitle, iris, 
                            column_names, 
                            (args.x_label_scatter, args.x_label_scatter),
                            (args.y_label_scatter, args.y_label_box),
                            args.title_scatter, 
                            args.title_box)
    return 0


if __name__ == "__main__":
    main()