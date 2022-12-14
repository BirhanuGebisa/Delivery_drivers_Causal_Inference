import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
from IPython.display import Markdown, display, Image, display_html

import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.io as pio
from IPython.display import Image


def myLayout(title, x_title, y_title, mode, width, height, margin):
    return go.Layout(
        title=title,
        yaxis=dict(title=x_title),
        xaxis=dict(title=y_title),
        legend=dict(x=0, y=1.0, bgcolor='rgba(255, 255, 255, 0)',
                    bordercolor='rgba(255, 255, 255, 0)'),
        barmode=mode,
        bargap=0.15,
        bargroupgap=0.1,
        width=width,
        height=height,
        margin=margin
    )


def BarTrace(x, y, names):
    trace = []
    for i in range(y.shape[0]):
        trace1 = go.Bar(
            x=x,
            y=y[i],
            name=names[i]
        )
        trace.append(trace1)
    return trace


def barChart(x, y, names, title="", x_title="x", y_title="y", mode='group', full=False, interactive=False):
    width = None
    height = None
    margin = None
    if not (full):
        width = 540
        height = 460
        margin = dict(b=12, l=12, pad=0, r=6, t=54)
    trace = BarTrace(x=x, y=y, names=names)
    fig = go.Figure(data=trace, layout=myLayout(
        title, x_title, y_title, mode, width, height, margin))

    if(interactive):
        fig.show()
    else:
        return Image(pio.to_image(fig, format='png', width=1200))


def scatter(df, x, y, c=None, s=None, mx=None, my=None, af=None, fit=None, interactive=False):
    fig = px.scatter(df, x=x, y=y, color=c, size=s, marginal_y=my,
                     marginal_x=mx, trendline=fit, animation_frame=af)
    if(interactive):
        fig.show()
    else:
        return Image(pio.to_image(fig, format='png', width=1200))


def scatter3D(df, x, y, z, c=None, s=None, mx=None, my=None, af=None, fit=None, rotation=[1, 1, 1], interactive=False):
    fig = px.scatter_3d(df, x=x, y=y, z=z, color=c, size=s,
                        animation_frame=af, size_max=18)

    fig.update_layout(scene=dict(camera=dict(eye=dict(x=rotation[0], y=rotation[1], z=rotation[2]))),
                      )
    if(interactive):
        fig.show()
    else:
        return Image(pio.to_image(fig, format='png', width=1200))


def histogram(hist_data, group_labels, bin_size=1, curve_type='normal', show_hist=True, invert=False, interactive=False):
    if(invert):
        hist_data.reverse()
        group_labels.reverse()
    fig = ff.create_distplot(hist_data, group_labels, bin_size=bin_size,
                             curve_type=curve_type, show_hist=show_hist)
    if(interactive):
        fig.show()
    else:
        return Image(pio.to_image(fig, format='png', width=1200))


def hist(sr, interactive=False):
    x = ["Id: " + str(i) for i in sr.index]
    fig = px.histogram(x=x, y=sr.values)
    if(interactive):
        fig.show()
    else:
        return Image(pio.to_image(fig, format='png', width=1200))


def mult_hist(sr, rows, cols, title_text, subplot_titles, interactive=False):
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)
    for i in range(rows):
        for j in range(cols):
            x = ["-> " + str(i) for i in sr[i + j].index]
            fig.add_trace(go.Bar(x=x, y=sr[i + j].values), row=i + 1, col=j + 1)
    fig.update_layout(showlegend=False, title_text=title_text)
    if(interactive):
        fig.show()
    else:
        return Image(pio.to_image(fig, format='png', width=1200))


def violinplot(x, y, start: int = 0, num_features: int = 10):
    data = pd.concat([y, x.iloc[:, start:num_features]], axis=1)
    data = pd.melt(data,
                   id_vars="diagnosis",
                   var_name="features",
                   value_name='value')
    plt.figure(figsize=(20, 12))
    sns.violinplot(x="features", y="value", hue="diagnosis",
                   data=data, split=True, inner="quart")
    plt.xticks(rotation=90)
    plt.show()


def plot_count(df: pd.DataFrame, column: str, xcolumn: str = None, ycolumn: str = None) -> None:
    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, x=column)
    plt.title(f'Plot count of {column}', size=18, fontweight='bold')
    if xcolumn:
        plt.xlabel(xcolumn)
    if xcolumn:
        plt.ylabel(ycolumn)
    plt.show()


def boxplot(x, y, start: int = 0, num_features: int = 10):
    data = pd.concat([y, x.iloc[:, start:num_features]], axis=1)
    data = pd.melt(data,
                   id_vars="diagnosis",
                   var_name="features",
                   value_name='value')
    plt.figure(figsize=(20, 12))
    sns.boxplot(x="features", y="value", hue="diagnosis", data=data)
    plt.xticks(rotation=90)
    plt.show()


def swarmplot(x, y, start: int = 0, num_features: int = 10):
    data = pd.concat([y, x.iloc[:, start:num_features]], axis=1)
    data = pd.melt(data,
                   id_vars="diagnosis",
                   var_name="features",
                   value_name='value')
    plt.figure(figsize=(20, 12))
    sns.swarmplot(x="features", y="value", hue="diagnosis", data=data)
    plt.xticks(rotation=90)
    plt.show()


def plot_correlation(x):
    corr = x.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    fig, ax = plt.subplots(figsize=(24, 20))
    heatmap = sns.heatmap(corr, mask=mask, square=True, linewidths=.5,
                          vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.1f')
    heatmap.set_title('Correlation between features',
                      fontdict={'fontsize': 15}, pad=12)
    fig.show()


def pairplot(x, y, cols):
    data = x[cols]
    data["diagnosis"] = y
    g = sns.PairGrid(data, hue="diagnosis")
    g.map_diag(sns.histplot)
    g.map_offdiag(sns.scatterplot)
    g.map_lower(sns.kdeplot, cmap="Blues_d")
    g.map_upper(plt.scatter)
    g.map_diag(sns.kdeplot, lw=3)
    g.add_legend()
    plt.show()


def view_df(df, subset=[], color='#66F582'):
    df = df.reset_index()
    style = df.style.set_table_attributes("style='display:inline'").\
        bar(subset=subset, axis=1, color=color)\
        .format({"label": lambda x: x.upper()})\
        .set_properties(**{'background-color': 'white', 'color': 'black'})
    display_html(style._repr_html_(), raw=True)


def vis_sm(sm):
  viz = plot_structure(
      sm,
      graph_attributes={"scale": "2.0", 'size': 2.5},
      all_node_attributes=NODE_STYLE.WEAK,
      all_edge_attributes=EDGE_STYLE.WEAK)
  return Image(viz.draw(format='png'))