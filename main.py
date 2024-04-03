import chartgpt as cg
import pandas as pd
import streamlit as st
import plotly
df = pd.read_csv('world_population.csv')
chart = cg.Chart(df, api_key="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")
fig= plotly.graph_objs.Figure(chart.plot("Top 10 Pop vs. country bar chart vertical"))



# import streamlit as st
# import numpy as np
# import plotly.figure_factory as ff

# # Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# print(type(fig))
st.plotly_chart(fig, use_container_width=True)