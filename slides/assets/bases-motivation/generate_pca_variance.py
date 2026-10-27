"""Render the variance shares for Deck 07's eight centered observations."""

from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Rows of X; Q = [[1, -1], [1, 1]] / sqrt(2).
data = [(10, 14), (-10, -14), (11, 5), (-11, -5),
        (4, 4), (-4, -4), (-2, 2), (2, -2)]
original_squares = [sum(row[j] ** 2 for row in data) for j in range(2)]
score_squares = [sum(Fraction((a + b) ** 2, 2) for a, b in data),
                 sum(Fraction((b - a) ** 2, 2) for a, b in data)]
shares = [100 * float(values[0] / sum(values)) for values in (original_squares, score_squares)]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 17,
                     "svg.fonttype": "none", "svg.hashsalt": "math332-pca-variance"})
fig, ax = plt.subplots(figsize=(12, 2.5))
positions = [1, 0]
ax.barh(positions, shares, height=0.52, color="#168b90", label="First coordinate")
ax.barh(positions, [100 - share for share in shares], left=shares, height=0.52,
        color="#064b76", label="Second coordinate")
for y, first in zip(positions, shares):
    for left, width in ((0, first), (first, 100 - first)):
        label = f"{width:.1f}%" if y == 0 else f"{width:.0f}%"
        ax.text(left + width / 2, y, label, ha="center", va="center", color="white", fontsize=16)
ax.set_xlim(0, 100)
ax.set_ylim(-0.45, 1.65)
ax.set_yticks(positions, ["Original", "PCA"])
ax.set_xticks([])
ax.tick_params(axis="y", length=0, pad=12, colors="#064b76")
for spine in ax.spines.values():
    spine.set_visible(False)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.24), ncol=2, frameon=False,
          handlelength=1.2, columnspacing=2)
ax.set_facecolor("none")
fig.subplots_adjust(left=0.14, right=0.995, top=0.76, bottom=0.03)
output = Path(__file__).with_name("pca-variance-share.svg")
fig.savefig(output, bbox_inches="tight",
            pad_inches=0.04, transparent=True, metadata={"Date": None})
plt.close(fig)
output.write_text("\n".join(line.rstrip() for line in output.read_text().splitlines()) + "\n")
