# LBV Portfolio Table - Intellectual Property Assessment Clients

A fully functional, searchable, sortable table displaying Leading Business Ventures' portfolio of Intellectual Property Assessment Clients.

## Features

- **Sortable columns** - Click any column header to sort
- **Global search** - Search across all columns simultaneously
- **Per-column search** - Filter individual columns with AND logic
- **Hide/Show columns** - Toggle column visibility
- **Pagination** - Navigate through pages (10, 25, 50, or 100 rows per page)
- **Export to CSV** - Download filtered data
- **Responsive design** - Works on desktop and mobile
- **Sticky first column** - Index column stays visible while scrolling horizontally

## Usage

Simply open `index.html` in any modern web browser. No server required - it's a self-contained HTML file.

## Data

The table contains 164 companies with the following information:
- Company details (name, website, LinkedIn, location)
- Technology descriptions
- Funding information
- Consultant assignments across multiple service areas

All data is publicly available from company websites, LinkedIn profiles, or public SBIR filings.

## Files

- `index.html` - Main HTML file with the interactive table
- `lbv_portfolio_full.csv` - Complete dataset in CSV format
- `add_lbv_column.py` - Script to add derived columns to CSV
- `convert_csv_to_html_rows.py` - Helper script to convert CSV to HTML table rows

## Technology

- jQuery - JavaScript library (via CDN)
- DataTables - Table plugin for jQuery (via CDN)
- Pure HTML/CSS/JavaScript - No build process required

## Browser Support

Works in all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## License

All information in this table is publicly available data.

