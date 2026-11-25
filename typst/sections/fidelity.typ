#import "../lib/theme.typ": note
#let render(t) = [
  = #t.sec_fidelity
  #note(t.fidelity_title, t.fidelity_body)
  #table(columns: (auto, 1fr), stroke: 0.4pt + luma(160), inset: 6pt,
    [*#t.fid_col_part*], [*#t.fid_col_status*],
    ..t.fidelity_table.flatten())
]
