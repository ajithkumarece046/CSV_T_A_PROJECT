This Project is mainly focus on cleaning and tranforming csv data for building a dashboard .



code logic :


     it is written using oops, function and basic if and elif statement



     Here if and elif statement is used for identifying which operation is choosen by user for transforming a data

     for example:


     if choices == 1:
        null_val = data.isnull().sum()
        print("Number of null values in each column:")
        print(null_val)
    elif choices == 2:
        data = data.dropna()  # Drop rows with null values
        print("Rows with null values have been dropped.")
    elif choices == 3:
        column_name = input("Enter the column name to find the maximum value: ")
        max_val = data[column_name].max()
        print(f"The maximum value in column '{column_name}' is: {max_val}")
    elif choices == 4:
        column_name = input("Enter the column name to find the minimum value: ")
        min_val = data[column_name].min()
        print(f"The minimum value in column '{column_name}' is: {min_val}")



i have written separate functions for each operation 

     for example:

    import pandas as pd

    class CSVDataAnalyzer:
        def __init__(self, path):
            self.data = pd.read_csv(path)

        def display_sample_data(self):
            sample_data_display = input("Do you want to see a sample of your data? (yes or no): ")
            if sample_data_display.lower() == 'yes':
                print(self.data.head(10))

        def find_null_values(self):
            null_val = self.data.isnull().sum()
            print("Number of null values in each column:")
                print(null_val)

        def drop_null_rows(self):
            self.data = self.data.dropna()
            print("Rows with null values have been dropped.")

        def find_max_value(self, column_name):
            max_val = self.data[column_name].max()
            print(f"The maximum value in column '{column_name}' is: {max_val}")

        def find_min_value(self, column_name):
            min_val = self.data[column_name].min()
            print(f"The minimum value in column '{column_name}' is: {min_val}")







operations we have done using our project:


     Hi, welcome to the CSV data analyzing tool!!!
        1. Find the number of null values in each column
        2. Drop rows with null values
        3. Find the maximum value in a column
        4. Find the minimum value in a column
        5. Calculate the mean (average) value of a column
        6. Calculate the median value of a column
        7. Concatenate two columns
        8. Fill missing values in a column
        9. creating a new column to existing data



        here only very few opertions are there ,dont worry the project is going on process more operations are updated in a daily basis!!!.


