from pax_data import PaxData
import warnings
from database import Database
import io
import csv

warnings.simplefilter(action='ignore', category=Warning)
cur = Database().get_cursor()

cur.execute("SELECT * FROM arrival_profile_data")
rows = cur.fetchall()
output = io.StringIO()
writer = csv.writer(output.getvalue())
writer.writerow(['checkin_terminal', 'airline_grouped_hash', 'arrival_profile', 'value','season'])
for row in rows:
    writer.writerow(row)
output.seek(0)
with open('arrival_profile_data.csv', 'w', newline='') as f:
    f.write(output.getvalue())

pax_data = PaxData("arrival_profile_data.csv")
pax_data.read_data()
pax_data.slice_data()


for i in range(3):
    result = pax_data.fit_model(i)
    df_predictions = pax_data.predict(result, i+1)
    print(df_predictions)