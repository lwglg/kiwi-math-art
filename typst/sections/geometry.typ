#import "../lib/notation.typ": *
#let render(t) = [
  = #t.sec_geometry
  #t.geo_intro

  $ a(x) = 36/100 - x^2/10, quad
    Gamma(x,y) = epsilon.alt_1000 (abs(y - a(x)) - 1/2000). $ <eq:axis>

  #t.geo_beak

  $ A(x,y) = epsilon.alt_100 (abs(y - a(x)) - abs(x + 21/10)^(3/10)/20 - 7/50 (x + 21/10)^4) thin
    epsilon.alt_20 (x + 123/100) thin sigma_1000 (x + 21/10). $ <eq:beak>

  #t.geo_legs

  $ q(x,y) = y + 4 abs(x - 1/5 + 1/2 abs(y + 4/5)^(13/10)), $ <eq:q>

  $ B(x,y) = & epsilon.alt_20 (abs(q(x,y)) - 9/10 + 1/200 sin(200 y + 5 x + 5 sin(34 y + 4 x)) - (10 y + 2)/11) \
    & dot epsilon.alt_50 (y + 1/2 - x^2). $ <eq:legs>

  #t.geo_levels

  $ u(x,y) = (x + 1)^2 + 2 abs(y - 1/4)^(3 + x) - 1/10, quad
    v(x,y) = (x + 6/25)^2 + 8/5 abs(y)^(2 + x) - 7/10, $ <eq:uv>

  #t.geo_eye

  $ E(x,y) = sigma_2000 ((x + 1)^2 + 64/1000 abs(y - 1/4) - 1/500). $ <eq:eye>
]
