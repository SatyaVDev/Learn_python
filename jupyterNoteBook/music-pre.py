#!/usr/bin/env python
# coding: utf-8

import io

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Read the JSON data into a pandas DataFrame
df = pd.read_json("DataSet/music_data_set.json")

# Convert the DataFrame to CSV format, but store the result in a string (StringIO)
csv_output = io.StringIO()
df.to_csv(csv_output, index=False)
csv_content = csv_output.getvalue()

# Reset the StringIO object's cursor to the beginning, and read it back into a DataFrame
csv_output.seek(0)  # Reset cursor
new_df = pd.read_csv(csv_output, index_col=0)

# Encoding the 'music_type' column because it is categorical
label_encoder = LabelEncoder()
new_df["music_type"] = label_encoder.fit_transform(new_df["music_type"])

# Features (X) and target (Y)
X = new_df.drop(columns="music_type")  # All columns except 'music_type' are features
Y = new_df["music_type"]  # Target variable

# Train the DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X, Y)

# Predicting new values (for example, for age = 20 and gender = 1)
# The input must be a 2D array, matching the number of features used during training
predictions = model.predict(
    [[20, 1], [23, 0]]
)  # You can change these values based on actual inputs

# Convert numeric predictions back to original labels
predicted_music_types = label_encoder.inverse_transform(predictions)

# Print the predicted music types
print(predicted_music_types)
