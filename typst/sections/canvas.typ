#import "../lib/notation.typ": *
#let render(t) = [
  = #t.sec_canvas
  #t.canvas_intro

  $ x = (m - 1300)/540, quad y = (531 - n)/540, quad m = 1, ..., 2000, quad n = 1, ..., 1060. $ <eq:plane>

  #t.canvas_color

  $ "rgb"(F(H_0 (x,y)), F(H_1 (x,y)), F(H_2 (x,y))), $ <eq:rgb>

  #t.canvas_transfer

  $ F(x) = floor(255 thin e^(-e^(-1000 x)) abs(x)^(e^(-e^(1000(x-1))))). $ <eq:transfer>
]
