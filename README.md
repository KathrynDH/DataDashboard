# DataDashboard
 
The data dashboard displays graphs and charts related to youth (ages 15-24) 
literacy rates in different countries.

Link:[Youth Literacy World Bank Data Dashboard](https://datadashboard-kh.herokuapp.com/)

The website was written with Python using the Flask micro web framework.

Data was retreived from the World Bank Data API and saved as csv files.
The Python files for creating the csv files are in the data-scripts folder.
They are not used by the website and were run prior to building the site.

[World Bank Open Data](https://data.worldbank.org/)

## Files and folders
- data: csv data files
- data-scripts: Python scripts for creating the csv files
- myapp: website files including images, page templates, __init.py__ and routes.py
    -  __init.py__: Flask file
    - routes.py: file used by Flask to route each page and execute code
- webscripts: Python files used to create Plotly graphs and load data
- myapp.py: Used for directing Flask to the myapp folder for init and routes files
- requirements.txt: List of Python libraries
- runtime.txt: Python and version used

## Required Python Libraries
- Pandas
- Flask
- Plotly
- Requests
- json