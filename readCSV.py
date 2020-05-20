import pandas as pd
import numpy
c=numpy.recfromcsv(
    'C:\Program Files (x86)\Python38-32\Lib\site-packages\matplotlib\mpl-data\sample_data\msft.csv',
  encoding='utf-8' )
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth',1000)
print(c)