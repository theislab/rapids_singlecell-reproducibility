import scanpy as sc

# plt.rcParams["font.family"] = "sans-serif"
# plt.rcParams["font.sans-serif"] = ["Arial", "Helvetica"]

rsc_lightgreen = "#a7c957"
rsc_darkgreen = "#386641"
rsc_blue = "#3f88c5"
rsc_grey = "#959595"
rsc_turquise = "#2EC4B6"


def figure_journal_basic():
    sc.set_figure_params(
        dpi=300,
        dpi_save=300,
        figsize=(4, 4),
        frameon=False,
        facecolor=None,
        transparent=True,
        vector_friendly=True,
    )


def figure_jupyter():
    sc.set_figure_params(
        dpi=80,
        dpi_save=150,
        figsize=(8, 8),
        frameon=False,
        facecolor="white",
        transparent=False,
        vector_friendly=True,
    )
