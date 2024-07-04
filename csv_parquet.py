import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

csv_path_file = "/Users/rujjalsada/Rujjal/Practice/Sentiment_Analysis_Amazon_Review/Reviews.csv"
df = pd.read_csv(csv_path_file)

table = pa.Table.from_pandas(df)

parquet_file_path = "/Users/rujjalsada/Rujjal/Practice/Sentiment_Analysis_Amazon_Review/Reviews.parquet"
pq.write_table(table, parquet_file_path)