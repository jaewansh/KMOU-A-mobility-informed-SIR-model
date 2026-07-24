import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"

REPLACEMENTS = {
    "/Users/sinjaewan/Desktop/연구/인플루엔자/seoul&g_metro.csv": "data/metro/seoul&g_metro.csv",
    "/Users/sinjaewan/Desktop/연구/인플루엔자/busan_metro.csv": "data/metro/busan_metro.csv",
    "/Users/sinjaewan/Desktop/연구/인플루엔자/daejeon_metro.csv": "data/metro/daejeon_metro.csv",
    "/Users/sinjaewan/Desktop/연구/인플루엔자/daegu_metro.csv": "data/metro/daegu_metro.csv",
    "/Users/sinjaewan/Desktop/연구/인플루엔자/gwangju_metro.csv": "data/metro/gwangju_metro.csv",

    "/Users/sinjaewan/Desktop/MBE/data/NHIS/": "data/NHIS/",
    "/Users/sinjaewan/Desktop/MBE/data/mobility_factor/": "data/mobility_factor/",
    "/Users/sinjaewan/Desktop/MBE/data/Rt": "data/Rt",
    "/Users/sinjaewan/Desktop/MBE/figure/mobility factor/": "figures/mobility_factor/",
    "/Users/sinjaewan/Desktop/MBE/figure/2016~2017/": "figures/2016~2017/",
    "/Users/sinjaewan/Desktop/MBE/figure/HeatMap/": "figures/HeatMap/",

    "/Users/sinjaewan/Desktop/연구/인플루엔자/csv/daily_rmse_results.csv": "results/validation/daily_rmse_results.csv",

    "df_results.to_csv('daily_rmse_results.csv', index=False)": "df_results.to_csv('results/validation/daily_rmse_results.csv', index=False)",
    "plt.savefig('SIR Mathematical Model Negative binomial distribution.eps', format='eps', bbox_inches='tight')": "plt.savefig('figures/validation/SIR Mathematical Model Negative binomial distribution.eps', format='eps', bbox_inches='tight')",
    "plt.savefig('SIR Mathematical Model Negative binomial distribution RMSE.eps', format='eps', bbox_inches='tight')": "plt.savefig('figures/validation/SIR Mathematical Model Negative binomial distribution RMSE.eps', format='eps', bbox_inches='tight')",
    "pd.read_csv(\"/Users/sinjaewan/Desktop/연구/인플루엔자/csv/daily_rmse_results.csv\")": "pd.read_csv(\"results/validation/daily_rmse_results.csv\")",

    "OUTPUT_DIR = Path(\"./rt_metric_outputs\")": "OUTPUT_DIR = Path(\"results/tables/rt_metric_outputs\")",
}

REQUIRED_DIRECTORIES = [
    ROOT / "data" / "metro",
    ROOT / "data" / "NHIS" / "2016~2017",
    ROOT / "data" / "mobility_factor" / "2016~2017",
    ROOT / "data" / "Rt" / "2016~2017",
    ROOT / "data" / "Rt" / "2017~2018",
    ROOT / "data" / "Rt" / "2018~2019",
    ROOT / "data" / "Rt" / "2022~2023",
    ROOT / "figures" / "mobility_factor",
    ROOT / "figures" / "2016~2017",
    ROOT / "figures" / "HeatMap",
    ROOT / "figures" / "validation",
    ROOT / "results" / "validation",
    ROOT / "results" / "tables",
]


def patch_notebook(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    for old, new in sorted(REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(old, new)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True

    return False


def validate_notebook_json(path: Path) -> None:
    with path.open("r", encoding="utf-8") as f:
        json.load(f)


def main() -> None:
    for directory in REQUIRED_DIRECTORIES:
        directory.mkdir(parents=True, exist_ok=True)

    if not NOTEBOOK_DIR.exists():
        raise FileNotFoundError(f"Notebook directory not found: {NOTEBOOK_DIR}")

    notebooks = sorted(NOTEBOOK_DIR.glob("*.ipynb"))
    if not notebooks:
        raise FileNotFoundError(f"No notebooks found in: {NOTEBOOK_DIR}")

    patched = []
    for notebook in notebooks:
        changed = patch_notebook(notebook)
        validate_notebook_json(notebook)
        if changed:
            patched.append(notebook.relative_to(ROOT))

    if patched:
        print("Patched notebook paths:")
        for path in patched:
            print(f"- {path}")
    else:
        print("No notebook path replacements were needed.")

    print("Notebook path patching completed.")


if __name__ == "__main__":
    main()
