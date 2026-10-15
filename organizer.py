"""
SA Business Closure Organizer
Handles CIPC, UIF, SARS docs for companies that never traded.
Built in Zamdela, Free State for real SARS deregistration case.
Author: leratoblessingm-netizen
Version: 1.0.0
"""

import os
import re
import shutil
from datetime import datetime
import csv

DOC_TYPES = {
    "CIPC": ["cipc", "cor40", "deregistration", "bizportal", "cor"],
    "UIF": ["ui19", "uif", "labour", "metsimaholo"],
    "SARS": ["sars", "tax", "tcs", "compliance", "it14", "efiling"],
    "BANK": ["bank", "statement", "fnb", "absa", "capitec"],
    "ID": ["id", "passport", "director"],
    "AFFIDAVIT": ["affidavit", "saps"]
}

def detect_type(filename):
    name = filename.lower()
    for doc_type, keywords in DOC_TYPES.items():
        for kw in keywords:
            if kw in name:
                return doc_type
    return "OTHER"

def clean_name(filename, doc_type):
    base = os.path.splitext(filename)[0]
    base = re.sub(r'wa_image_\d+|image_\d+', '', base, flags=re.I)
    base = re.sub(r'[^a-zA-Z0-9]+', '-', base).strip('-')
    date = datetime.now().strftime("%Y-%m-%d")
    return f"{date}-{doc_type}-{base}.pdf" if base else f"{date}-{doc_type}.pdf"

def organize_folder(input_folder="my_documents", output_folder="organized"):
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Created {input_folder} - put PDFs inside and run again")
        return

    os.makedirs(output_folder, exist_ok=True)
    inventory = []

    for fname in os.listdir(input_folder):
        if not fname.lower().endswith(('.pdf', '.jpg', '.png', '.jpeg')):
            continue
        fpath = os.path.join(input_folder, fname)
        doc_type = detect_type(fname)
        new_name = clean_name(fname, doc_type)
        dest = os.path.join(output_folder, new_name)
        shutil.copy2(fpath, dest)
        inventory.append([fname, doc_type, new_name])
        print(f"[OK] {fname} -> {new_name}")

    # checklist
    with open(os.path.join(output_folder, "checklist.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Original", "Type", "New Name"])
        w.writerows(inventory)

    print(f"\nDone! Organized {len(inventory)} files")

if __name__ == "__main__":
    organize_folder()
