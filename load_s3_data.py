# To load S3 csv, need to do `pip install s3fs`
import pandas as pd

# Somtimes you don't know the delimiter, put `error_bad_lines=False` in `read_csv()` function might help
df = pd.read_csv('s3://[file_path]',  # get the file path from S3
                 delimiter='|',
                 nrows=10)
