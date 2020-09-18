import yaml
import os

path_to_merge = "//home//users//pdepretz"
files_to_merge = {file:yaml.load((open(path_to_merge + file, "r").read()).lower(), Loader=yaml.FullLoader) for file in os.listdir(path_to_merge) if file.find(".yaml") and "psql_ingenico::pg_hba_rule" in open((path_to_merge + file)).read()}

proper_new_file = {"psql_ingenico::pg_hba_rule":{}}
reject_rules = []

for key_file, value_file in files_to_merge.items():
    for key, value in value_file["psql_ingenico::pg_hba_rule"].items():
        if sum([ True for i in files_to_merge if str(key) in files_to_merge[i]["psql_ingenico::pg_hba_rule"] ]) > 1:
            for file in files_to_merge.values():
                if file["psql_ingenico::pg_hba_rule"][key] != value: reject_rules.append(key)
                else: proper_new_file["psql_ingenico::pg_hba_rule"][key] = value
        else: proper_new_file["psql_ingenico::pg_hba_rule"][key] = value

new=yaml.dump(proper_new_file, indent=6, default_flow_style=False)
print("\n-----------\nLe nouveau common.yaml merge:\n-----------\n" + new.replace("'","\"").replace("\"\"","'"))
print("\n-----------\nLes regles en doublon:\n-----------\n" + ", ".join(reject_rules))

