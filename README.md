
# 📄 README: GBK to ASN.1 Converter

This script converts a GenBank (`.gbk`) file into an ASN.1 (`.asn`) file using [NCBI's `tbl2asn`](https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2/), via intermediate FASTA (`.fsa`) and feature table (`.tbl`) files.

---

### 🧰 Requirements

- Python 3.6+
- [Biopython](https://biopython.org/)
- [`tbl2asn`](https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2/) (must be in your system PATH)

Install Biopython:
```bash
pip install biopython
```

---

### 🚀 Usage

```bash
python gbk_to_asn_cli.py
```

You’ll be prompted to:

1. Paste the **full path** to your `.gbk` file.
2. Optionally paste the path to a `template.sbt` submission template file.

---

### 📦 Output

In the same directory as your `.gbk` file, the script will generate:

- `.fsa` — FASTA file
- `.tbl` — Feature table
- `.asn` — ASN.1 file
- `.sqn` — Sequin submission file
- `discrep.log` — Discrepancy report from `tbl2asn`

---

### 📝 Example

```text
Paste the full path to your .gbk file: /home/user/genomes/my_genome.gbk
Paste path to template.sbt (or press Enter to skip): /home/user/templates/template.sbt
```

---

### 📌 Notes

- If you don’t have a `template.sbt`, the script can still run for internal use.
- `tbl2asn` is maintained by NCBI — be sure to use the latest version available.
