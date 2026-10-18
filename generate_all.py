import os, argparse
from datetime import date
def load_template(name):
    with open(f"templates/{name}.txt","r",encoding="utf-8") as f:
        return f.read()
def generate(company, reg_no):
    today = date.today().strftime("%d %B %Y")
    out_dir = f"output/{reg_no.replace('/','-')}"
    os.makedirs(out_dir, exist_ok=True)
    data = {"{{COMPANY_NAME}}":company,"{{REG_NO}}":reg_no,"{{DATE}}":today}
    for tmpl in ["cipc_letter","sars_letter","uif_letter"]:
        content = load_template(tmpl)
        for k,v in data.items():
            content = content.replace(k,v)
        with open(f"{out_dir}/{tmpl}.txt","w",encoding="utf-8") as f:
            f.write(content)
    print("Done! in", out_dir)
if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--company",required=True)
    p.add_argument("--reg",required=True)
    a=p.parse_args()
    generate(a.company,a.reg)
