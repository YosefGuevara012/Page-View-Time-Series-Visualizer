import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = "date")


# Clean data
q_bottom = df["value"].quantile(q = 0.025) 
q_top = df["value"].quantile(q = 0.975)

df = df[(df["value"] > q_bottom) & (df["value"] < q_top)]


def draw_line_plot():
    # Draw line plot

    fig = df.plot(color = "red", legend = False)

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    plt.show()
  
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    df["year"] = pd.DatetimeIndex(df.index).year
    df["month"] = pd.DatetimeIndex(df.index).month
  
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot(kind = "bar", legend = True).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title = "Months", labels = ['January', 'February', 'March', 'April', 'May', 'June',
                                           'July', 'August', 'September', 'October', 'November', 'December'])

    plt.show()
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return df_bar

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    #fig.savefig('box_plot.png')
    return df_box['month']
    #return fig
