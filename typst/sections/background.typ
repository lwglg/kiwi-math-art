#import "../lib/notation.typ": *
#let render(t) = [
  = #t.sec_background
  #t.bg_intro

  $ P_r (x,y) = sin^10 (sin(2 r) + (3 + sin(r^2)) (x/2 sin(7 r) + (y - 8)/2 cos(7 r))), $ <eq:P>

  $ Q_r (x,y) = sin^10 (sin(3 r) + (3 + 2 sin(r^2)) ((y - 8)/2 sin(7 r) - x/2 cos(7 r))). $ <eq:Q>

  #t.bg_sum

  $ K_s (x,y) = sum_(r=1)^40 w_(s,r) thin sigma_15 (P_r (x,y) Q_r (x,y) - 1/10), $ <eq:K>

  $ w_(s,r) = 9/(54 - 30(s - 1) + 32(s^2 - s)) (3/5 + sin(2 r + 4 s)/5 + sin((2 + 5 s) r)/5). $ <eq:w>
]
