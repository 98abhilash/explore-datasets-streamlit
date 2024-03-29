import streamlit as st
import os

# EDA Pkgs
import pandas as pd

# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def main():
    """Common ML Dataset Explorer """
    st.title("Common ML Dataset Explorer")
    st.subheader("Simple Data Science with Streamlit")

    # Selecting dataset file

    def file_selector(folder_path = './datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select a dataset file",filenames)
        return os.path.join(folder_path,selected_filename)

    filename = file_selector()
    st.info("You selected {}".format(filename))

    # Reading Data
    df = pd.read_csv(filename)
    #Show Dataset

    if st.checkbox("Show Dataset"):
        number = st.number_input("Select number of rows to view",5,10)
        st.dataframe(df.head(number))

    #Show Column

    if st.button("Column Names"):
        st.write(df.columns)

    #Show Shape

    if st.checkbox("Shape of Dataset"):
        st.write(df.shape)
        data_dim = st.radio("Show Shape of Dataset by",("Rows","Columns"))
        if data_dim == "Columns":
            st.text("Number of Columns")
            st.write(df.shape[1])
        elif data_dim == "Rows":
            st.text("Number of Rows")
            st.write(df.shape[0])
        else:
            st.write(df.shape)

    
    #Select Columns

    if st.checkbox("Show Columns"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Select",all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)
    
    #Show Values

    if st.button("Value Counts"):
        st.text("Value Counts by Target/Class")
        st.write(df.iloc[:,-1].value_counts())

    #Show Datatypes

    if st.button("Show Datatypes"):
        st.text("Datatypes")
        st.write(df.dtypes)

    #Show Summary

    if st.checkbox("Show Summary"):
        st.write(df.describe().T)

    ## Plot and Visualization

    st.subheader('Data Visualization')

    # Correlation
    # Seaborn Plot

    if st.checkbox("Correlation Plot [Seaborn]"):
        st.write(sns.heatmap(df.corr(),annot = True))
        st.pyplot()

    # Count Plot

    if st.checkbox("Plot of value counts"):
        st.text("Value Counts by Target")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("Primary Column to Groupby",all_columns_names)
        selected_columns_names = st.multiselect("Select Columns",all_columns_names)
        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind = 'bar'))
            st.pyplot

    # Pie Chart

    if st.checkbox("Pie Chart"):
        all_columns_names = df.columns.tolist()
        if st.button("Generate Pie Plot"):
            st.success("Generating a Pie Chart")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct = "%1.1f%%"))
            st.pyplot()

    # Customizable Plot
    
    st.subheader("Customizable Plot")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select type of Plot",["area","bar","line","hist","box","kde"])
    selected_columns_names = st.multiselect('Select Columns to Plot',all_columns_names)

    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

        # Plot by streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)
        
        # Custom Plot

        elif type_of_plot:
            cust_data = df[selected_columns_names].plot(kind = type_of_plot)
            st.write(cust_data)
            st.pyplot()

    if st.button("Thank You"):
        st.balloons()
        
if __name__ == '__main__':
    main()