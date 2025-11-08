#!/usr/bin/env python3
"""
BibTeX to HTML Converter for Academic Publications

Converts BibTeX entries to standardized HTML format for personal website.
Supports arXiv preprints, journal publications, and conference papers.

Author: Da-Chuan Lu
Date: November 2025
"""

import re
import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional

try:
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
except ImportError:
    print("Error: bibtexparser not installed")
    print("Install with: pip install bibtexparser")
    sys.exit(1)


class PublicationConverter:
    """Converts BibTeX entries to HTML publication list."""

    def __init__(self, tags_config: Optional[Dict] = None, verbose: bool = False):
        """
        Initialize converter.

        Args:
            tags_config: Dictionary mapping citation keys to tags/keywords
            verbose: Enable verbose output
        """
        self.tags_config = tags_config or {}
        self.verbose = verbose

    def log(self, message: str):
        """Print message if verbose mode enabled."""
        if self.verbose:
            print(f"[INFO] {message}")

    def parse_bibtex(self, bibtex_file: str) -> List[Dict]:
        """
        Parse BibTeX file and return list of entries.

        Args:
            bibtex_file: Path to BibTeX file

        Returns:
            List of parsed BibTeX entries
        """
        self.log(f"Parsing BibTeX file: {bibtex_file}")

        with open(bibtex_file, 'r', encoding='utf-8') as f:
            parser = BibTexParser(common_strings=True)
            parser.ignore_nonstandard_types = False
            bib_database = bibtexparser.load(f, parser=parser)

        self.log(f"Found {len(bib_database.entries)} entries")
        return bib_database.entries

    def format_author_name(self, author: str) -> str:
        """
        Convert BibTeX author format to display format.

        Args:
            author: Author name in format "LastName, FirstName" or "FirstName LastName"

        Returns:
            Formatted name with bold for Da-Chuan Lu
        """
        # Handle "LastName, FirstName" format
        if ',' in author:
            parts = [p.strip() for p in author.split(',')]
            if len(parts) == 2:
                name = f"{parts[1]} {parts[0]}"
            else:
                name = author
        else:
            name = author

        # Clean up extra spaces
        name = ' '.join(name.split())

        # Bold Da-Chuan Lu (case-insensitive match)
        if re.search(r'da-?chuan\s+lu', name, re.IGNORECASE):
            name = f"<strong>{name}</strong>"

        return name

    def parse_authors(self, author_string: str) -> str:
        """
        Parse BibTeX author field and format for HTML.

        Args:
            author_string: BibTeX author field (authors separated by 'and')

        Returns:
            Formatted author list with proper HTML
        """
        # Split by ' and ' (BibTeX standard)
        authors = [a.strip() for a in author_string.split(' and ')]

        # Format each author name
        formatted_authors = [self.format_author_name(a) for a in authors]

        # Join with comma-space
        return ', '.join(formatted_authors)

    def extract_arxiv_id(self, entry: Dict) -> Optional[str]:
        """
        Extract arXiv ID from various BibTeX fields.

        Args:
            entry: BibTeX entry dictionary

        Returns:
            arXiv ID (e.g., "2505.00673") or None
        """
        # Check eprint field
        if 'eprint' in entry:
            return entry['eprint']

        # Check journal field for arXiv preprint
        if 'journal' in entry:
            match = re.search(r'arXiv[: ]+(\d+\.\d+)', entry['journal'])
            if match:
                return match.group(1)

        # Check note field
        if 'note' in entry:
            match = re.search(r'arXiv[: ]+(\d+\.\d+)', entry['note'])
            if match:
                return match.group(1)

        return None

    def get_publication_link(self, entry: Dict) -> str:
        """
        Determine primary link for publication (DOI > arXiv > URL).

        Args:
            entry: BibTeX entry dictionary

        Returns:
            URL for publication
        """
        # Prefer DOI if available
        if 'doi' in entry:
            doi = entry['doi']
            if not doi.startswith('http'):
                return f"https://doi.org/{doi}"
            return doi

        # Use arXiv if available
        arxiv_id = self.extract_arxiv_id(entry)
        if arxiv_id:
            return f"https://arxiv.org/abs/{arxiv_id}"

        # Fall back to URL field
        if 'url' in entry:
            return entry['url']

        # No link available
        return "#"

    def format_venue(self, entry: Dict) -> str:
        """
        Format publication venue (journal, conference, or arXiv).

        Args:
            entry: BibTeX entry dictionary

        Returns:
            Formatted venue string
        """
        year = entry.get('year', '')
        arxiv_id = self.extract_arxiv_id(entry)

        # Check if it's an arXiv-only preprint (has eprint/archivePrefix but no DOI/journal)
        journal = entry.get('journal', '')

        # Case 1: Has eprint/archivePrefix but no DOI and no proper journal
        if arxiv_id and not entry.get('doi') and not journal:
            return f"arXiv:{arxiv_id} ({year})"

        # Case 2: Journal field says "arXiv preprint"
        if 'arxiv preprint' in journal.lower():
            if arxiv_id:
                return f"arXiv:{arxiv_id} ({year})"

        # Case 3: Published paper with DOI and journal
        if 'doi' in entry and 'journal' in entry:
            venue_parts = []

            # Journal name (standardize common abbreviations)
            journal_name = entry['journal']
            journal_name = journal_name.replace('Physical Review B', 'Phys. Rev. B')
            journal_name = journal_name.replace('JHEP', 'JHEP')
            venue_parts.append(journal_name)

            # Volume, issue, pages
            if 'volume' in entry:
                volume = entry['volume']
                if 'number' in entry:
                    volume += f"({entry['number']})"
                venue_parts.append(volume)

            if 'pages' in entry:
                venue_parts.append(entry['pages'])

            venue_str = ' '.join(venue_parts)

            # Add arXiv if available
            if arxiv_id:
                return f"{venue_str} ({year}), arXiv:{arxiv_id}"
            else:
                return f"{venue_str} ({year})"

        # Case 4: Has journal but no DOI (older papers or non-standard venues)
        if 'journal' in entry:
            venue_parts = [journal]

            # Add volume/pages if available
            if 'volume' in entry:
                volume = entry['volume']
                if 'number' in entry:
                    volume += f"({entry['number']})"
                venue_parts.append(volume)

            if 'pages' in entry:
                venue_parts.append(entry['pages'])

            venue_str = ' '.join(venue_parts)

            # Add arXiv if available
            if arxiv_id:
                return f"{venue_str} ({year}), arXiv:{arxiv_id}"
            else:
                return f"{venue_str} ({year})"

        # Case 5: Only arXiv ID available
        if arxiv_id:
            return f"arXiv:{arxiv_id} ({year})"

        # Case 6: No venue information at all
        return f"({year})"

    def clean_latex(self, text: str) -> str:
        """
        Convert LaTeX commands to HTML entities.

        Args:
            text: Text with LaTeX formatting

        Returns:
            Text with HTML formatting
        """
        # Fix common patterns like $p$-ality → p-ality first
        text = re.sub(r'\$([^$]+)\$', r'\1', text)

        # Handle LaTeX subscripts: _{...} or _X
        text = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', text)
        text = re.sub(r'_([0-9A-Za-z])', r'<sub>\1</sub>', text)

        # Handle LaTeX superscripts: ^{...} or ^X
        text = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', text)
        text = re.sub(r'\^([0-9A-Za-z])', r'<sup>\1</sup>', text)

        # Remove curly braces used for grouping (but not those in sub/sup)
        text = re.sub(r'\{([^}]*)\}', r'\1', text)

        # Convert common LaTeX commands
        text = re.sub(r'\\textit\{([^}]*)\}', r'<em>\1</em>', text)
        text = re.sub(r'\\textbf\{([^}]*)\}', r'<strong>\1</strong>', text)
        text = re.sub(r'\\emph\{([^}]*)\}', r'<em>\1</em>', text)

        return text

    def get_tags(self, entry: Dict) -> Tuple[str, str]:
        """
        Get categories and keywords for publication.

        Args:
            entry: BibTeX entry dictionary

        Returns:
            Tuple of (categories, keywords)
        """
        entry_id = entry.get('ID', '')

        if entry_id in self.tags_config:
            config = self.tags_config[entry_id]
            categories = config.get('categories', '')
            keywords = config.get('keywords', '')
            return categories, keywords

        # Try to extract from BibTeX fields
        categories = entry.get('primaryClass', '')
        if not categories and 'archivePrefix' in entry:
            categories = 'arXiv'

        # Keywords might be in keywords or note field
        keywords = entry.get('keywords', entry.get('note', ''))

        return categories, keywords

    def entry_to_html(self, entry: Dict) -> str:
        """
        Convert single BibTeX entry to HTML.

        Args:
            entry: BibTeX entry dictionary

        Returns:
            HTML string for publication
        """
        # Extract fields
        title = self.clean_latex(entry.get('title', 'Untitled'))
        authors = self.parse_authors(entry.get('author', ''))
        venue = self.format_venue(entry)
        link = self.get_publication_link(entry)
        categories, keywords = self.get_tags(entry)

        # Build HTML
        html_lines = [
            '    <li>',
            f'        <a href="{link}">{title}</a>',
            f'        <p>{authors}</p>',
            f'        <p>{venue}</p>',
        ]

        # Add tags if available
        if categories or keywords:
            tag_line = '        <p class="tagp">'
            if categories:
                tag_line += f'<code class="ctag">{categories}</code> '
            if keywords:
                tag_line += keywords
            tag_line += '</p>'
            html_lines.append(tag_line)

        html_lines.append('    </li>')

        return '\n'.join(html_lines)

    def convert(self, bibtex_file: str, output_file: str):
        """
        Convert BibTeX file to HTML publication list.

        Args:
            bibtex_file: Path to input BibTeX file
            output_file: Path to output HTML file
        """
        # Parse BibTeX
        entries = self.parse_bibtex(bibtex_file)

        # Sort by year (descending - newest first)
        entries.sort(key=lambda e: int(e.get('year', '0')), reverse=True)

        # Convert each entry
        html_entries = []
        for entry in entries:
            entry_id = entry.get('ID', 'unknown')
            self.log(f"Converting entry: {entry_id}")
            html_entry = self.entry_to_html(entry)
            html_entries.append(html_entry)

        # Build complete HTML
        html_output = ['<ol class="publication">']
        html_output.extend(html_entries)
        html_output.append('</ol>')

        # Write output
        output_path = Path(output_file)
        output_path.write_text('\n'.join(html_output), encoding='utf-8')

        self.log(f"Output written to: {output_file}")
        print(f"✓ Converted {len(entries)} publications to {output_file}")


def load_tags_config(config_file: str) -> Dict:
    """
    Load tags configuration from JSON file.

    Args:
        config_file: Path to JSON configuration file

    Returns:
        Dictionary of tags configuration
    """
    if not config_file or not Path(config_file).exists():
        return {}

    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    """Main entry point for script."""
    parser = argparse.ArgumentParser(
        description='Convert BibTeX publications to HTML format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python bibtex_to_html.py pub.bib --output publications.html
  python bibtex_to_html.py pub.bib --config tags.json --verbose
        """
    )

    parser.add_argument('bibtex_file', help='Input BibTeX file')
    parser.add_argument('--config', help='Tags configuration JSON file')
    parser.add_argument('--output', default='publications_output.html',
                       help='Output HTML file (default: publications_output.html)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')

    args = parser.parse_args()

    # Validate input file
    if not Path(args.bibtex_file).exists():
        print(f"Error: BibTeX file not found: {args.bibtex_file}")
        sys.exit(1)

    # Load configuration
    tags_config = load_tags_config(args.config)

    # Convert
    converter = PublicationConverter(tags_config=tags_config, verbose=args.verbose)
    converter.convert(args.bibtex_file, args.output)


if __name__ == '__main__':
    main()
