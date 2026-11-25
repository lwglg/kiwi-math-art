// Entry point. Usage: typst compile --root . --input lang=en|de|pt|ru|fa typst/main.typ out.pdf
#import "lib/theme.typ": apply
#import "lib/authors.typ": title-block
#import "sections/canvas.typ"
#import "sections/switches.typ"
#import "sections/feathers.typ"
#import "sections/geometry.typ"
#import "sections/background.typ"
#import "sections/assembly.typ"
#import "sections/fidelity.typ"

#let lang = sys.inputs.at("lang", default: "en")
#let t = if lang == "pt" {
  import "lang/pt.typ": t
  t
} else if lang == "fa" {
  import "lang/fa.typ": t
  t
} else if lang == "ru" {
  import "lang/ru.typ": t
  t
} else if lang == "de" {
  import "lang/de.typ": t
  t
} else {
  import "lang/en.typ": t
  t
}

#show: apply.with(t)

#title-block(t, image-path: "/build/kiwi.png")

#v(1em)
#align(center, block(width: 88%)[
  #text(weight: "bold", t.abstract_title) \
  #set text(size: 9.5pt)
  #t.abstract
])

#canvas.render(t)
#switches.render(t)
#feathers.render(t)
#geometry.render(t)
#background.render(t)
#assembly.render(t)
#fidelity.render(t)
