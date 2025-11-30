#!/usr/bin/env python3
"""
Helper script to convert CSV data into HTML table rows for index.html

Usage:
    python convert_csv_to_html_rows.py input.csv output_rows.html

The CSV should have these columns (in order):
    Index, Company Name, Company Website, LinkedIn, Affiliation, City, State, 
    Region, Company Category, Technology Description, Funding Agency, 
    Funding Amount, Consultant for IP and Competitive Assessment,
    Consultant for Business Model Profitability & Funding,
    Consultant for Market Assessment and Marketing Strategy,
    Consultant for Management Team & Strategic Partnerships,
    Consultant for Reimbursement, Consultant for Regulatory
"""

import csv
import sys
import html
from pathlib import Path


def format_url(url, pd):
    """Format URL as clickable link if it's a valid URL, otherwise return as text."""
    if pd.isna(url) or url == '' or url == 'NA':
        return 'NA'
    
    url_str = str(url).strip()
    
    # If it doesn't start with http, assume it's not a URL
    if not url_str.startswith(('http://', 'https://')):
        return html.escape(url_str)
    
    # Format as clickable link
    return f'<a href="{html.escape(url_str)}" target="_blank" rel="noopener">{html.escape(url_str)}</a>'


def format_cell(value, pd):
    """Format a cell value, handling URLs, NA values, and HTML escaping."""
    if pd.isna(value) or value == '':
        return '--'
    
    value_str = str(value).strip()
    
    # Check if it's a URL (starts with http)
    if value_str.startswith(('http://', 'https://')):
        return format_url(value_str, pd)
    
    # Escape HTML entities
    return html.escape(value_str)


def convert_csv_to_html_rows(csv_path, start_row=10):
    """
    Convert CSV file to HTML table rows.
    
    Args:
        csv_path: Path to CSV file
        start_row: Starting row number (default 10, since rows 0-9 already exist)
    
    Returns:
        String of HTML table rows
    """
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas is required. Install with: pip install pandas")
        sys.exit(1)
    
    # Read CSV
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)
    
    # Expected columns (18 total)
    expected_columns = [
        'Index', 'Company Name', 'Company Website', 'LinkedIn', 'Affiliation',
        'City', 'State', 'Region', 'Company Category', 'Technology Description',
        'Funding Agency', 'Funding Amount',
        'Consultant for IP and Competitive Assessment',
        'Consultant for Business Model Profitability & Funding',
        'Consultant for Market Assessment and Marketing Strategy',
        'Consultant for Management Team & Strategic Partnerships',
        'Consultant for Reimbursement', 'Consultant for Regulatory'
    ]
    
    # Check if columns match (allow for variations)
    if len(df.columns) != len(expected_columns):
        print(f"Warning: Expected {len(expected_columns)} columns, found {len(df.columns)}")
        print(f"Columns found: {list(df.columns)}")
        print("\nProceeding anyway...")
    
    html_rows = []
    
    for idx, row in df.iterrows():
        row_num = start_row + idx
        
        # Start building the HTML row
        html_row = f'        <!-- Row {row_num} -->\n        <tr>\n'
        
        # Add each cell
        for col_idx, col_name in enumerate(df.columns):
            value = row[col_idx]
            
            # Special handling for Index column - use row_num instead
            if col_idx == 0:
                cell_value = str(row_num)
            # Special handling for URL columns (Company Website, LinkedIn)
            elif col_idx in [2, 3]:  # Company Website, LinkedIn
                cell_value = format_url(value, pd)
            else:
                cell_value = format_cell(value, pd)
            
            html_row += f'          <td>{cell_value}</td>\n'
        
        html_row += '        </tr>\n'
        html_rows.append(html_row)
    
    return '\n'.join(html_rows)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nExample:")
        print("  python convert_csv_to_html_rows.py data.csv output_rows.html")
        sys.exit(1)
    
    csv_path = Path(sys.argv[1])
    
    if not csv_path.exists():
        print(f"Error: CSV file not found: {csv_path}")
        sys.exit(1)
    
    # Determine start row (default 10)
    start_row = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    
    # Convert CSV to HTML rows
    print(f"Converting {csv_path} to HTML rows...")
    html_rows = convert_csv_to_html_rows(csv_path, start_row)
    
    # Output to file or stdout
    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
        output_path.write_text(html_rows, encoding='utf-8')
        print(f"✓ HTML rows written to {output_path}")
        print(f"  Copy and paste these rows into index.html before the '<!-- TODO: Add rows 10-163 here -->' comment")
    else:
        print(html_rows)


if __name__ == '__main__':
    main()

