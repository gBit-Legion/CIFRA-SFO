from apv_data import ApvData
from database import Database
import psycopg2
import io
import csv

cur = Database().get_cursor()

cur.execute("SELECT * FROM arrival_profile_data")
rows = cur.fetchall()
output = io.StringIO()
writer = csv.writer(output.getvalue())
writer.writerow(['checkin_terminal', 'airline_grouped_hash', 'arrival_profile', 'value','season'])
for row in rows:
    writer.writerow(row)
output.seek(0)
with open('arrival_profile_value.csv', 'w', newline='') as f:
    f.write(output.getvalue())

cur.execute("SELECT * FROM arrival_profile_value")
rows = cur.fetchall()
output = io.StringIO()
writer = csv.writer(output.getvalue())
writer.writerow(['ts', 'checkin_terminal', 'airline_grouped_hash', 'pax_arrival_profile'])
for row in rows:
    writer.writerow(row)
output.seek(0)
with open('arrival_profile_value.csv', 'w', newline='') as f:
    f.write(output.getvalue())

model = ApvData("arrival_profile_value.csv", "arrival_profile_data.csv")
model.read_data()
model.build_model()
model.make_predictions()