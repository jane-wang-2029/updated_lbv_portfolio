# Extension Plan: Adding Pages 2-17 and GitHub Hosting

## Current Status
- ✅ `index.html` created with 10 rows (rows 0-9) from page 1
- ✅ All functionality working: sorting, global search, per-column search, hide/show columns, pagination
- ⏳ Need to add rows 10-163 (approximately 154 more rows)

## Step 1: Adding Rows 10-163

### Option A: Manual Entry (if you have the data in another format)
1. Locate your source data (CSV, Excel, or original HTML pages 2-17)
2. For each row, add a `<tr>` block inside `<tbody>` before the `<!-- TODO: Add rows 10-163 here -->` comment
3. Follow this exact format:

```html
<!-- Row X -->
<tr>
  <td>X</td>
  <td>Company Name</td>
  <td><a href="https://example.com" target="_blank" rel="noopener">https://example.com</a></td>
  <td><a href="https://linkedin.com/..." target="_blank" rel="noopener">https://linkedin.com/...</a></td>
  <td>Affiliation</td>
  <td>City</td>
  <td>State</td>
  <td>Region</td>
  <td>Company Category</td>
  <td>Technology Description</td>
  <td>Funding Agency</td>
  <td>Funding Amount</td>
  <td>Consultant for IP and Competitive Assessment</td>
  <td>Consultant for Business Model Profitability &amp; Funding</td>
  <td>Consultant for Market Assessment and Marketing Strategy</td>
  <td>Consultant for Management Team &amp; Strategic Partnerships</td>
  <td>Consultant for Reimbursement</td>
  <td>Consultant for Regulatory</td>
</tr>
```

**Important Notes:**
- Replace `X` with the actual row number (10, 11, 12, ... 163)
- For URLs: Use `<a href="URL" target="_blank" rel="noopener">URL</a>` format
- For "NA" values: Use `NA` (not `--`)
- For empty consultant fields: Use `--`
- Escape HTML entities: `&` becomes `&amp;`, `<` becomes `&lt;`, etc.

### Option B: Automated Script (if you have CSV/Excel data)
A Python script can be created to convert CSV/Excel data into HTML table rows. This would:
1. Read your CSV/Excel file
2. Generate HTML `<tr>` blocks for each row
3. Handle URL formatting, HTML escaping, and NA values
4. Output ready-to-paste HTML

**If you have a CSV/Excel file, share it and I can create this conversion script.**

### Option C: Web Scraping (if data is on original website)
If the original website is still accessible, a Python script can:
1. Scrape pages 2-17
2. Extract table data
3. Generate HTML rows in the correct format

## Step 2: Testing After Adding Rows

After adding rows 10-163:

1. **Open `index.html` in a browser**
   - Verify all rows display correctly
   - Check that pagination shows ~17 pages (164 rows ÷ 10 per page)

2. **Test all features:**
   - ✅ Sorting: Click column headers
   - ✅ Global search: Use top-right search box
   - ✅ Per-column search: Use search boxes above each column
   - ✅ Hide/Show columns: Click column names in the toggle section
   - ✅ Pagination: Navigate through pages
   - ✅ Links: Click company websites and LinkedIn links

3. **Verify data integrity:**
   - Check that row indices are sequential (0-163)
   - Ensure all URLs are properly formatted
   - Confirm no broken HTML tags

## Step 3: Hosting on GitHub Pages

### Method 1: Simple GitHub Pages (Recommended)

1. **Create a GitHub repository:**
   ```bash
   cd Nov_30
   git init
   git add index.html
   git commit -m "Initial commit: LBV portfolio table"
   ```

2. **Push to GitHub:**
   - Create a new repository on GitHub (e.g., `lbv-portfolio-table`)
   - Link your local repo:
     ```bash
     git remote add origin https://github.com/YOUR_USERNAME/lbv-portfolio-table.git
     git branch -M main
     git push -u origin main
     ```

3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Under "Source", select "Deploy from a branch"
   - Choose branch: `main`
   - Choose folder: `/ (root)`
   - Click "Save"

4. **Access your site:**
   - Your site will be available at: `https://YOUR_USERNAME.github.io/lbv-portfolio-table/`
   - GitHub Pages typically takes 1-2 minutes to deploy

### Method 2: GitHub Pages with Custom Domain (Optional)

If you have a custom domain:
1. Follow Method 1 steps above
2. In repository Settings → Pages, add your custom domain
3. Add a `CNAME` file in the root with your domain name
4. Configure DNS records as GitHub instructs

### Method 3: Using GitHub Actions (Advanced)

For automatic deployment or if you want to use a different branch:
1. Create `.github/workflows/deploy.yml`
2. Configure GitHub Actions workflow
3. This is overkill for a single HTML file but useful if you plan to add more files

## Step 4: Post-Deployment Checklist

After deploying to GitHub Pages:

- [ ] Site loads correctly at GitHub Pages URL
- [ ] All 164 rows display
- [ ] Sorting works on all columns
- [ ] Search functionality works (global and per-column)
- [ ] Hide/Show columns works
- [ ] Pagination works correctly
- [ ] All links open correctly (test a few)
- [ ] Mobile responsiveness (test on phone/tablet)
- [ ] Cross-browser compatibility (Chrome, Firefox, Safari, Edge)

## Troubleshooting

### Issue: GitHub Pages shows 404
- **Solution:** Make sure `index.html` is in the root of the repository, not in a subfolder
- Check that GitHub Pages is enabled in Settings → Pages

### Issue: DataTables not loading
- **Solution:** The CDN links should work, but if blocked, check browser console for errors
- Verify internet connection (CDN requires internet access)

### Issue: Links not working
- **Solution:** Check that URLs are properly formatted in `<a>` tags
- Verify `target="_blank" rel="noopener"` attributes are present

### Issue: Pagination shows wrong number of pages
- **Solution:** Verify all rows are inside `<tbody>` tags
- Check that row count matches expected (164 rows = ~17 pages at 10 per page)

## Next Steps

1. **Add the remaining rows** (10-163) using one of the methods above
2. **Test locally** before deploying
3. **Deploy to GitHub Pages** following Step 3
4. **Share the GitHub Pages URL** with stakeholders

## Additional Enhancements (Optional)

Once the basic table is working, consider:

- **Export to CSV:** Add a button to export filtered/sorted data
- **Print-friendly CSS:** Add print stylesheet for better printing
- **Responsive improvements:** Enhance mobile experience
- **Loading indicator:** Show loading state while DataTables initializes
- **Row highlighting:** Highlight rows on hover
- **Column width optimization:** Adjust column widths for better readability

