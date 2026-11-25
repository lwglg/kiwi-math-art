#import "../lib/notation.typ": *
#let render(t) = [
  = #t.sec_feathers
  #t.feather_intro

  $ delta_r (x) = x + (60 - r)/40. $ <eq:delta>

  #t.feather_warp

  $ T_r (x,y) = y + 4/5 (3 + cos((12 + 5 cos(2 r^2)) y + 5 cos(14 r))) delta_r (x)^3. $ <eq:T>

  #t.feather_phase

  $ U_r (x,y) = & (140 - 30 arctan((3(r-20))/10) - 30 e^(-y^2)) T_r (x,y) \
    & + cos(10 T_r (x,y) + 5 r) + 10 cos(r^2). $ <eq:U>

  #t.feather_reach

  $ lambda_r = 29/88 (1 + sqrt(r/100)) - 3/2 abs((r - 50)/45)^3, $ <eq:reach>

  $ W(x,y) = (x + 1 - 1/(70 abs(y - 2/5) + 4))^2 + 2 abs(y - 1/4)^(3 + x) - 11/100. $ <eq:head-level>

  #t.feather_ridge

  $ theta_r = 2/5 + 2/58 arctan(2/5 (r - 15)), quad
    Phi_r (x,y) = sigma_5 (sin U_r (x,y) - theta_r - 4 delta_r (x)^2). $ <eq:ridge>

  #t.feather_gate

  $ chi_r (x,y) = sigma_200 (abs(T_r (x,y)) - lambda_r) thin sigma_40 (W(x,y)). $ <eq:gate>

  #t.feather_stroke

  $ J_r (x,y) = sigma_1000 (r - 1/2) thin sigma_100 (delta_r (x)) thin Phi_r (x,y) thin (1 - chi_r (x,y)). $ <eq:J>

  #t.feather_cover

  $ Z(x,y) = product_(r=1)^100 (1 - J_r (x,y)). $ <eq:Z>

  #t.feather_paint

  $ L_s (x,y) = sum_(r=1)^100 J_r (x,y) (product_(u=0)^(r-1) (1 - J_u (x,y))) thin C_r (x,y) thin V_r (x,y) thin h_(s,r) thin R_r (x), $ <eq:L>

  #t.feather_factors

  $ C_r (x,y) = 1 + sigma_30 (y - 64/100 + (5 + 100 (x + 29/50)^2)^(-1)), $ <eq:C>

  $ V_r (x,y) = 2/5 + 1/2 sigma_1000 (sin(U_r (x,y)/2)) + 3/5 T_r (x,y), $ <eq:V>

  $ h_(s,r) = 2^(2-s)/10 + (1/5 - (s^2 - s)/60)(1/2 - 1/pi arctan((r - 10)/10)), $ <eq:h>

  $ R_r (x) = 1/10 + 3/10 (1/2 - 1/pi arctan((3(r - 25))/10)) + (7/2 + 7/pi arctan((r - 10)/10)) delta_r (x). $ <eq:R>
]
