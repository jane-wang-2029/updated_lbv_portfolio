#!/usr/bin/env python3
"""
Add a new column to lbv_portfolio_full.csv indicating if LBV is a consultant
in any of the specified consultant columns.
"""

import csv
import sys
from pathlib import Path

def main():
    csv_path = Path(__file__).parent / "lbv_portfolio_full.csv"
    
    if not csv_path.exists():
        print(f"Error: Could not find {csv_path}")
        sys.exit(1)
    
    consultant_columns = [
        "Consultant for Business Model Profitability & Funding",
        "Consultant for Market Assessment and Marketing Strategy",
        "Consultant for Management Team & Strategic Partnerships",
        "Consultant for Reimbursement"
    ]
    new_column_name = "LBV Consultant (Any Service)"
    
    # Read CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = list(reader.fieldnames)
        rows = list(reader)
    
    # Filter to existing columns only
    consultant_columns = [col for col in consultant_columns if col in headers]
    
    if not consultant_columns:
        print("Error: None of the specified consultant columns found in CSV")
        sys.exit(1)
    
    # Process rows
    yes_count = 0
    for row in rows:
        has_lbv = any('Leading Business Ventures, LLC' in str(row.get(col, '')).strip() 
                      for col in consultant_columns)
        row[new_column_name] = 'Yes' if has_lbv else 'No'
        if has_lbv:
            yes_count += 1
    
    # Add new column to headers if not present
    if new_column_name not in headers:
        headers.append(new_column_name)
    
    # Save updated CSV
    with open(csv_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"✓ Added column '{new_column_name}'")
    print(f"  Yes: {yes_count}, No: {len(rows) - yes_count}")

if __name__ == '__main__':
    main()

