// Operators and shorthand used across sections.
#let arctan = math.op("arctan")
#let clip = math.op("clip")
// Smooth switches: sigma_k(t) ~ 1 for t > 0; epsilon_k(t) ~ 1 for t < 0.
#let sw(k, arg) = if k == none { $sigma (#arg)$ } else { $sigma_#k (#arg)$ }
#let co(k, arg) = if k == none { $epsilon.alt (#arg)$ } else { $epsilon.alt_#k (#arg)$ }
