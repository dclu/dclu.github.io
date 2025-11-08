# Publication Management Scripts

This directory contains scripts for managing the publication page on Da-Chuan Lu's personal website.

## Contents

- **bibtex_to_html.py** - Converts BibTeX entries to HTML
- **tags_config.json** - Category and keyword mappings for publications
- **README.md** - This documentation file

## Quick Start

### 1. Install Dependencies

```bash
pip install bibtexparser
```

### 2. Convert BibTeX to HTML

```bash
python bibtex_to_html.py ../pub.bib --config tags_config.json --output publications_output.html
```

### 3. Update website

Copy the generated HTML from `publications_output.html` and paste it into `../publication.html`.

## Usage

### Basic Conversion

```bash
python bibtex_to_html.py ../pub.bib
```

This generates `publications_output.html` with default formatting.

### With Tags Configuration

```bash
python bibtex_to_html.py ../pub.bib --config tags_config.json
```

This includes arXiv categories and research keywords from `tags_config.json`.

### Verbose Mode

```bash
python bibtex_to_html.py ../pub.bib --config tags_config.json --verbose
```

Shows detailed processing information for debugging.

### Custom Output File

```bash
python bibtex_to_html.py ../pub.bib --output custom_name.html
```

## Tags Configuration

The `tags_config.json` file maps BibTeX citation keys to arXiv categories and research keywords.

### Format

```json
{
  "citation_key": {
    "categories": "arxiv-category1, arxiv-category2",
    "keywords": "keyword1, keyword2, keyword3"
  }
}
```

### Example

```json
{
  "lu2025strange": {
    "categories": "cond-mat.str-el, hep-th",
    "keywords": "Non-invertible symmetry, strange correlator, string order"
  }
}
```

### Common Categories

- `cond-mat.str-el` - Strongly Correlated Electrons
- `hep-th` - High Energy Physics - Theory
- `cond-mat.supr-con` - Superconductivity
- `DQCP` - Deconfined Quantum Critical Point
- `SMG` - Symmetric Mass Generation

## Script Features

### Author Formatting

- Automatically bolds "Da-Chuan Lu" in author lists
- Handles various name formats:
  - `Lu, Da-Chuan`
  - `Da-Chuan Lu`
  - `Lu, Dachuan`

### Link Generation

Priority order for publication links:
1. DOI (if available)
2. arXiv URL
3. Other URL from BibTeX

### Publication Types

**Type A - arXiv Preprint:**
```
arXiv:2505.00673 (2025)
```

**Type B - Published with arXiv:**
```
Phys. Rev. B 108, 205117 (2023), arXiv:2307.12223
```

**Type C - Published Only:**
```
Scientific Reports 9(1), 664 (2019)
```

### Special Character Handling

The script automatically converts:
- LaTeX math symbols: `$p$` → `p`
- Subscripts: `_3` → `₃`
- Superscripts: `^2` → `²`
- LaTeX commands: `\textit{}`, `\textbf{}`

## Workflow

### Adding New Publications

1. **Export from Google Scholar**
   - Go to your profile
   - Select publications → Export → BibTeX
   - Save to `pub.bib` or copy entries

2. **Update pub.bib**
   ```bash
   cat new_publications.bib >> ../pub.bib
   ```

3. **Add tags for new entries**
   - Edit `tags_config.json`
   - Add categories and keywords

4. **Run conversion**
   ```bash
   python bibtex_to_html.py ../pub.bib --config tags_config.json
   ```

5. **Update website**
   - Copy content from `publications_output.html`
   - Paste into `../publication.html`
   - Replace the `<ol class="publication">` section

6. **Commit changes**
   ```bash
   git add ../publication.html ../pub.bib tags_config.json
   git commit -m "Update publications"
   git push
   ```

## Troubleshooting

### Problem: bibtexparser not found

**Solution:**
```bash
pip install bibtexparser
```

### Problem: BibTeX parsing error

**Cause:** Malformed BibTeX (unmatched braces, special characters)

**Solution:** Check the BibTeX file for syntax errors

### Problem: Author name not bolded

**Cause:** Name format doesn't match expected patterns

**Solution:** Ensure BibTeX uses standard format: `Lu, Da-Chuan`

### Problem: Missing tags

**Cause:** Citation key not in `tags_config.json`

**Solution:** Add entry to config file with matching citation key

### Problem: Incorrect journal format

**Cause:** Non-standard abbreviation in BibTeX

**Solution:** Manually edit the generated HTML or update the script's journal mapping

## Advanced Usage

### Filtering Entries

To process only specific entries, create a separate BibTeX file:

```bash
# Create filtered file
grep -A 10 "@article{lu2025" ../pub.bib > recent.bib

# Convert filtered file
python bibtex_to_html.py recent.bib --config tags_config.json
```

### Batch Processing

Process multiple BibTeX files:

```bash
for file in *.bib; do
    python bibtex_to_html.py "$file" --output "${file%.bib}.html"
done
```

## File Format Reference

### Input: BibTeX

Standard BibTeX format with fields:
- `title` - Publication title
- `author` - Authors (separated by ' and ')
- `journal` - Journal name or "arXiv preprint"
- `year` - Publication year
- `volume`, `number`, `pages` - Citation details
- `doi` - DOI identifier
- `eprint` - arXiv ID
- `url` - Publication URL

### Output: HTML

Standardized HTML structure:

```html
<ol class="publication">
    <li>
        <a href="[link]">[title]</a>
        <p>[authors]</p>
        <p>[venue] ([year])</p>
        <p class="tagp">
            <code class="ctag">[categories]</code>
            [keywords]
        </p>
    </li>
    <!-- More entries... -->
</ol>
```

## Maintenance

### Regular Updates

It's recommended to update your publications:
- After each new paper is published
- When paper status changes (arXiv → published)
- Quarterly review for accuracy

### Version Control

Always commit these files together:
- `pub.bib` - Source BibTeX data
- `tags_config.json` - Tag mappings
- `../publication.html` - Output HTML

## Support

For issues or questions:
- Email: dclu137@gmail.com
- GitHub: [@dclu](https://github.com/dclu)

---

**Last Updated**: November 2025
