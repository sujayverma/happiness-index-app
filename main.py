import streamlit as st
import pandas as pd
import plotly.express as pt

st.title("In Search for Happiness")

x_axis = st.selectbox("Select data for x-axis: ",
                      ('Gdp', 'Happiness', 'Generosity'))

y_axis = st.selectbox("Select data for y-axis: ",
                      ('Gdp', 'Happiness', 'Generosity'))

st.subheader(f"{x_axis} and {y_axis}")


def get_data(x_axis, y_axis):
    data = pd.read_csv("happy.csv")
    values = data.get([x_axis.lower(), y_axis.lower()])

    return values.to_dict(orient="records")


value = get_data(x_axis, y_axis)
x_value = []
y_value = []
for i in value:
    x_value.append(i[x_axis.lower()])
    y_value.append(i[y_axis.lower()])

figure = pt.scatter(x=x_value, y=y_value, labels={"x": x_axis, "y": y_axis})

st.plotly_chart(figure)


# figure = px.scatter(data,
#                     x=f"{x_option}", y=f"{y_option}",
#                     labels={"x": f"{x_option}", "y": f"{y_option}"})
# st.plotly_chart(figure)
