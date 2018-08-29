# movegeeks
The description of the code files is as below
### data_simulator.py
This script simulates the data generation as an IOT device would be generating the data.
This script simulates and stores a batch of data to be processed and derive statistics from it. It finally exports a batch of simulated data.

### hotspots.py
This script is the main script. This script fires the data_simulator and processes the generated data and exports into hotspots.csv file. This file contains an extra column containing hotspot_magnitude(0-100) which is calculated/predicted by the analysing the behaviour of the buses and their alarm type generated for a specific speed. 
Using the data, anomalies/accident hotspot magnitudes are predicted for each record in the hotspots.csv
After predicting the hotspot magnitudes, a rating score (0-10) is assigned to each bus/bus driver depicting its behaviour on road in a given ward/zone.

Execute the hotspots.py file <br>
$ python hotspots.py

### Tableau Dashboard Links
https://public.tableau.com/views/Bangaloretrafficalerts/Dashboard1?:embed=y&:display_count=yes
https://public.tableau.com/shared/Z62H2Z8HD?:display_count=no
