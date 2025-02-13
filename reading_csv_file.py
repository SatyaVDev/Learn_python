from faker import Faker
import pandas as pd

# Initialize Faker instance
fake = Faker()

# Define the number of columns and rows
num_columns = 20
num_rows = 10  # You can adjust the number of rows as needed

# Create a list of column names
columns = [f"Column_{i+1}" for i in range(num_columns)]

# Generate fake data for each row and column
data = {col: [fake.name() for _ in range(num_rows)] for col in columns}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
