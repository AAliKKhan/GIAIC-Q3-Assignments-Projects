# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.title("Simple Data Dashboard")
# uploaded_file = st.file_uploader("Choose a CSV file" , type="csv")

# if uploaded_file is not None:
#     df= pd.read_csv(uploaded_file)
    

#     st.subheader("Data Preview")
#     st.write(df.head())

#     st.subheader("Data Summary")
#     st.write(df.describe())

#     st.subheader('Filter Data')
#     columns = df.columns.tolist()
#     selected_column= st.selectbox("Select column to filter by ", columns )
#     unique_values = df[selected_column].unique()
#     selected_value = st.selectbox("Select value", unique_values )

#     filtered_df = df[df[selected_column ] == selected_value ]
#     st.write(filtered_df )

#     st.subheader("Plot Data")
#     x_column= st.selectbox("Select x-axis column" , columns)
#     y_column= st.selectbox("Select y-axis column" , columns)
    
#     if st.button("Generate Plot"):
#         st.line_chart(filtered_df.set_index(x_column) [y_column])
# else:
#     st.write("Waiting on file upload ...")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display Data Preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Display Data Summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # Filter Data
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Plot Data
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        if filtered_df.empty:
            st.error("No data available after filtering. Please adjust your filter.")
        elif x_column not in filtered_df.columns or y_column not in filtered_df.columns:
            st.error("Selected columns are not found in the data. Please check your selections.")
        elif not pd.api.types.is_numeric_dtype(filtered_df[y_column]):
            st.error(f"The column '{y_column}' is not numeric and cannot be plotted.")
        else:
            try:
                st.line_chart(filtered_df.set_index(x_column)[y_column])
            except Exception as e:
                st.error(f"An error occurred while plotting: {e}")
else:
    st.write("Waiting on file upload...")




    

        