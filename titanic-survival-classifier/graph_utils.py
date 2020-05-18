import plotly.graph_objs as go
import plotly.offline as py
import numpy as np

# Function for pie plots
def plot_pie(column, class1df, class2df) :
    
    trace1 = go.Pie(values  = class1df[column].value_counts().values.tolist(),
                    labels  = class1df[column].value_counts().keys().tolist(),
                    hoverinfo = "label+percent+name",
                    domain  = dict(x = [0,.48]),
                    name    = "Survived Passengers",
                    marker  = dict(line = dict(width = 2,
                                               color = "rgb(243,243,243)")
                                  ),
                    hole    = .6
                   )
    trace2 = go.Pie(values  = class2df[column].value_counts().values.tolist(),
                    labels  = class2df[column].value_counts().keys().tolist(),
                    hoverinfo = "label+percent+name",
                    marker  = dict(line = dict(width = 2,
                                               color = "rgb(243,243,243)")
                                  ),
                    domain  = dict(x = [.52,1]),
                    hole    = .6,
                    name    = "Dead Passengers" 
                   )


    layout = go.Layout(dict(title = column + " Distribution per Survival Status",
                            plot_bgcolor  = "rgb(243,243,243)",
                            paper_bgcolor = "rgb(243,243,243)",
                            annotations = [dict(text = "Survived Passengers",
                                                font = dict(size = 13),
                                                showarrow = False,
                                                x = .15, y = .5),
                                           dict(text = "Dead Passengers",
                                                font = dict(size = 13),
                                                showarrow = False,
                                                x = .83,y = .5
                                               )
                                          ],
                            height = 450
                           )
                      )
    data = [trace1,trace2]
    fig  = go.Figure(data = data,layout = layout)
    
    py.iplot(fig)


# Function for histogram
def histogram(column, class1df, class2df) :
    trace1 = go.Histogram(x  = class1df[column],
                          histnorm= "percent",
                          name = "Survived Passengers",
                          marker = dict(line = dict(width = .5,
                                                    color = "black"
                                                    )
                                        ),
                         opacity = .9 
                         ) 
    
    trace2 = go.Histogram(x  = class2df[column],
                          histnorm = "percent",
                          name = "Dead Passengers",
                          marker = dict(line = dict(width = .5,
                                              color = "black"
                                             )
                                 ),
                          opacity = .9
                         )
    
    data = [trace1,trace2]
    layout = go.Layout(dict(title =column + " Distribution per Survival Status ",
                            plot_bgcolor  = "rgb(243,243,243)",
                            paper_bgcolor = "rgb(243,243,243)",
                            xaxis = dict(gridcolor = 'rgb(255, 255, 255)',
                                             title = column,
                                             zerolinewidth=1,
                                             ticklen=5,
                                             gridwidth=2
                                            ),
                            yaxis = dict(gridcolor = 'rgb(255, 255, 255)',
                                             title = "percent",
                                             zerolinewidth=1,
                                             ticklen=5,
                                             gridwidth=2
                                            ),
                            height = 430
                           )
                      )
    fig  = go.Figure(data=data,layout=layout)
    
    py.iplot(fig)


# Function for correlation matrix

def corr_matrix(dummy_df):
    # Calculate correlation
    correlation = dummy_df.corr()
    # Determine tick labels
    matrix_cols = dummy_df.columns.tolist()
    # Convert to array
    corr_array  = np.array(correlation)

    # Plot
    trace = go.Heatmap(z = corr_array,
                    x = matrix_cols,
                    y = matrix_cols,
                    colorscale = "Viridis",
                    colorbar   = dict(title = "Pearson Correlation coefficient",
                                        titleside = "right"
                                        ) ,
                    )

    layout = go.Layout(dict(title = "Correlation Matrix for Variables",
                            autosize = False,
                            height  = 720,
                            width   = 800,
                            margin  = dict(r = 0 ,l = 210,
                                        t = 25,b = 210,
                                        ),
                            yaxis   = dict(tickfont = dict(size = 9)),
                            xaxis   = dict(tickfont = dict(size = 9))
                        )
                    )

    data = [trace]
    fig = go.Figure(data=data,layout=layout)

    py.iplot(fig)


# Plot radar chart for survived and died passengers (binary variables)
def plot_radar(df, binary_cols, aggregate, title) :
    data_frame = df[df["Survived"] == aggregate] 
    data_frame_x = data_frame[binary_cols].sum().reset_index()
    data_frame_x.columns  = ["feature","yes"]
    data_frame_x["no"]    = data_frame.shape[0]  - data_frame_x["yes"]
    data_frame_x  = data_frame_x[data_frame_x["feature"] != "Survived"]
    
    #count of 1's(yes)
    trace1 = go.Scatterpolar(r = data_frame_x["yes"].values.tolist(),
                             theta = data_frame_x["feature"].tolist(),
                             fill  = "toself",name = "count of 1's",
                             mode = "markers+lines",
                             marker = dict(size = 5)
                            )
    #count of 0's(No)
    trace2 = go.Scatterpolar(r = data_frame_x["no"].values.tolist(),
                             theta = data_frame_x["feature"].tolist(),
                             fill  = "toself",name = "count of 0's",
                             mode = "markers+lines",
                             marker = dict(size = 5)
                            ) 
    layout = go.Layout(dict(polar = dict(radialaxis = dict(visible = True,
                                                           side = "counterclockwise",
                                                           showline = True,
                                                           linewidth = 2,
                                                           tickwidth = 2,
                                                           gridcolor = "white",
                                                           gridwidth = 2),
                                         angularaxis = dict(tickfont = dict(size = 10),
                                                            layer = "below traces"
                                                           ),
                                         bgcolor  = "rgb(243,243,243)",
                                        ),
                            paper_bgcolor = "rgb(243,243,243)",
                            title = title,height = 700))
    
    data = [trace2,trace1]
    fig = go.Figure(data=data,layout=layout)
    
    py.iplot(fig)