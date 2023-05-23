def find_column_index(header, column_name):
    column_index = None
    for idx, col in enumerate(header):
        if column_name.lower() in col.lower():
            column_index = idx
            break
    return column_index

def normalize_data(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = []

    for value in data:
        normalized_value = (value - min_val) / (max_val - min_val)
        normalized_data.append(normalized_value)

    return normalized_data

def read_dataset(file_path):
    with open(file_path, "r") as file:
        dataset = [line.strip().split(",") for line in file]
    return dataset

def extract_column_data(dataset, column_index):
    data = [float(row[column_index]) for row in dataset[1:]]
    return data

# Specify the file path and column name
file_path = "C:/Users/Zaidi/Downloads/DSS.csv"
column_name = "Height"

# Read the dataset from the file
dataset = read_dataset(file_path)

# Extract the desired column from the dataset
header = dataset[0]
column_index = find_column_index(header, column_name)

if column_index is not None:
    data = extract_column_data(dataset, column_index)
    normalized_data = normalize_data(data)

    # Format and print the message and normalized data
    message = "Your characteristics have been normalized. Following are your results:"
    formatted_message = message.center(len(message) + 6)  # Add 6 to accommodate spaces before and after
    print(formatted_message)
    print(normalized_data)
else:
    print("Column not found: " + column_name)
