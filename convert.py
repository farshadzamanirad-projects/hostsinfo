import pandas as pd
from sys import argv

csvfile = argv[1]
read_file = pd.read_csv (csvfile)
read_file.to_excel (csvfile.rsplit('.', 1)[0] + '.xlsx', index = None, header=True)
