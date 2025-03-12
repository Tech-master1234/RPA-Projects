import pandas as pd

def calculate_highest_expense_category(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Ensure the CSV has 'Category' and 'Amount' columns
    if 'Category' not in df.columns or 'Amount' not in df.columns:
        return "Invalid CSV format. Must contain 'Category' and 'Amount' columns."
    
    # Group by 'Category' and sum the 'Amount'
    grouped = df.groupby('Category')['Amount'].sum()
    
    # Find the category with the highest expense
    highest_expense_category = grouped.idxmax()
    
    return highest_expense_category

# Example usage
if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]  # Get the file path from command line arguments
    highest_expense_category = calculate_highest_expense_category("C:\Users\manoj\OneDrive\Documents\1PROGRAMS\UiPath\Integrating python\Inputdata.csv")
    print(highest_expense_category)
