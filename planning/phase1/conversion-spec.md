# ADS-Tutor Phase 1 Conversion Specification

## Scope and provenance

Convert only `main.ptx-main > #ptx-content`. Every output begins with YAML
frontmatter containing `source_relative_path`, `source_sha256`, `scope_class`,
and `displayed_section_or_chapter`. Known missing assets add
`content_gap: true` and an exact `missing_assets` list.

## Canonical constructs

- A chapter/section heading becomes the corresponding Markdown heading, with
  the displayed number and title retained verbatim.
- Typed blocks use this locked template:
  `> **Definition 1.2.1 — Intersection.**`
  followed by each body paragraph as a consecutive blockquote paragraph.
  Examples, exercises, and theorem-like blocks use the same form with their
  source type and number. Exercise subparts retain their lower-alpha labels.
- Inline math is preserved verbatim inside `\( ... \)`; display math is
  preserved verbatim inside `\[ ... \]`. No LaTeX normalization is allowed.
- `.process-math` and `script[type^="math/tex"]` are both converted to those
  delimiters; script contents are copied verbatim.
- `pre.sagecell-sage` becomes a fenced `sage` block with source unchanged.
- Figures become `![alt](source-path)`. Known missing assets become
  `![MISSING FIGURE: description](GAP:original-path)` and are listed in
  frontmatter.
- Internal links resolve through the Phase 0 source-to-output mapping when a
  target exists; unresolved targets remain as links with an
  `UNRESOLVED_INTERNAL_LINK` marker.
- Tables are emitted as Markdown tables when rectangular; otherwise they are
  retained in an `UNHANDLED_SOURCE` fence.
- Any unsupported construct is visibly retained in an
  `UNHANDLED_SOURCE` fenced block; nothing is silently discarded.

## Boilerplate removal

Discard navigation/sidebar/search elements, header/footer regions, CSS/JS
links, MathJax runtime configuration, and scripts that reference the 760
known chrome assets. Content is selected only below `#ptx-content`.

## Fixture gates

The 1.2 fixture must preserve its six definitions/examples/exercises/Sage
counts, all seven known missing assets, source provenance, and every LaTeX
string represented in the selected blocks.
