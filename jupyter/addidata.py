
from jupyter.hydrogen import *
import pandas as pd
from colajob import *
import fileinput
from colajob import models
import re
from datetime import datetime

DATA_PATH

#============================================================
"""Loader."""
#============================================================


# ------------------------------------------------------------
"""job_titles.csv"""
# ------------------------------------------------------------


df = pd.read_csv('/Users/sambong/pjts/colajob/dataset/Additional data/job_titles.csv')

df.info()

df = df.rename(columns={'311 DIRECTOR':'direc'})
direcs = list(df.direc.unique())
len(direcs)

sorted(direcs)

# ------------------------------------------------------------
"""kaggle_data_dictionary.csv"""
# ------------------------------------------------------------


dictionary = pd.read_csv('/Users/sambong/pjts/colajob/dataset/Additional data/kaggle_data_dictionary.csv')

dictionary.info()
df = df.rename(columns={'311 DIRECTOR':'direc'})
'Field Name':'fieldname',
'Annotation Letter':'annotation_letter',
'Description':'description',
'Data Type':'dtype',
'Allowable Values':'allowabel_value',
'Accepts Null Values?',
'Additional Notes'


cols = list(dictionary.columns)
for col in cols:
    unqs = list(dictionary[col].unique())
    print(f"{'-'*60}\n {col} : {len(unqs)}")
    pp.pprint(unqs)

dictionary
df = df.rename(columns={'311 DIRECTOR':'direc'})
direcs = list(df.direc.unique())
len(direcs)

sorted(direcs)



# ------------------------------------------------------------
"""JobBullentinsLoader"""
# ------------------------------------------------------------

bulletin_path = f"{DATA_PATH}/Job Bulletins"
for root, dirs, files in os.walk(bulletin_path):
    print('-'*60)
    print(f"root : {root}")
    print(f"dirs : {dirs}")
    print(f"files : {files}")






class JobBullentin(models.JobBullentin):

    def __init__(self):
        super().__init__()

    def load_targets(self):
        pass

    def _title(self):
        pass

    def _open_date(self):
        pass

    def _requirements(self):
        pass

jb = JobBullentin()
jb.__dict__

Open Date: 04-18-14




files = sorted(files)
files[0]

p_opendate = re.compile(pattern='^(Open Date):\s*(\d+-\d+-\d+)', flags=re.I)



# for line in fileinput.input(files=f"{bulletin_path}/{files[0]}"):
with open(file=f"{bulletin_path}/{files[0]}", mode='r') as f:
    for line in f:
        # print(f"{'-'*60}\n line : {line}")
        line = line.strip()
        m = p_opendate.search(string=line)
        if m is None:
            pass
        else:
            print(f"m : {m}")
            print(f"m.groups() : {m.groups()}")
            tpl = m.groups()
            jb.open_date = datetime.strptime(tpl[1], '%m-%d-%y')
            # jb.open_date = line
        """parser"""


tpl
tpl[1]
datetime.strptime(tpl[1], '%m-%d-%y')

jb.open_date
