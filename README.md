# tdwi-accelerate-2017-python
Code and materials for the TDWI Accelerate 2017 Python Quick Camp

# From TDWI Accelerate Agenda
In this hands-on 90 min course, participants will get a quick overview of the latest trends in using Python for data science, followed by a practical workshop.

* Trends
 * Using Python to close the gap between data scientists and technical users
 * Python frameworks, IDEs, web-based notebooks, and other development tools on the rise
 * Integrating specialized Python code through language- and technology-agnostic APIs

* Instruction
 * Basic arithmetic and variables
 * Data structures such as Python lists and dictionaries, ndarrays, and Pandas DataFrames\
 * How to build Numpy arrays and perform parallel calculations
 * Creating Python functions, importing packages, and control program flow
 * How to create and customize data visualizations with matplotlib, Pandas, Seaborn, and Plotly
 * Participants will gain an understanding of how Python can provide rich data structures and functions.

# Structure for the Quick Camp
For this coding camp, we're going to the following real-world scenario to keep things interesting: We all know that the price of healthcare in the US is both out of control as well as highly variable from one provider to the next, even within a tight geographic region.  We're going to use Python to retrieve a list of facilities that all provide sleep study procedures.  We'll automatically look up some information about those providers and the demographics of that region using other websites and merge the data together.  We'll do some basic blots of the data to see if there are any interesting trends, and maybe even build a predictive model.

# Step 1: Retrieve data from Clear Health Costs
https://clearhealthcosts.com/search/?query=sleep&zip_code=94016&radius=100&submit=
* Loop over list of several CA zip codes
* Beautiful Soup for HTML parsing
* Using a 2-d list to capture the data
* Sort for uniqueness?
* Write out to Excel

# Step 2: Get demographic data for these regions
