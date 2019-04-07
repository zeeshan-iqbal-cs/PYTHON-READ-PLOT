import json
from datetime import datetime
import matplotlib.pyplot as plt

data = json.load(open("internet-controled-car-data-export.json", "r"))
data = data["br"]["data"]["s1"]
temperature = []
timestamp = []

for tag in data:
    ts = data[tag]["timestamp"]
    ts = int(str(ts)[:10])
    ts = datetime.fromtimestamp(ts)
    timestamp.append(ts)
    temperature.append(data[tag]['temprature'])

plt.title("Baskey Robins: Temperature plot")
plt.suptitle("Stress testing 3 days")
plt.plot(timestamp, temperature, label="Temperature values")
plt.scatter(timestamp, temperature, s=3, edgecolors="k", label="sample arrived")
plt.grid()
plt.legend()
plt.show()
