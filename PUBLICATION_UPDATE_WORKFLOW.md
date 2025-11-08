# Publication Update Workflow

A step-by-step guide for updating publications on the website using BibTeX data.

## Quick Reference

```bash
# Navigate to project directory
cd /Users/dachuan/Documents/GitHub/dclu.github.io

# Run conversion
python3 bin/bibtex_to_html.py pub.bib --config bin/tags_config.json --output bin/publications_output.html

# Copy output to publication.html
# Then commit and push changes
```

---

## Complete Workflow

### Step 1: Export BibTeX from Google Scholar

1. Go to [Google Scholar Profile](https://scholar.google.com/citations?user=wLi-G-cAAAAJ&hl=en)
2. Select publications you want to export
3. Click "Export" → Choose "BibTeX"
4. Save or copy the BibTeX entries

### Step 2: Update pub.bib File

**Option A: Add new publications**
```bash
# Open pub.bib and paste new BibTeX entries at the top
nano pub.bib
```

**Option B: Replace entire file**
```bash
# If you have a complete export, replace the entire file
# Make sure to back up the old version first
cp pub.bib pub.bib.backup
cat new_export.bib > pub.bib
```

### Step 3: Update Tags Configuration (if needed)

For new publications, add category and keyword information:

```bash
nano bin/tags_config.json
```

Add entries in this format:
```json
{
  "citation_key": {
    "categories": "cond-mat.str-el, hep-th",
    "keywords": "Non-invertible symmetry, strange correlator, string order"
  }
}
```

**Common Categories:**
- `cond-mat.str-el` - Strongly Correlated Electrons
- `hep-th` - High Energy Physics - Theory
- `cond-mat.supr-con` - Superconductivity
- `DQCP` - Deconfined Quantum Critical Point
- `SMG` - Symmetric Mass Generation

### Step 4: Run BibTeX to HTML Conversion

```bash
python3 bin/bibtex_to_html.py pub.bib \
  --config bin/tags_config.json \
  --output bin/publications_output.html \
  --verbose
```

**What this does:**
- Parses all BibTeX entries from `pub.bib`
- Applies formatting rules for venues, authors, and special characters
- Adds tags from `tags_config.json`
- Generates standardized HTML output
- Displays verbose information about processing

### Step 5: Review Generated HTML

```bash
# View the generated HTML
cat bin/publications_output.html

# Or open in browser for preview
open bin/publications_output.html
```

**Check for:**
- ✓ Proper arXiv formatting (e.g., `arXiv:2406.12151 (2024)`)
- ✓ Journal citations with volume/issue (e.g., `Phys. Rev. B 109(4) 045123 (2024)`)
- ✓ Your name is bolded: `<strong>Da-Chuan Lu</strong>`
- ✓ Special characters rendered correctly (subscripts, superscripts)
- ✓ All publications have proper links (DOI or arXiv)
- ✓ Tags and keywords are present

### Step 6: Update publication.html

1. Open `publication.html` in your editor
2. Find the `<ol class="publication">` section (starts around line 72)
3. Copy the entire content from `bin/publications_output.html`
4. Replace the existing publication list

**Visual Studio Code / Cursor:**
```bash
code publication.html
# Then manually copy/paste the <ol> section
```

**Command line:**
```bash
# Extract just the <ol> section from output
# Then manually update publication.html
```

### Step 7: Test Locally

Start a local web server to preview changes:

```bash
# Option 1: Python HTTP server
python3 -m http.server 8000

# Option 2: If you have Node.js
npx http-server -p 8000

# Then open: http://localhost:8000/publication.html
```

**Verify:**
- Publications display correctly
- Links work (open a few to test)
- Formatting is consistent
- No broken HTML
- Mobile view looks good (resize browser window)

### Step 8: Commit Changes

```bash
# Check what files changed
git status

# Review the changes
git diff publication.html
git diff pub.bib
git diff bin/tags_config.json

# Stage the files
git add publication.html pub.bib bin/tags_config.json bin/publications_output.html

# Create commit
git commit -m "Update publications: Add [paper title] and [other changes]

- Added [N] new publications
- Updated venue information for [specific papers]
- Enhanced tags for [research area]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Step 9: Push to GitHub

```bash
# Push to remote repository
git push origin master
```

**If you encounter authentication issues:**

See [Authentication Troubleshooting](#authentication-troubleshooting) section below.

### Step 10: Verify Live Site

1. Wait 1-2 minutes for GitHub Pages to rebuild
2. Visit [https://dclu.github.io/publication.html](https://dclu.github.io/publication.html)
3. Hard refresh browser (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows/Linux)
4. Verify all changes appear correctly

---

## Common Tasks

### Adding a Single New Publication

1. Get BibTeX from Google Scholar or journal website
2. Add to top of `pub.bib`
3. Add entry to `bin/tags_config.json` with the citation key
4. Run conversion script
5. Update `publication.html`
6. Test, commit, push

### Updating Publication Status (arXiv → Published)

When a paper gets published:

1. Update the BibTeX entry in `pub.bib` with:
   - `doi` field
   - `journal` field with full name
   - `volume`, `number`, `pages` fields
   - Keep the `eprint` field for arXiv ID

Example:
```bibtex
@article{Lu:2024xyz,
    author = "Lu, Da-Chuan and Others",
    title = "{Paper Title}",
    doi = "10.1103/PhysRevB.109.045123",
    journal = "Physical Review B",
    volume = "109",
    number = "4",
    pages = "045123",
    year = "2024",
    eprint = "2302.12731",
    archivePrefix = "arXiv",
    primaryClass = "cond-mat.str-el"
}
```

2. Run conversion script
3. The output will show: `Phys. Rev. B 109(4) 045123 (2024), arXiv:2302.12731`

### Fixing Formatting Issues

**Problem: Author name not bolded**

Ensure BibTeX uses standard format:
```bibtex
author = "Lu, Da-Chuan and Sun, Zhengdi"
```

**Problem: Missing arXiv ID**

Add these fields:
```bibtex
eprint = "2406.12151",
archivePrefix = "arXiv",
```

**Problem: Special characters not rendering**

Use LaTeX notation in BibTeX:
- Subscripts: `La_{3}Ni_{2}O_{7}` → La₃Ni₂O₇
- Superscripts: `x^{2}` → x²
- Math mode: `$p$-ality` → p-ality

**Problem: Wrong venue format**

Check the script's journal abbreviation mapping in `bin/bibtex_to_html.py` (lines 202-204):
```python
journal_name = journal_name.replace('Physical Review B', 'Phys. Rev. B')
journal_name = journal_name.replace('JHEP', 'JHEP')
```

Add more mappings if needed.

---

## Authentication Troubleshooting

If `git push` fails with authentication error:

### Option 1: Use SSH (Recommended)

```bash
# Check current remote URL
git remote -v

# Change to SSH URL
git remote set-url origin git@github.com:dclu/dclu.github.io.git

# Test SSH connection
ssh -T git@github.com

# Push again
git push origin master
```

### Option 2: Use Personal Access Token

1. Generate token at: https://github.com/settings/tokens
2. Select scopes: `repo` (full control)
3. Copy the token
4. Clear cached credentials:
```bash
git credential reject <<EOF
protocol=https
host=github.com
EOF
```
5. Push again - use token as password when prompted

### Option 3: Use GitHub CLI

```bash
# Install gh if not present
brew install gh  # macOS
# or: sudo apt install gh  # Linux

# Authenticate
gh auth login

# Push
git push origin master
```

---

## File Structure Reference

```
dclu.github.io/
├── publication.html          # Main publication page (edit this)
├── pub.bib                   # Source BibTeX data (update this)
├── PUBLICATION_UPDATE_WORKFLOW.md  # This file
├── CLAUDE.md                 # Technical documentation
├── bin/
│   ├── bibtex_to_html.py    # Conversion script
│   ├── tags_config.json     # Category/keyword mappings
│   ├── publications_output.html  # Generated HTML (intermediate)
│   └── README.md            # Script documentation
└── css/
    └── main.css             # Styling (don't usually need to edit)
```

---

## Maintenance Schedule

**After each new publication:**
- Add BibTeX entry
- Run conversion
- Update website

**When paper status changes (arXiv → published):**
- Update BibTeX with DOI and journal info
- Run conversion
- Update website

**Quarterly review:**
- Verify all links work
- Check for any formatting inconsistencies
- Update any changed journal abbreviations
- Review tags/keywords for accuracy

---

## Tips and Best Practices

1. **Always test locally** before pushing to production
2. **Keep pub.bib sorted** by year (newest first) for easier management
3. **Use consistent citation keys** (e.g., `Lu:2024xyz` format)
4. **Backup before major changes**: `cp pub.bib pub.bib.backup`
5. **Commit frequently** with descriptive messages
6. **Check mobile view** - many visitors use phones
7. **Validate BibTeX** before running conversion (use online validators if unsure)
8. **Keep tags_config.json in sync** with pub.bib entries

---

## Advanced Usage

### Batch Update from Conference Proceedings

```bash
# Download proceedings BibTeX
curl -o conference.bib "https://..."

# Merge with existing
cat conference.bib >> pub.bib

# Remove duplicates (manual review recommended)
# Then run normal workflow
```

### Preview Specific Entry

```bash
# Create temporary file with single entry
grep -A 15 "@article{Lu:2024xyz" pub.bib > temp.bib

# Convert just that entry
python3 bin/bibtex_to_html.py temp.bib --output temp_output.html

# Review
cat temp_output.html
```

### Validate All Links

```bash
# Extract all URLs from publication.html
grep -o 'href="[^"]*"' publication.html | grep -v "#" | sort -u

# Test them (requires curl)
for url in $(grep -o 'href="[^"]*"' publication.html | cut -d'"' -f2 | grep http); do
    echo "Testing: $url"
    curl -I "$url" 2>&1 | head -1
done
```

---

## Getting Help

**Documentation:**
- Technical details: See [CLAUDE.md](CLAUDE.md)
- Script usage: See [bin/README.md](bin/README.md)
- This workflow: [PUBLICATION_UPDATE_WORKFLOW.md](PUBLICATION_UPDATE_WORKFLOW.md)

**Common Issues:**
- BibTeX parsing errors → Check for unmatched braces `{}` in pub.bib
- Missing tags → Add entry to `bin/tags_config.json`
- Formatting problems → Review LaTeX conversion in script
- Git authentication → See [Authentication Troubleshooting](#authentication-troubleshooting)

**Contact:**
- Email: dclu137@gmail.com
- GitHub: [@dclu](https://github.com/dclu)

---

**Last Updated:** November 2025
**Version:** 1.0
