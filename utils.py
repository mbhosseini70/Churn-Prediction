
def replace_yes_no_values(column):
    column.replace("No internet service", "No", inplace=True)
    column.replace("No phone service", "No", inplace=True)
    return column

# To encode the binary 'Yes'/'No' values into numerical values
def encode_yes_no_values(column):
    return column.replace({'Yes': 1, 'No': 0})