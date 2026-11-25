#import "../lib/notation.typ": *
#let render(t) = [
  = #t.sec_switches
  #t.switch_intro

  $ sigma_k (u) = e^(-e^(-k u)), quad epsilon.alt_k (u) = e^(-e^(k u)) = sigma_k (-u). $ <eq:switches>

  #t.switch_use

  $ F(x) = floor(255 thin sigma_1000 (x) abs(x)^(epsilon.alt_1000 (x - 1))). $ <eq:transfer2>

  #t.switch_union
]
