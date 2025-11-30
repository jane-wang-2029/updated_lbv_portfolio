# Uploading to GitHub Pages

## Quick Steps

### Option 1: Using GitHub Web Interface (Easiest)

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Repository name: `lbv-portfolio-table` (or any name you prefer)
   - Make it **Public** (required for free GitHub Pages)
   - Don't initialize with README, .gitignore, or license
   - Click "Create repository"

2. **Upload files:**
   - On the new repository page, click "uploading an existing file"
   - Drag and drop these files:
     - `index.html`
     - `lbv_portfolio_full.csv` (optional - if you want the data available)
   - Click "Commit changes"

3. **Enable GitHub Pages:**
   - Go to repository **Settings** → **Pages**
   - Under "Source", select **"Deploy from a branch"**
   - Branch: `main` (or `master`)
   - Folder: `/ (root)`
   - Click **Save**

4. **Access your site:**
   - Your site will be live at: `https://YOUR_USERNAME.github.io/lbv-portfolio-table/`
   - It may take 1-2 minutes to deploy

### Option 2: Using Git Command Line (Recommended)

1. **Initialize git repository:**
   ```bash
   cd "/Users/shangw/MIT Dropbox/Shang Wang/therapeutic_area_project_JW/Nov_30"
   git init
   ```

2. **Create .gitignore** (optional but recommended):
   ```
   # Python
   __pycache__/
   *.pyc
   *.pyo
   .DS_Store
   ```

3. **Add files:**
   ```bash
   git add index.html
   git add lbv_portfolio_full.csv
   git add *.py
   git add *.md
   ```

4. **Commit:**
   ```bash
   git commit -m "Initial commit: LBV portfolio table with 164 companies"
   ```

5. **Create repository on GitHub:**
   - Go to https://github.com/new
   - Create repository (don't initialize with README)
   - Copy the repository URL (e.g., `https://github.com/YOUR_USERNAME/lbv-portfolio-table.git`)

6. **Connect and push:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/lbv-portfolio-table.git
   git branch -M main
   git push -u origin main
   ```

7. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main` / folder `/ (root)`
   - Save

## Files to Include

**Required:**
- `index.html` - The main table file

**Optional but useful:**
- `lbv_portfolio_full.csv` - The data file
- `add_lbv_column.py` - Script for adding columns
- `convert_csv_to_html_rows.py` - Helper script
- `EXTENSION_PLAN.md` - Documentation
- `README.md` - Project description (create one!)

## Custom Domain (Optional)

If you have a custom domain:
1. Add a `CNAME` file in the repository root with your domain name
2. Configure DNS records as GitHub instructs

## Troubleshooting

**Issue: GitHub Pages shows 404**
- Make sure `index.html` is in the root directory
- Check that GitHub Pages is enabled in Settings → Pages
- Wait 1-2 minutes for deployment

**Issue: Table doesn't load**
- Check browser console (F12) for errors
- Ensure CDN links are accessible (requires internet)
- Verify all JavaScript is properly formatted

**Issue: Changes not showing**
- GitHub Pages can take 1-2 minutes to update
- Try hard refresh (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)
- Check repository Settings → Pages for deployment status

