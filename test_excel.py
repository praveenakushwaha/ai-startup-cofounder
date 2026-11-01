from tools.excel_export import export_to_excel

sample = {
    "Market": "Growing",
    "Finance": "Good",
    "Risk": "Low"
}

export_to_excel(
    sample,
    "reports/test.xlsx"
)

print("Excel Created")