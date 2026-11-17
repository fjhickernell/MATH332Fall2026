"""Draw one ODE trajectory in the original and eigenvector coordinates.

Run with the course's qmcpy Python environment.  The generated SVG is a
course asset, rather than notebook output.  Its equal-time dots correspond
under x = V c; field arrows show direction only, not speed.
"""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


NAVY = "#064b76"
ORANGE = "#c46716"
TEAL = "#128279"
PALE = "#becbd1"

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--preview", type=Path, help="Optional PNG preview destination")
args = parser.parse_args()

A = np.array([[2.0, 1.0], [1.0, 2.0]])
V = np.array([[1.0, 1.0], [1.0, -1.0]])
D = np.diag([3.0, 1.0])
assert np.allclose(A @ V, V @ D)


def coordinates(t):
    """Columns are the eigenbasis coordinates at the supplied times."""
    return np.array([3 * np.exp(3 * t), np.exp(t)])


def arrow_on_curve(ax, curve, t0=0.34, t1=0.385):
    start, end = curve(np.array([t0, t1])).T
    ax.annotate(
        "", xy=end, xytext=start,
        arrowprops={"arrowstyle": "-|>", "color": NAVY, "lw": 2.8,
                    "mutation_scale": 22, "shrinkA": 0, "shrinkB": 0},
        zorder=6,
    )


plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 17,
    "mathtext.fontset": "dejavuserif",
    "svg.fonttype": "none",
    "svg.hashsalt": "math332-eigenbasis-flow",
})
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
fig.subplots_adjust(left=0.035, right=0.985, top=0.82, bottom=0.09, wspace=0.23)

times = np.linspace(0, 0.45, 200)
marks = np.array([0.0, 0.15, 0.30, 0.45])
panels = [
    {
        "coordinates": "original",
        "matrix": A,
        "curve": lambda t: V @ coordinates(t),
        "limits": ((-2, 15), (-5, 12)),
        "title": "Original coordinates",
        "start_label": r"$\mathbf{x}(0)=(4,2)$",
        "start_offset": (15, -28),
    },
    {
        "coordinates": "eigenbasis",
        "matrix": D,
        "curve": coordinates,
        "limits": ((-2, 13), (-5, 10)),
        "title": "Eigenbasis coordinates",
        "start_label": r"$\mathbf{c}(0)=(3,1)$",
        "start_offset": (1, 26),
    },
]

for ax, panel in zip(axes, panels):
    matrix, curve = panel["matrix"], panel["curve"]
    xlim, ylim = panel["limits"]
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks([0, 5, 10])
    ax.set_yticks([-5, 0, 5, 10])
    ax.tick_params(length=0, labelsize=13, colors="#60717b", pad=5)
    ax.grid(color="#e9eef0", linewidth=0.65, zorder=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.axhline(0, color="#748994", lw=1.0, zorder=1)
    ax.axvline(0, color="#748994", lw=1.0, zorder=1)
    ax.set_axisbelow(True)

    # Direction-only arrows avoid the enormous speed variation of this field.
    gx, gy = np.meshgrid(np.linspace(xlim[0] + 0.65, xlim[1] - 0.65, 10),
                         np.linspace(ylim[0] + 0.65, ylim[1] - 0.65, 10))
    velocity = matrix @ np.array([gx.ravel(), gy.ravel()])
    norms = np.linalg.norm(velocity, axis=0)
    velocity /= np.maximum(norms, 1e-12)
    ax.quiver(gx, gy, velocity[0].reshape(gx.shape), velocity[1].reshape(gy.shape),
              color=PALE, alpha=0.63, angles="xy", scale_units="xy", scale=1.3,
              width=0.0035, headwidth=4.5, headlength=5.5, zorder=1)

    line = np.linspace(-18, 18, 200)
    if panel["coordinates"] == "eigenbasis":
        ax.plot(line, np.zeros_like(line), color=ORANGE, lw=2.3, alpha=0.8, zorder=2)
        ax.plot(np.zeros_like(line), line, color=TEAL, lw=2.3, alpha=0.8, zorder=2)
        ax.text(11.7, -1.0, r"$c_1$", color=ORANGE, ha="center", fontsize=20)
        ax.text(-1.0, 8.8, r"$c_2$", color=TEAL, ha="center", fontsize=20)
    else:
        ax.plot(line, line, color=ORANGE, lw=2.3, alpha=0.8, zorder=2)
        ax.plot(line, -line, color=TEAL, lw=2.3, alpha=0.8, zorder=2)
        ax.text(7.8, 10.3, r"$\mathrm{span}\{\mathbf{v}_1\}$", color=ORANGE,
                fontsize=17, ha="center")
        ax.text(5.0, -4.15, r"$\mathrm{span}\{\mathbf{v}_2\}$", color=TEAL,
                fontsize=17, ha="left", bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
        ax.text(13.6, -1.1, r"$x_1$", color=NAVY, ha="center", fontsize=20)
        ax.text(-1.0, 10.8, r"$x_2$", color=NAVY, ha="center", fontsize=20)

    values = curve(times)
    ax.plot(*values, color=NAVY, lw=3.2, zorder=5)
    points = curve(marks)
    ax.scatter(*points, s=63, facecolor="white", edgecolor=NAVY, linewidth=2.0, zorder=7)
    ax.scatter(*points[:, 0], s=75, facecolor=NAVY, edgecolor="white", linewidth=0.9, zorder=8)
    arrow_on_curve(ax, curve)

    ax.annotate(panel["start_label"], xy=points[:, 0], xytext=panel["start_offset"],
                textcoords="offset points",
                fontsize=17, color=NAVY,
                ha="left", va="center",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    # End time locates the traversal; intervening open circles are equally spaced in time.
    ax.annotate(r"$t=0.45$", xy=points[:, -1], xytext=(-2, 20), textcoords="offset points",
                fontsize=15, color=NAVY, ha="center", va="bottom")
    ax.set_title(panel["title"], color=NAVY,
                 fontsize=20, pad=25)

# Matrices and their change-of-basis identity are exact; derivatives of the
# displayed analytic curve satisfy both systems at every time.
sample_c = coordinates(marks)
sample_cprime = np.array([9 * np.exp(3 * marks), np.exp(marks)])
assert np.allclose(sample_cprime, D @ sample_c)
assert np.allclose(V @ sample_cprime, A @ V @ sample_c)
assert np.allclose(V @ coordinates(0), [4, 2])

output = Path(__file__).with_name("eigenbasis-flow.svg")
fig.savefig(output, transparent=True, metadata={"Date": None})
if args.preview:
    fig.savefig(args.preview, dpi=150, transparent=False)
plt.close(fig)
output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
