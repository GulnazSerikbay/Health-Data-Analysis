Mini project on analyzing the user's health data using python's ML libraries. Includes Data collection, Data Wrangling and Modeling in a Jupyter Notebook.

Data was collected from the IOS mobile application that tracks the health data.  

The datasets for each user is different according to the settings established by the user. For example, one user might block the tracking option for walking speed, while the other user allows it.

All the available data from the health app was exported as xml file, which contained a spreadsheet with every data on one page from March 2020. I removed the columns with technical details and some tables that were private to a user. Also, I selected the data from the most recent 2 months for every feature datasets (stepcount, walking speed, distance, etc) manually and rearranged them in separate csv files for convenience. 


How to test:
the interface is on file main.py. You have to install tkinter and PIL to run the program. Now, it shows the plot of the last recorded stpes and trains the model if to click on the second button.
Initial datasets are in datasets folder.
Recreated datasets are in GUI folder.
