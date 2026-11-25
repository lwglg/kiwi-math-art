// Page, typography and heading styles shared by every language.
#let apply(t, body) = {
  set document(title: t.title, author: ("Hamid Naderi Yeganeh", "Guilherme Lima Gonçalves"))
  // Optional per-language overrides (the Persian PDF needs an Arabic-script font).
  let font = t.at("font", default: ("New Computer Modern", "Libertinus Serif"))
  set text(font: font, size: t.at("size", default: 10.5pt), lang: t.lang, region: t.region)
  show math.equation: set text(font: "New Computer Modern Math")
  set page(paper: "a4", margin: (x: 2.3cm, y: 2.5cm), numbering: "1", footer: context {
    set text(size: 8pt, fill: luma(90))
    grid(columns: (1fr, auto),
      [#t.footer_credit],
      // Numbers stay left-to-right even in right-to-left documents ("page / total").
      box(text(dir: ltr, counter(page).display("1 / 1", both: true))))
  })
  set par(justify: true, leading: t.at("leading", default: 0.65em))
  set heading(numbering: "1.1")
  show heading.where(level: 1): it => block(above: 1.6em, below: 0.9em, text(size: 14pt, weight: "bold", it))
  show heading.where(level: 2): it => block(above: 1.2em, below: 0.6em, text(size: 11.5pt, weight: "bold", it))
  set math.equation(numbering: "(1)", supplement: t.eq_supplement)
  set footnote(numbering: "(1)")
  show link: set text(fill: rgb("#1a56a0"))
  body
}

// A framed note box (used for fidelity warnings).
#let note(title, body) = block(
  width: 100%, inset: 10pt, radius: 3pt, stroke: 0.6pt + rgb("#b36b00"), fill: rgb("#fff6e5"),
  [*#title* \ #body],
)
