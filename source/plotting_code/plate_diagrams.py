"""
This file draws the probabilistic graphical model plate diagrams from Figure 1
Just run python plate_diagrams.py
"""

import daft
import matplotlib
matplotlib.rc("font", family="serif", size=12)
matplotlib.rc("text", usetex=True)

def create_plate(x, y, width, height, label, label_offset=None, bbox=None, **kwargs):
    if label_offset is None:
        label_offset = [4, 4]
    if bbox is None:
        bbox = {'fc': 'None', 'ec': 'None'}

    plate = daft.Plate([x, y, width, height], label, label_offset=label_offset, bbox=bbox, **kwargs)
    return plate


## (A) GENERATIVE MODEL
pgm = daft.PGM([2.7, 4.1], origin=[0.3, 0.0])

pgm.add_node(daft.Node("kappa", r"$\kappa$", 2.1, 3.8, fixed=True))
pgm.add_node(daft.Node("alpha", r"$\alpha$", 1., 2.9, fixed=True))
pgm.add_node(daft.Node("signatures", r"$s_n$", 1., 2.))
pgm.add_node(daft.Node("exposures", r"$e_{g}$", 2.1, 2.9))
pgm.add_node(daft.Node("assignment", r"$\theta_{g, i}$", 2.1, 2.))
pgm.add_node(daft.Node("data", r"$m_{g, i}$", 2.1, 1.1, observed=True))

pgm.add_edge("kappa", "exposures")
pgm.add_edge("alpha", "signatures")
pgm.add_edge("exposures", "assignment")
pgm.add_edge("assignment", "data")
pgm.add_edge("signatures", "data")

pgm.add_plate(create_plate(x=0.55, y=1.2, width=0.9, height=1.3, label=r"$n \in 1:N$", position="bottom right", label_offset = [3, 4]))
pgm.add_plate(create_plate(x=1.55, y=0.25, width=1.1, height=3.15, label=r"$g \in 1:G$", position="bottom right", label_offset = [4, 5]))
pgm.add_plate(create_plate(x=1.625, y=0.55, width=0.95, height=1.95, label=r"$i \in 1:I$", position="bottom right"))


pgm.render()
pgm.figure.savefig("generative_model.pdf", transparent=True)


## (B) NMF INFERENTIAL MODEL
pgm = daft.PGM([2.7, 4.1], origin=[0.3, 0.0])

pgm.add_node(daft.Node("kappa", r"$\kappa$", 2.1, 3.8, fixed=True))
pgm.add_node(daft.Node("alpha", r"$\alpha$", 1., 2.9, fixed=True))
pgm.add_node(daft.Node("signatures", r"$s_n$", 1., 2.))
pgm.add_node(daft.Node("exposures", r"$e_g$", 2.1, 2.9))
pgm.add_node(daft.Node("probs", r"$p_{g}$", 2.1, 2., plot_params={'ec': "#bbbbbb", 'lw': 3}))
pgm.add_node(daft.Node("data", r"$m_{g}$", 2.1, 1.1, observed=True))

pgm.add_edge("kappa", "exposures")
pgm.add_edge("alpha", "signatures")
pgm.add_edge("exposures", "probs")
pgm.add_edge("probs", "data")
pgm.add_edge("signatures", "probs")

pgm.add_plate(create_plate(x=0.55, y=1.2, width=0.9, height=1.3, label=r"$n \in 1:N$", position="bottom right", label_offset = [3, 4]))
pgm.add_plate(create_plate(x=1.55, y=0.45, width=1.1, height=2.95, label=r"$g \in 1:G$", position="bottom right", label_offset = [4, 5]))


pgm.render()
pgm.figure.savefig("nmf_inferential.pdf", transparent=True)


## (C) EMu INFERENTIAL MODEL
pgm = daft.PGM([3.3, 4.1], origin=[0.3, 0.0])

pgm.add_node(daft.Node("mu", r"$\mu$", 1.7, 3.8, fixed=True))
pgm.add_node(daft.Node("gamma", r"$\gamma$", 2.5, 3.8, fixed=True))
pgm.add_node(daft.Node("alpha", r"$\alpha$", 1., 2.9, fixed=True))
pgm.add_node(daft.Node("opportunities", r"$o_{g, k}$", 2.85, 2., fixed=True))
pgm.add_node(daft.Node("signatures", r"$s_n$", 1., 2.))
pgm.add_node(daft.Node("activities", r"$a_{g}$", 2.1, 2.9))
pgm.add_node(daft.Node("probs", r"$p_{g, k}$", 2.1, 2., plot_params={'ec': "#bbbbbb", 'lw': 3}))
pgm.add_node(daft.Node("data", r"$m_{g, k}$", 2.1, 1.1, observed=True))

pgm.add_edge("mu", "activities")
pgm.add_edge("gamma", "activities")
pgm.add_edge("alpha", "signatures")
pgm.add_edge("activities", "probs")
pgm.add_edge("probs", "data")
pgm.add_edge("signatures", "probs")
pgm.add_edge("opportunities", "probs")

pgm.add_plate(create_plate(x=0.55, y=1.2, width=0.9, height=1.3, label=r"$n \in 1:N$", position="bottom right", label_offset = [3, 4]))
pgm.add_plate(create_plate(x=1.55, y=0.25, width=1.7, height=3.15, label=r"$g \in 1:G$", position="bottom right", label_offset = [4, 5]))
pgm.add_plate(create_plate(x=1.625, y=0.55, width=1.55, height=1.95, label=r"$k \in 1:K$", position="bottom right"))


pgm.render()
pgm.figure.savefig("emu_inferential.pdf", transparent=True)
