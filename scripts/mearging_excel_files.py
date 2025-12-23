import pandas as pd
import glob
import os

folder_path = r"D:\my_projects\air-india-data\data-dec-2025\app_operation_data"

# Find both xlsx and xls files
xlsx_files = glob.glob(os.path.join(folder_path, "*.xlsx"))
xls_files = glob.glob(os.path.join(folder_path, "*.xls"))

all_files = xlsx_files + xls_files

print(f"Found {len(all_files)} Excel files")
for f in all_files:
    print(" -", f)

if not all_files:
    raise FileNotFoundError("No Excel (.xlsx or .xls) files found!")

# Read and combine
df_list = []
for file in all_files:
    if file.lower().endswith(".xls"):
        df = pd.read_excel(file, engine="xlrd")
    else:
        df = pd.read_excel(file, engine="openpyxl")

    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

# Save output as xlsx
output_path = os.path.join(folder_path, "combined_output.xlsx")
combined_df.to_excel(output_path, index=False)

print("✅ Excel files (.xls + .xlsx) combined successfully!")
print(f"Output saved to: {output_path}")
