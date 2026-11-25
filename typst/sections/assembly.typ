#import "../lib/notation.typ": *
#let render(t) = [
  = #t.sec_assembly
  #t.asm_intro

  $ G_s (x,y) = (16 - 2 s^2 + s)/20 + 4 y - 36/25 + (2 x^2)/5. $ <eq:G>

  #t.asm_final

  $ H_s (x,y) = & (G_s (x,y) - Gamma(x,y)) thin A(x,y) thin Z(x,y) \
    & + Z(x,y) B(x,y)/10 (3/2 - (4 s^2 + 5 s)/30) (1 + 8 (sigma_50 (x - 3/20) - 1/2) q(x,y)) \
    & + ((2 - s)/10 + (x/5 + 53/50) K_s (x,y) thin sigma_40 (u(x,y)) thin sigma_17 (v(x,y))) (1 - A(x,y) - B(x,y)) thin Z(x,y) \
    & + L_s (x,y) thin E(x,y). $ <eq:H>

  #t.asm_chain

  $ (m, n) arrow.r.bar (x, y) arrow.r.bar (delta_r, T_r, U_r, J_r) arrow.r.bar (Z, L_s) arrow.r.bar (A, B, E, u, v, K_s) arrow.r.bar H_s arrow.r.bar F arrow.r.bar "rgb". $ <eq:chain>
]
