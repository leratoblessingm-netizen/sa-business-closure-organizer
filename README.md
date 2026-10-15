# SA Business Closure Organizer

Built after closing a real company in Zamdela that never traded — dealing with CIPC, UIF (Metsimaholo), and SARS deregistration with files named wa_image_8255...jpg

## The Problem
When SARS asks for proof 2 years after you closed, you need:
- CIPC CoR40.005 certificate
- ID copy of director
- Bank statements showing zero trading
- UIF UI19 termination
- Affidavit from SAPS

Most people lose them in WhatsApp folders.

## Solution
Python tool that:
- Scans `my_documents/` folder
- Auto-detects CIPC / UIF / SARS / BANK / ID from filename
- Renames to `2026-10-15-CIPC-Deregistration.pdf`
- Copies to clean `organized/` folder
- Creates `checklist.csv` showing what's MISSING for SARS

## How to Use (No data needed)
```bash
# 1. Put all PDFs/JPGs in my_documents/
# 2. Run
python organizer.py
# 3. Check organized/ folder
