import pandas as pd



import pandas_profiling

df = pd.read_csv("G:\WorkingData\Work @ Home\Insecurity\E3-2019-Approved-Media-List-1-1.csv")
pandas_profiling.ProfileReport(df).to_file("G:\WorkingData\Work @ Home\Insecurity\ProfileReport.html")



from pivottablejs import pivot_ui

df = pd.read_csv("G:\WorkingData\Work @ Home\Insecurity\E3-2019-Approved-Media-List-1-1.csv")
pivot_ui(df)



from pydqc.data_compare import distribution_compare_pretty

train = pd.read_csv("G:\WorkingData\Work @ Home\Insecurity\E3-2019-Approved-Media-List-1-1.csv")
test = pd.read_csv("G:\WorkingData\Work @ Home\Insecurity\E3-2019-Approved-Media-List-1-1-1.csv")
#distribution_compare_pretty(train, test, "SOME COLUMNS", figsize=None)



