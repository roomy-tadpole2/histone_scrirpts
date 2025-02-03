import matplotlib.pyplot as plt
import numpy as np
from Bio import AlignIO

def plot(input_file_path, output_file_path: str, name_title=False):
    # Define colors for amino acids based on ESPript-like scheme
    aa_color_scheme = {
        "A": "green", "V": "green", "L": "green", "I": "green",  # Hydrophobic
        "F": "blue", "Y": "blue", "W": "blue",                   # Aromatic
        "D": "red", "E": "red",                                   # Negative (acidic)
        "R": "purple", "K": "purple", "H": "purple",             # Positive (basic)
        "S": "orange", "T": "orange", "N": "orange", "Q": "orange", # Polar uncharged
        "C": "yellow", "M": "yellow",                            # Sulfur-containing
        "G": "gray", "P": "brown",                               # Special cases
        "-": "white"                                             # Gaps
    }
    def color_adjust(color: str):
        if (color=='yellow'): return "black"
        else: return "white"
    # Load aligned sequences
    alignment = AlignIO.read(f"{input_file_path}.fasta", "fasta")

    # Convert sequences to a matrix (rows = sequences, columns = positions)
    seq_data = [list(record.seq) for record in alignment]
    seq_labels = [record.id for record in alignment]
    num_seqs = len(seq_data)
    num_positions = len(seq_data[0])

    fig, ax = plt.subplots(figsize=(num_positions * 0.2, num_seqs * 0.5))

    for i, seq in enumerate(seq_data):
        for j, aa in enumerate(seq):
            color = aa_color_scheme.get(aa, "black")  # Default to black if unknown
            if (aa!='-'):
                ax.text(j, i, aa, fontsize=10, color=color_adjust(color),
                        ha="center", va="center", bbox=
                        dict(facecolor=color, edgecolor='black', boxstyle='round,pad=0.2'))
            else:
                ax.text(j, i, aa, fontsize=20, color="black",
                        ha="center", va="center", bbox=None)

    ax.set_xticks(range(num_positions))
    ax.set_xticklabels(range(1, num_positions + 1), fontsize=8, rotation=90)
    ax.set_yticks(range(num_seqs))
    ax.set_yticklabels(seq_labels, fontsize=14)
    ax.set_xlim(-0.5, num_positions - 0.5)
    ax.set_ylim(num_seqs - 0.5, -0.5)
    ax.grid(False)

    # Remove axes
    ax.set_frame_on(False)
    ax.xaxis.set_tick_params(size=0)
    ax.yaxis.set_tick_params(size=0)

    plt.tight_layout()

    if (name_title):
        plt.title(output_file_path, fontsize=35, fontfamily='serif', color='#8B4513', loc='left', pad=20)  

    plt.savefig(f"{output_file_path}.pdf", dpi=300, bbox_inches="tight")
