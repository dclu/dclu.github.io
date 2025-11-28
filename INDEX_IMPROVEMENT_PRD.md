# Product Requirements Document (PRD)
## Homepage Improvement Project

**Project**: Index.html Enhancement with SEO and Content Structure
**Version**: 1.0
**Date**: November 2025
**Author**: Da-Chuan Lu

---

## 1. Executive Summary

This PRD outlines improvements to the personal homepage (index.html) to enhance discoverability, readability, and user experience while maintaining the current clean, minimalist design aesthetic.

### Selected Improvements
1. **Enhanced meta tags and SEO** (Suggestion #1)
2. **Structured Recent Events section** (Suggestion #2)
3. **Separate Research Interests section** (Suggestion #3)
4. **News/Highlights section** (Suggestion #5)
5. **Accessibility improvements** (Suggestion #7)
6. **Last updated timestamp** (Suggestion #10)

### Goals
- Improve search engine visibility for academic searches
- Make content more scannable and organized
- Enhance accessibility for screen readers
- Keep existing visual style and layout unchanged
- Maintain mobile responsiveness

---

## 2. Current State Analysis

### Existing Structure
```
index.html (100 lines)
├── Header (site name)
├── Sidebar navigation
│   ├── Home, Publications, Teaching, Fun
│   └── Social links (Email, Scholar, GitHub)
└── Main content
    ├── Short Bio (2 paragraphs)
    ├── Email contact
    ├── Recent Events (dense paragraph)
    └── Recent Talks (collapsible list)
```

### Strengths
- Clean, minimal design
- Good semantic HTML structure
- Mobile responsive
- Fast loading

### Weaknesses
- Generic meta description ("Da-Chuan Lu's homepage")
- Research interests buried in bio paragraph
- Recent events are hard to scan (one long paragraph with semicolons)
- No structured data for search engines
- Missing accessibility features (skip links, ARIA labels)
- No indication of page freshness

---

## 3. Requirements

### 3.1 SEO Enhancements (Priority: HIGH)

**Requirement ID**: SEO-001
**Title**: Enhanced Meta Description
**Description**: Replace generic meta description with specific, keyword-rich description

**Current**:
```html
<meta name="description" content="Da-Chuan Lu's homepage">
```

**Required**:
```html
<meta name="description" content="Da-Chuan Lu - Postdoctoral Fellow at University of Colorado Boulder and Harvard University studying condensed matter theory, deconfined quantum criticality, symmetric mass generation, and generalized symmetries in quantum field theory">
```

**Acceptance Criteria**:
- [ ] Description is 150-160 characters (optimal for Google snippets)
- [ ] Includes current position and institutions
- [ ] Contains 3-5 key research areas
- [ ] Natural language, not keyword stuffing

---

**Requirement ID**: SEO-002
**Title**: Enhanced Keywords Meta Tag
**Description**: Expand keywords to include specific research areas

**Current**:
```html
<meta name="keywords" content="Theoretical physics, Condensed matter physics, High energy physics">
```

**Required**:
```html
<meta name="keywords" content="Da-Chuan Lu, theoretical physics, condensed matter theory, deconfined quantum criticality, symmetric mass generation, generalized symmetry, non-invertible symmetry, topological phases, SPT phases, fermi surface anomaly, quantum field theory, high energy physics, UCSD, Harvard, University of Colorado Boulder">
```

**Acceptance Criteria**:
- [ ] Includes full name
- [ ] Lists specific research topics (not just broad fields)
- [ ] Includes current and former institutions
- [ ] 10-15 relevant keywords

---

**Requirement ID**: SEO-003
**Title**: Open Graph Meta Tags
**Description**: Add Open Graph tags for better social media sharing

**Required**:
```html
<meta property="og:title" content="Da-Chuan Lu - Theoretical Physicist">
<meta property="og:description" content="Postdoctoral Fellow at CU Boulder & Harvard studying condensed matter theory, quantum criticality, and generalized symmetries">
<meta property="og:type" content="website">
<meta property="og:url" content="https://dclu.github.io/">
<meta property="og:image" content="https://dclu.github.io/images/profile.jpg">
```

**Acceptance Criteria**:
- [ ] OG title is concise and professional
- [ ] OG description is 60-80 characters
- [ ] OG type is set to "website"
- [ ] OG URL points to homepage
- [ ] OG image tag included (even if image not yet available)

---

**Requirement ID**: SEO-004
**Title**: Schema.org Structured Data
**Description**: Add JSON-LD structured data for person entity

**Required**:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Da-Chuan Lu",
  "jobTitle": "Postdoctoral Fellow",
  "description": "Theoretical physicist specializing in condensed matter theory and quantum field theory",
  "affiliation": [
    {
      "@type": "Organization",
      "name": "University of Colorado Boulder",
      "url": "https://www.colorado.edu/physics/"
    },
    {
      "@type": "Organization",
      "name": "Harvard University",
      "url": "https://cmt.physics.harvard.edu/"
    }
  ],
  "alumniOf": [
    {
      "@type": "Organization",
      "name": "University of California San Diego"
    },
    {
      "@type": "Organization",
      "name": "Nanjing University"
    }
  ],
  "email": "dclu137@gmail.com",
  "url": "https://dclu.github.io",
  "sameAs": [
    "https://scholar.google.com/citations?user=wLi-G-cAAAAJ",
    "https://github.com/dclu"
  ],
  "knowsAbout": [
    "Condensed Matter Physics",
    "Quantum Field Theory",
    "Deconfined Quantum Criticality",
    "Symmetric Mass Generation",
    "Generalized Symmetry",
    "Topological Phases"
  ]
}
</script>
```

**Acceptance Criteria**:
- [ ] Valid JSON-LD format
- [ ] @type is "Person"
- [ ] Includes current affiliations with URLs
- [ ] Includes alumni institutions
- [ ] Lists research areas in "knowsAbout"
- [ ] Links to Google Scholar and GitHub
- [ ] Validates at https://validator.schema.org/

---

### 3.2 Content Restructuring (Priority: HIGH)

**Requirement ID**: CONTENT-001
**Title**: Research Interests Section
**Description**: Extract research interests from bio paragraph into dedicated section

**Current**: Research interests are embedded in second paragraph of bio

**Required**:
```html
<h3>Research Interests</h3>
<ul class="research-interests">
    <li>Deconfined Quantum Criticality</li>
    <li>Symmetric Mass Generation</li>
    <li>Generalized Symmetry & Non-Invertible Symmetry</li>
    <li>Strongly Correlated Electronic States</li>
    <li>Topological Phases & SPT Phases</li>
    <li>Quantum Information Theory</li>
</ul>
```

**Acceptance Criteria**:
- [ ] Appears after bio, before Recent Events
- [ ] Uses unordered list format
- [ ] Lists 5-7 specific research areas
- [ ] Each item is concise (3-6 words)
- [ ] Maintains visual consistency with site design

**Content Changes**:
- Remove research interests sentence from bio paragraph
- Condense bio to focus on positions and background only

---

**Requirement ID**: CONTENT-002
**Title**: Restructured Recent Events
**Description**: Convert dense paragraph into structured timeline list

**Current**: Single paragraph with semicolon-separated events

**Required**:
```html
<h3>Recent Events</h3>
<ul class="event-list">
    <li><strong>Jan 2025</strong> - <a href="https://www.kitp.ucsb.edu/activities/gensym25">KITP Program</a>: Generalized Symmetries in Quantum Field Theory: High Energy Physics, Condensed Matter, and Quantum Gravity</li>
    <li><strong>Fall 2024</strong> - <a href="https://scgp.stonybrook.edu/archives/42481">SCGP Program</a>: Applications of Generalized Symmetries and Topological Defects to Quantum Matter</li>
    <li><strong>Summer 2024</strong> - <a href="https://www.ias.edu/pitp">PiTP 2024</a>: Quantum Matter Summer School at IAS</li>
    <li><strong>Summer 2024</strong> - <a href="https://scgp.stonybrook.edu/archives/39956">SCGP Program</a>: Symmetric Mass Generation, Topological Phases and Lattice Chiral Gauge Theories</li>
    <li><strong>Spring 2024</strong> - <a href="https://www.kitp.ucsb.edu/activities/gapless24">KITP Program</a>: Correlated Gapless Quantum Matter</li>
    <li><strong>2023</strong> - <a href="https://pccm.princeton.edu/education/psscmp">PSSCMP 2023</a>: "Fractionalization, criticality and unconventional quantum materials"</li>
    <li><strong>2023</strong> - <a href="https://sites.google.com/colorado.edu/tasi-2023-wiki/">TASI 2023</a>: Aspects of Symmetry</li>
    <li><strong>2023</strong> - <a href="https://online.kitp.ucsb.edu/online/qcrystal-c23/">KITP Conference</a>: Topology, Symmetry and Interactions in Crystals</li>
</ul>
```

**Acceptance Criteria**:
- [ ] Events listed in reverse chronological order (newest first)
- [ ] Each event has date/time period in bold
- [ ] Event name is hyperlinked to program website
- [ ] Brief description/subtitle included where relevant
- [ ] Maximum 8-10 most recent events (can trim older ones)
- [ ] Consistent date formatting

---

**Requirement ID**: CONTENT-003
**Title**: News & Highlights Section
**Description**: Add news section for recent career updates and achievements

**Required**:
```html
<h3>News & Highlights</h3>
<ul class="news-list">
    <li><strong>Sep 2024</strong> - Started joint postdoctoral position at University of Colorado Boulder and Harvard University</li>
    <li><strong>Jun 2024</strong> - Successfully defended Ph.D. thesis at UC San Diego</li>
    <li><strong>Jun 2024</strong> - New preprint on G-ality defects in 2D quantum field theories (arXiv:2406.12151)</li>
    <li><strong>2024</strong> - Paper on strange SPT correlators published in arXiv:2505.00673</li>
</ul>
```

**Acceptance Criteria**:
- [ ] Appears after Research Interests, before Recent Events
- [ ] Lists 3-5 most recent highlights
- [ ] Includes career milestones (positions, graduation)
- [ ] Includes recent publications (1-2 most recent)
- [ ] Date in bold, followed by description
- [ ] Can be updated easily (no hard-coded HTML complexity)

---

### 3.3 Accessibility Improvements (Priority: MEDIUM)

**Requirement ID**: ACCESS-001
**Title**: Skip to Main Content Link
**Description**: Add skip link for keyboard navigation

**Required**:
```html
<body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <!-- existing header and navigation -->
    <main role="main" id="main-content">
```

**Acceptance Criteria**:
- [ ] Link appears at very top of body
- [ ] Hidden by default (positioned off-screen)
- [ ] Visible when focused via keyboard (Tab key)
- [ ] Links to main content area with id="main-content"
- [ ] Styled according to site design when visible

---

**Requirement ID**: ACCESS-002
**Title**: ARIA Labels for Navigation
**Description**: Add semantic labels for screen readers

**Current**:
```html
<menu id="sidebar">
```

**Required**:
```html
<nav id="sidebar" role="navigation" aria-label="Main navigation">
    <div class="content">
        <ul class="submenu-collections" aria-label="Page navigation">
            <!-- existing items -->
        </ul>
        <ul class="menu-main" aria-label="Social links">
            <!-- existing items -->
        </ul>
    </div>
</nav>
```

**Acceptance Criteria**:
- [ ] Change `<menu>` to `<nav>` (more semantic)
- [ ] Add aria-label to main navigation
- [ ] Add aria-label to submenu sections
- [ ] Add aria-label to social links section
- [ ] No visual changes to layout

---

**Requirement ID**: ACCESS-003
**Title**: Improved Heading Hierarchy
**Description**: Ensure proper heading structure

**Current**: Multiple `<h3 id="home">` tags (incorrect)

**Required**:
```html
<h2>Short Bio</h2>
<!-- bio content -->

<h2>Research Interests</h2>
<!-- interests list -->

<h2>News & Highlights</h2>
<!-- news list -->

<h2>Recent Events</h2>
<!-- events list -->

<h2>Recent Talks</h2>
<!-- talks details -->
```

**Acceptance Criteria**:
- [ ] Only one h1 per page (site title)
- [ ] All main sections use h2
- [ ] Subsections use h3 (if needed)
- [ ] No skipping heading levels
- [ ] Remove duplicate id="home" attributes

---

### 3.4 Metadata Improvements (Priority: LOW)

**Requirement ID**: META-001
**Title**: Last Updated Timestamp
**Description**: Add visible timestamp at page bottom

**Required**:
```html
<main role="main" id="main-content">
    <!-- existing content -->

    <footer class="page-footer">
        <p class="last-updated">Last updated: November 2025</p>
    </footer>
</main>
```

**Acceptance Criteria**:
- [ ] Appears at bottom of main content area
- [ ] Uses format "Last updated: Month YYYY"
- [ ] Styled subtly (smaller text, gray color)
- [ ] Easy to update manually

---

## 4. Design Specifications

### 4.1 CSS Requirements

**New CSS Classes Needed**:

```css
/* Research interests list */
.research-interests {
    list-style: none;
    padding-left: 0;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 10px;
}

.research-interests li {
    padding: 8px 12px;
    background-color: #f7fafc;
    border-left: 3px solid #2c5282;
}

/* Event list */
.event-list {
    line-height: 1.8;
    list-style: none;
    padding-left: 0;
}

.event-list li {
    margin-bottom: 12px;
    padding-left: 20px;
    position: relative;
}

.event-list li:before {
    content: "•";
    color: #2c5282;
    position: absolute;
    left: 0;
}

/* News list */
.news-list {
    list-style: none;
    padding-left: 0;
}

.news-list li {
    padding: 10px 0;
    border-bottom: 1px solid #e2e8f0;
}

.news-list li:last-child {
    border-bottom: none;
}

/* Skip link for accessibility */
.skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: #2c5282;
    color: white;
    padding: 8px;
    text-decoration: none;
    z-index: 100;
}

.skip-link:focus {
    top: 0;
}

/* Footer */
.page-footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #e2e8f0;
}

.last-updated {
    font-size: 14px;
    color: #718096;
    text-align: center;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .research-interests {
        grid-template-columns: 1fr;
    }

    .event-list li,
    .news-list li {
        font-size: 14px;
    }
}
```

**Design Principles**:
- Maintain existing color scheme (blues: #2c5282, grays: #718096, #e2e8f0)
- Keep spacing consistent with existing design
- Ensure mobile responsiveness
- No visual "clutter" - clean and minimal
- Use existing font stack

---

## 5. Content Guidelines

### 5.1 Research Interests
- List 5-7 main research areas
- Use proper capitalization
- Be specific (not just "Physics")
- Update when research focus changes

### 5.2 News & Highlights
- Keep 3-5 most recent items
- Archive older items annually
- Include: career moves, publications, awards, major talks
- Use consistent date format

### 5.3 Recent Events
- List workshops/programs attended in last 2 years
- Include link to program website
- Brief descriptive title
- Remove very old events (>2 years)

---

## 6. Implementation Plan

### Phase 1: SEO & Meta Tags (30 minutes)
1. Update meta description
2. Expand keywords
3. Add Open Graph tags
4. Add Schema.org JSON-LD
5. Validate structured data

### Phase 2: Content Restructuring (45 minutes)
1. Create Research Interests section
2. Convert Recent Events to list format
3. Add News & Highlights section
4. Update bio paragraph (remove extracted content)
5. Fix heading hierarchy

### Phase 3: CSS Styling (30 minutes)
1. Add new CSS classes to main.css
2. Test responsive behavior
3. Verify visual consistency
4. Test in multiple browsers

### Phase 4: Accessibility (20 minutes)
1. Add skip link
2. Update navigation with ARIA labels
3. Change `<menu>` to `<nav>`
4. Add id="main-content"
5. Test with screen reader

### Phase 5: Final Touches (10 minutes)
1. Add last updated timestamp
2. Final validation
3. Test all links
4. Review on mobile device

**Total Estimated Time**: 2.5 hours

---

## 7. Testing & Validation

### 7.1 SEO Testing
- [ ] Google Rich Results Test: https://search.google.com/test/rich-results
- [ ] Schema.org Validator: https://validator.schema.org/
- [ ] Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/
- [ ] Twitter Card Validator: https://cards-dev.twitter.com/validator

### 7.2 Accessibility Testing
- [ ] WAVE Web Accessibility Tool: https://wave.webaim.org/
- [ ] Keyboard navigation (Tab through all elements)
- [ ] Screen reader test (macOS VoiceOver or NVDA)
- [ ] Lighthouse accessibility score >90

### 7.3 Browser Testing
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

### 7.4 Responsive Testing
- [ ] Desktop (1920x1080)
- [ ] Laptop (1366x768)
- [ ] Tablet (768x1024)
- [ ] Mobile (375x667)

---

## 8. Success Metrics

### Immediate (Week 1)
- [ ] All HTML validates without errors
- [ ] Lighthouse SEO score >90
- [ ] Lighthouse Accessibility score >90
- [ ] All links functional
- [ ] No visual regressions

### Short-term (Month 1)
- [ ] Google indexes structured data
- [ ] Rich snippets appear in search results
- [ ] Social media shares show proper preview cards

### Long-term (6 months)
- [ ] Increase in organic search traffic
- [ ] Higher ranking for name + research area searches
- [ ] More professional network connections citing website

---

## 9. Maintenance Plan

### Monthly
- Update News & Highlights with recent activities
- Add new events to Recent Events
- Remove events older than 2 years

### Quarterly
- Review and update Research Interests if focus changes
- Update Recent Talks section
- Check all external links (workshops, programs)

### Annually
- Update "Last updated" timestamp
- Archive old news items
- Review SEO keywords
- Check Google Search Console data

---

## 10. File Changes Summary

### Files to Modify
1. **index.html**
   - Add meta tags in `<head>`
   - Add skip link at top of `<body>`
   - Update navigation structure
   - Restructure main content sections
   - Add footer with timestamp

2. **css/main.css**
   - Add `.research-interests` styles
   - Add `.event-list` styles
   - Add `.news-list` styles
   - Add `.skip-link` styles
   - Add `.page-footer` and `.last-updated` styles
   - Add responsive media queries

### Files to Create
None (all changes are modifications)

### Files to Delete
None

---

## 11. Rollback Plan

If issues arise:

1. **Keep backup**: Before starting, copy current index.html to index.html.backup
2. **Git commit**: Commit changes incrementally by phase
3. **Quick rollback**: `git checkout HEAD~1 index.html` to revert to previous version
4. **Full rollback**: `cp index.html.backup index.html`

---

## 12. Future Enhancements (Out of Scope)

Not included in this PRD, but potential future improvements:

- Profile photo section
- CV download link
- Publication highlights on homepage
- Dark mode toggle
- Google Analytics integration
- ORCID integration
- Teaching highlights preview
- Collaboration network visualization

---

## 13. Approval & Sign-off

**Prepared by**: Claude Code
**Reviewed by**: Da-Chuan Lu
**Approved by**: _______________
**Date**: _______________

---

## Appendix A: Content Templates

### A.1 Research Interests (Example)
```
- Deconfined Quantum Criticality
- Symmetric Mass Generation
- Generalized Symmetry & Non-Invertible Symmetry
- Strongly Correlated Electronic States
- Topological Phases & SPT Phases
- Quantum Information Theory
```

### A.2 News Items (Example Format)
```
<strong>Month YYYY</strong> - Achievement description with optional link
```

### A.3 Event Items (Example Format)
```
<strong>Season YYYY</strong> - <a href="URL">Program Name</a>: Brief description
```

---

**Document Version**: 1.0
**Last Updated**: November 2025
**Status**: Ready for Implementation
