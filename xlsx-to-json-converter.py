import pandas as pd

# Load the Excel file
df = pd.read_excel("input.xlsx", engine="openpyxl")

# Convert to JSON
json_data = df.to_json(orient="records", indent=4)

# Save to a file
with open("output.json", "w") as json_file:
    json_file.write(json_data)

print("Conversion completed! JSON saved as output.json")

