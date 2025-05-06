import os
import subprocess
from Bio import SeqIO
from pathlib import Path

def convert_gbk_to_fsa_tbl(gbk_path):
    base = gbk_path.stem
    record = SeqIO.read(gbk_path, "genbank")

    # Create .fsa
    fsa_path = gbk_path.with_suffix(".fsa")
    with open(fsa_path, "w") as fasta_out:
        SeqIO.write(record, fasta_out, "fasta")

    # Create .tbl
    tbl_path = gbk_path.with_suffix(".tbl")
    with open(tbl_path, "w") as tbl_out:
        tbl_out.write(f">Feature {record.id}\n")
        for feature in record.features:
            if feature.type == "source":
                continue
            start = int(feature.location.start) + 1  # 1-based
            end = int(feature.location.end)
            tbl_out.write(f"{start}\t{end}\t{feature.type}\n")
            for key, val_list in feature.qualifiers.items():
                for val in val_list:
                    tbl_out.write(f"\t\t\t{key}\t{val}\n")
    return fsa_path, tbl_path

def run_tbl2asn(directory, template_sbt=None):
    cmd = ["tbl2asn", "-p", str(directory), "-a", "s", "-V", "b", "-Z", "discrep.log"]
    if template_sbt and Path(template_sbt).exists():
        cmd += ["-t", str(template_sbt)]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print("[✔] tbl2asn completed successfully")
    else:
        print("[!] tbl2asn failed:")
        print(result.stderr)

def main():
    gbk_path_str = input("Paste the full path to your .gbk file: ").strip()
    gbk_path = Path(gbk_path_str)

    if not gbk_path.exists() or not gbk_path.suffix in [".gbk", ".gb"]:
        print("[!] Invalid .gbk file path.")
        return

    convert_gbk_to_fsa_tbl(gbk_path)

    template_sbt = input("Paste path to template.sbt (or press Enter to skip): ").strip()
    template_sbt = template_sbt if template_sbt else None

    run_tbl2asn(gbk_path.parent, template_sbt)

if __name__ == "__main__":
    main()
