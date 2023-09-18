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

    def calculate_mean(self, column_name):
        mean_val = self.data[column_name].mean()
        print(f"The mean (average) value in column '{column_name}' is: {mean_val}")

    def calculate_median(self, column_name):
        median_val = self.data[column_name].median()
        print(f"The median value in column '{column_name}' is: {median_val}")

    def concatenate_columns(self, column1_name, column2_name, new_column_name):
        self.data[new_column_name] = self.data[column1_name] + self.data[column2_name]
        print(f"The new concatenated column '{new_column_name}' has been added.")

    def fill_missing_values(self, column_name, method_val, axis_val, value):
        if method_val == 'ffill':
            self.data[column_name]=self.data[column_name].ffill()
        elif method_val == 'bfill':
            self.data[column_name]=self.data[column_name].bfill()
        else:
            if value!='None':
                value = int(value)
            self.data[column_name] = self.data[column_name].fillna(value)
        print(self.data)   
        
    def new_column_creater(self,col_list,new_column_name):
        self.data[new_column_name]=col_list
        print(self.data)

    def drop_column(self,drop_list):
        self.data=self.data.drop(drop_list,axis='columns')    
        print(self.data)

    def shape_data(self):
        print(self.data.shape) 

    def sum_val_col(self,column_name):
        print(self.data[column_name].sum())   

    def copy_data(self,data_copy,deep_val):
        self.data_copy=self.data.copy(deep=deep_val)
        print(self.data_copy)

    def analyze_data(self):
        print("Hi, welcome to the CSV data analyzing tool!!!")
        while True:
            print("Menu options:")
            print("1. Find the number of null values in each column")
            print("2. Drop rows with null values")
            print("3. Find the maximum value in a column")
            print("4. Find the minimum value in a column")
            print("5. Calculate the mean (average) value of a column")
            print("6. Calculate the median value of a column")
            print("7. Concatenate two columns")
            print("8. Fill missing values in a column")
            print("9. Adding new column to the data")
            print("10.Drop the unnecessary column")
            print("11.Shape of the data")
            print("12.Sum of the column")
            print("13.Copy the orginal data")
            print("14.Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.find_null_values()
            elif choice == '2':
                self.drop_null_rows()
            elif choice == '3':
                column_name = input("Enter the column name to find the maximum value: ")
                self.find_max_value(column_name)
            elif choice == '4':
                column_name = input("Enter the column name to find the minimum value: ")
                self.find_min_value(column_name)
            elif choice == '5':
                column_name = input("Enter the column name to calculate the mean value: ")
                self.calculate_mean(column_name)
            elif choice == '6':
                column_name = input("Enter the column name to calculate the median value: ")
                self.calculate_median(column_name)
            elif choice == '7':
                column1_name = input("Enter the name of the first column to concatenate: ")
                column2_name = input("Enter the name of the second column to concatenate: ")
                new_column_name = input("Enter the name for the new concatenated column: ")
                self.concatenate_columns(column1_name, column2_name, new_column_name)
                print(self.data)
            elif choice == '8':
                column_name = input("Enter the column name to fill missing values: ")
                method_val = input("Enter the method to fill missing values (options: 'ffill', 'bfill', default: None): ")
                axis_val = int(input("Enter the axis to fill missing values (options: 0 or 'index', 1 or 'columns', default: 0): "))
                value = input("Enter the value to fill missing values (default: None): ")    
                self.fill_missing_values(column_name, method_val, axis_val, value)
                
            elif choice=='9':
                col_list=[]
                new_column_name=input("Enter the new_column_name: ")
                col_len=int(input("Enter the column length: "))
                for i in range(col_len):
                    data_val=input("Enter the data value to be inserted in a new_column: ")
                    col_list.append(data_val)
                self.new_column_creater(col_list,new_column_name) 

            elif choice=='10' :
                drop_list=[]
                drop_length=int(input("Enter the length of the drop list: "))  
                for i in range(drop_length):
                    drop_col=input("enter the list of column that need to be dropped: ")
                    drop_list.append(drop_col)    
                self.drop_column(drop_list)

            elif choice=='11':
                self.shape_data()
            elif choice=='12':
                column_name=input("Enter the column_name: ")
                self.sum_val_col(column_name)    
            elif choice=='13':
                data_copy=input("Enter the new copy column name: ")    
                deep_val=input("enter the deep val(options-True/False): ")
                self.copy_data(data_copy,deep_val)
            elif choice == '14':
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    # Get the path to the CSV file from the user
    path = input("Enter the specified path where your CSV file is located: ")

    try:
        analyzer = CSVDataAnalyzer(path)
        analyzer.display_sample_data()
        analyzer.analyze_data()

    except FileNotFoundError:
        print(f"Error: The file at the path '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
