// Authorship block: original author and author of this augmented project.
#let original = (
  name: "Hamid Naderi Yeganeh",
  links: (
    (label: "LinkedIn", url: "https://www.linkedin.com/in/hamidnaderiyeganeh"),
    (label: "X", url: "https://x.com/naderi_yeganeh"),
    (label: "YouTube", url: "https://www.youtube.com/@naderiyeganeh"),
  ),
)

// `personal_page` is translated, so the augmented links are built from the dictionary.
#let augmented(t) = (
  name: "Guilherme Lima Gonçalves",
  links: (
    (label: "LinkedIn", url: "https://linkedin.com/in/guligon90"),
    (label: "GitHub", url: "https://github.com/lwglg"),
    (label: t.personal_page_label, url: "https://lwglg.github.io/portfolio-spa"),
  ),
)

#let link-list(links) = links.map(l => link(l.url)[#l.label]).join([ · ])

#let wikipedia = "https://en.wikipedia.org/wiki/Hamid_Naderi_Yeganeh"

// `name` overrides the plain name (used to attach the PhD and its footnote).
#let person(label, who, name: none, note: none) = align(center)[
  #text(size: 8.5pt, weight: "bold", upper(label)) \
  #text(size: 12.5pt, if name == none { who.name } else { name }) \
  #if note != none { text(size: 9pt, fill: luma(90), note); linebreak() }
  #text(size: 9pt, link-list(who.links))
]

#let title-block(t, image-path: none) = {
  align(center)[
    #v(0.6cm)
    #text(size: 22pt, weight: "bold", t.title) \
    #v(0.3em)
    #text(size: 12pt, style: "italic", t.subtitle)
    #v(1.2em)
  ]
  grid(columns: (1fr, 1fr), gutter: 1.2em,
    person(
      t.original_label,
      original,
      name: [#original.name, PhD#footnote(t.original_footnote)],
      note: t.original_note,
    ),
    person(t.augmented_label, augmented(t), note: t.augmented_note))
  if image-path != none {
    v(0.8em)
    align(center, figure(image(image-path, width: 100%), caption: t.figure_caption))
  }
}
