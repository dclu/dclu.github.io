# Publication Page Improvement Project

## Overview
This document describes the automated system for maintaining the publication page on Da-Chuan Lu's personal website. The system converts BibTeX entries from Google Scholar into standardized HTML format.

## Project Structure

```
dclu.github.io/
├── CLAUDE.md                    # This documentation file
├── publication.html             # Publications page
├── pub.bib                      # BibTeX export from Google Scholar
├── css/
│   └── main.css                # Styles with publication enhancements
├── bin/
│   ├── bibtex_to_html.py       # Conversion script
│   ├── tags_config.json        # Category and keyword mappings
│   └── README.md               # Script documentation
└── ...
```

## Publication Template

Each publication follows this standardized HTML structure:

```html
<li>
    <a href="[LINK_URL]">[TITLE]</a>
    <p>[AUTHORS_WITH_FORMATTING]</p>
    <p>[VENUE] ([YEAR])[OPTIONAL_ARXIV]</p>
    <p class="tagp">
        <code class="ctag">[CATEGORIES]</code>
        [KEYWORDS]
    </p>
</li>
```

### Publication Types

**Type A - arXiv Preprint:**
```html
<p>arXiv:2505.00673 (2025)</p>
```

**Type B - Published with arXiv:**
```html
<p>Phys. Rev. B 108, 205117 (2023), arXiv:2307.12223</p>
```

**Type C - Published Only:**
```html
<p>Scientific Reports 9(1), 664 (2019)</p>
```

### Author Formatting
- "Da-Chuan Lu" is wrapped in `<strong>` tags for emphasis
- All other authors appear in normal text
- Authors are separated by comma-space ", "

### Special Characters
- Subscripts: `<sub>3</sub>` → ₃
- Superscripts: `<sup>2</sup>` → ²
- LaTeX math symbols are converted to HTML entities

## Workflow: Adding New Publications

### Step 1: Export from Google Scholar
1. Go to your [Google Scholar profile](https://scholar.google.com/citations?user=wLi-G-cAAAAJ&hl=en)
2. Select publications to export
3. Click "Export" → "BibTeX"
4. Save or copy the BibTeX entries

### Step 2: Update pub.bib
Add the new BibTeX entries to `pub.bib`:

```bash
# Append new entries to pub.bib
cat new_publications.bib >> pub.bib
```

### Step 3: Add Tags/Keywords
Edit `bin/tags_config.json` to add categories and keywords for new publications:

```json
{
  "lu2025intrinsic": {
    "categories": "hep-th",
    "keywords": "Non-invertible symmetry, SPT, Mixed anomaly"
  }
}
```

The citation key (e.g., `lu2025intrinsic`) matches the BibTeX entry identifier.

### Step 4: Run Conversion Script
```bash
cd bin
python3 bibtex_to_html.py ../pub.bib --config tags_config.json --output publications_output.html
```

**Script Options:**
- `--config`: Path to tags configuration file
- `--output`: Output HTML file name
- `--verbose`: Show detailed processing information

### Step 5: Update publication.html
1. Open the generated `publications_output.html`
2. Copy the `<ol class="publication">` content
3. Replace the corresponding section in `publication.html`
4. Verify the output in a browser

### Step 6: Commit Changes
```bash
git add publication.html pub.bib bin/tags_config.json
git commit -m "Update publications with [new paper title]"
git push
```

## BibTeX to HTML Conversion Script

### Features
- **Automatic parsing**: Extracts title, authors, venue, year, DOI, arXiv ID
- **Author formatting**: Automatically bolds "Da-Chuan Lu" (case-insensitive)
- **Link generation**: Creates proper arXiv and DOI URLs
- **Special character handling**: Converts LaTeX symbols to HTML
- **Sorting**: Orders publications by year (newest first)
- **Tag integration**: Merges categories and keywords from config

### Dependencies
```bash
pip install bibtexparser
```

### Manual Adjustments

Some fields may require manual editing:

**1. Tags and Keywords**
The script cannot auto-detect research categories. Always update `tags_config.json` before running the conversion.

**2. Special Chemical Formulas**
Complex subscripts like La₃Ni₂O₇ need manual HTML:
```html
La<sub>3</sub>Ni<sub>2</sub>O<sub>7</sub>
```

**3. Journal Name Formatting**
Verify journal abbreviations match your preferred style:
- `Phys. Rev. B` (preferred)
- `Physical Review B` (BibTeX default)

## CSS Enhancements

### Publication Styling
Located in `css/main.css`:

```css
.publication li {
    margin: 20px 0;
}

.publication a:hover {
    text-decoration: underline;
}

.tagp {
    color: rgb(99, 99, 99);
}

.ctag {
    color: crimson;
    background-color: #f1f1f1;
    padding-left: 4px;
    padding-right: 4px;
}
```

### Responsive Design
Publications remain readable on all screen sizes with the existing responsive breakpoints at 768px.

## Troubleshooting

### Issue: BibTeX Parsing Errors
**Symptom**: Script fails with parsing error
**Solution**: Check for unmatched braces `{}` or special characters in BibTeX

### Issue: Author Name Not Bolded
**Symptom**: "Da-Chuan Lu" appears in normal text
**Solution**: Verify BibTeX uses one of these formats:
- `Lu, Da-Chuan`
- `Da-Chuan Lu`
- `Lu, Dachuan`

### Issue: Missing arXiv Links
**Symptom**: No arXiv URL in output
**Solution**: Ensure BibTeX has `eprint` field or arXiv URL in `journal` field

### Issue: Tags Not Appearing
**Symptom**: Categories/keywords missing from output
**Solution**: Add entry to `tags_config.json` with matching citation key

## Future Enhancements

**Planned Improvements:**
- Automated Google Scholar API integration (if available)
- Dark mode support
- Publication search/filter functionality
- Structured data (Schema.org) for better SEO
- Citation metrics display
- Export to CV format

## Template Standards

### Indentation
- Use 4 spaces per indentation level
- No tabs
- No trailing whitespace

### HTML Structure
- Maintain semantic HTML5
- Use proper heading hierarchy
- Keep ARIA attributes for accessibility

### Formatting Conventions
- Single space after periods
- Comma-space between authors
- Consistent arXiv category format: `cond-mat.str-el, hep-th`
- Keywords in lowercase unless proper nouns

## Version History

- **v1.0 (2025-11)**: Initial implementation
  - BibTeX conversion script
  - Standardized HTML template
  - CSS enhancements
  - Documentation

## Contact & Support

For issues or questions about this system:
- Email: dclu137@gmail.com
- GitHub: [@dclu](https://github.com/dclu)

---

**Last Updated**: November 2025
**Maintained By**: Da-Chuan Lu
**Generated With**: Claude Code
