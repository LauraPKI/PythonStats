import pandas as pd
import researchpy as rp
import scipy.stats as stats

df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")
df.info()
results = stats.ttest_ind(df['bp_after'][df['sex'] == 'Male'], df['bp_after'][df['sex'] == 'Female'])
