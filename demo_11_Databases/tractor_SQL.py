# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 6315: Python for Business Analytics
#
# Name:
#
# Date:
#
##################################################
#
# Sample Script for Assignment 4:
# Creating a Database, Populating it with Data
# and Obtaining Data from a Database
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

import pandas as pd
import os

# To pass SQL queries to a database
# you would import some kind of API 
# to interact with the database
# We will continue using sqlite3
import sqlite3 as dbapi

# Import a module for estimating regression models.
import statsmodels.formula.api as sm # Another way to estimate linear regression
# This is a "light duty" modeling package designed to mimic the interface in R.


##################################################
# Set up Workspace
##################################################


# Find out the current directory.
os.getcwd()

# Get the path where you saved this script.
# This only works when you run the entire script (with the green "Play" button or F5 key).
print(os.path.dirname(os.path.realpath(__file__)))
# It might be comverted to lower case, but it gives you an idea of the text of the path. 
# You could copy it directly or type it yourself, using your spelling conventions. 

# Change to a new directory.

# You could set it directly from the location of this file
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Check that the change was successful.
os.getcwd()
# I got lower case output, even though my folders have some upper case letters.
# But anyway, it works.



##################################################
# Question 1: Create a Database
#     and Load Sales Data
##################################################

# In this example, we will create a table 
# to store the tractor sales data. 


#--------------------------------------------------
# a. Create a new database called tractors.db.
#--------------------------------------------------


con = dbapi.connect('tractors.db')


##################################################
# Read Spreadsheet and Sales Data
##################################################


tractor_xlsx = pd.ExcelFile('tractor_data.xlsx')

# Read the data from the sheet with tractor sales data.
tractor_sales_csv = pd.read_excel(tractor_xlsx,  'tractor_sales')


# Describe the contents of that file.
tractor_sales_csv.describe()

tractor_sales_csv.columns



#--------------------------------------------------
# b. Create a table in the database.
#--------------------------------------------------



# b. Make a database table called Sales that will 
# hold the name of the sale_id (INTEGER), 
# the age (REAL), 
# and the price (REAL). 


cur = con.cursor()
cur.execute('''CREATE TABLE Sales(
    sale_id TEXT, 
    saleprice REAL, 
    age REAL, 
    enghours REAL, 
    johndeere INTEGER, 
    spring INTEGER, 
    summer INTEGER, 
    winter INTEGER)''')
con.commit()



#--------------------------------------------------
# c. Upload this table to the database.
#--------------------------------------------------


# Loop through the rows of the dataframe to INSERT the VALUES.
for row in tractor_sales_csv.index:
   cur.execute('INSERT INTO Sales VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
               (str(tractor_sales_csv['sale_id'][row]), 
                float(tractor_sales_csv['saleprice'][row]), 
                float(tractor_sales_csv['age'][row]), 
                float(tractor_sales_csv['enghours'][row]), 
                int(tractor_sales_csv['johndeere'][row]), 
                int(tractor_sales_csv['spring'][row]), 
                int(tractor_sales_csv['summer'][row]), 
                int(tractor_sales_csv['winter'][row]) ))
con.commit()


cur.execute('SELECT * FROM Sales')
for row in cur.fetchall():
 print(row)



#--------------------------------------------------
# d. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

cur.execute("""
            SELECT 
                sale_id,
                saleprice, 
                age, 
                enghours, 
                johndeere, 
                spring, 
                summer, 
                winter
            FROM Sales
            """)


#--------------------------------------------------
# e. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------


# Define column names
column_names = ['sale_id', 'saleprice', 'age', 'enghours', 
                'johndeere', 'spring', 'summer', 'winter'] 


# Create an empty DataFrame with the specified column names
tractor_sales = pd.DataFrame(columns = column_names)

for row in cur.fetchall():
    query_row = pd.DataFrame([list(row)], columns = column_names)
    tractor_sales = pd.concat([tractor_sales, query_row], axis = 0)



# Describe the contents of the dataframe to check the result.
tractor_sales.describe()

tractor_sales.columns



#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_sales = sm.ols(formula = 
                           "saleprice ~ age + enghours + johndeere + spring + summer + winter", 
                           data = tractor_sales).fit()


# Display a summary table of regression results.
print(reg_model_sales.summary())






##################################################
# Question 2: Load and Obtain Specification Data
##################################################


#--------------------------------------------------
# a. Read Specification Data
#--------------------------------------------------

# Read the data from the sheet with tractor sales data.
tractor_specs_csv = pd.read_excel(tractor_xlsx,  'tractor_specs')


# Describe the contents of that file.
tractor_specs_csv.describe()
tractor_specs_csv.columns


#--------------------------------------------------
# b. Create a table in the database.
#--------------------------------------------------

cur.execute('''CREATE TABLE Specs(
        sale_id TEXT, 
        horsepower REAL, 
        diesel INTEGER, 
        fwd INTEGER, 
        manual INTEGER)''')
con.commit()


#--------------------------------------------------
# c. Upload this table to the database.
#--------------------------------------------------


# Loop through the rows of the dataframe to INSERT the VALUES.
for row in tractor_specs_csv.index:
   cur.execute('INSERT INTO Specs VALUES (?, ?, ?, ?, ?)', 
               (str(tractor_specs_csv['sale_id'][row]), 
                float(tractor_specs_csv['horsepower'][row]), 
                int(tractor_specs_csv['diesel'][row]), 
                int(tractor_specs_csv['fwd'][row]), 
                int(tractor_specs_csv['manual'][row]) ))
con.commit()


cur.execute('SELECT * FROM Specs')
for row in cur.fetchall():
 print(row)



#--------------------------------------------------
# d. Submit a query to the database that obtains
#    the sales data joined with specification data.
#--------------------------------------------------


cur.execute("""
            SELECT 
               a.sale_id,
               a.saleprice, 
               a.age, 
               a.enghours, 
               a.johndeere, 
               a.spring, 
               a.summer, 
               a.winter,
               b.horsepower, 
               b.diesel, 
               b.fwd, 
               b.manual
            FROM Sales AS a
            LEFT JOIN
            Specs AS b
            ON a.sale_id = b.sale_id
            """)



#--------------------------------------------------
# e. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------


# Define column names
column_names = ['sale_id', 'saleprice', 'age', 'enghours', 
                'johndeere', 'spring', 'summer', 'winter', 
                'horsepower', 'diesel', 'fwd', 'manual']

# Create an empty DataFrame with the specified column names
tractor_sales_specs = pd.DataFrame(columns = column_names)

for row in cur.fetchall():
    query_row = pd.DataFrame([list(row)], columns = column_names)
    tractor_sales_specs = pd.concat([tractor_sales_specs, query_row], axis = 0)




# Describe the contents of the dataframe to check the result.
tractor_sales_specs.describe()
tractor_sales_specs.columns



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------


reg_model_sales_specs = sm.ols(formula = 
                           "saleprice ~ age + enghours + johndeere \
                               + spring + summer + winter \
                                   + horsepower + diesel + fwd + manual", 
                           data = tractor_sales_specs).fit()


# Display a summary table of regression results.
print(reg_model_sales_specs.summary())



##################################################
# Question 3: Load and Obtain Data to Indicate 
#   Tractors with Cabs
##################################################


#--------------------------------------------------
# a. Read Data to Indicate Tractors with Cabs
#--------------------------------------------------

# Read the data from the sheet with tractor performance data.
tractors_w_cabs_csv = pd.read_excel(tractor_xlsx,  'tractors_cabs')



# Describe the contents of that file.
tractors_w_cabs_csv.describe()
tractors_w_cabs_csv.columns


#--------------------------------------------------
# b. Create a table in the database.
#--------------------------------------------------

cur.execute('''CREATE TABLE Cabs(
        sale_id TEXT, 
        cab INTEGER)''')
con.commit()




#--------------------------------------------------
# c. Upload this table to the database.
#--------------------------------------------------


# Loop through the rows of the dataframe to INSERT the VALUES.
for row in tractors_w_cabs_csv.index:
   cur.execute('INSERT INTO Cabs VALUES (?, ?)', 
               (str(tractors_w_cabs_csv['sale_id'][row]), 
                int(tractors_w_cabs_csv['cab'][row]) ))
con.commit()



cur.execute('SELECT * FROM Cabs')
for row in cur.fetchall():
 print(row)



#--------------------------------------------------
# d. Submit a query to the database that obtains
#    the sales data joined with specification data
#    and then joined with the performance data.
#--------------------------------------------------


cur.execute("""
            SELECT 
               a.sale_id,
               a.saleprice, 
               a.age, 
               a.enghours, 
               a.johndeere, 
               a.spring, 
               a.summer, 
               a.winter,
               b.horsepower, 
               b.diesel, 
               b.fwd, 
               b.manual, 
               c.cab
            FROM Sales AS a
            LEFT JOIN
            Specs AS b
            ON a.sale_id = b.sale_id
            LEFT JOIN
            Cabs AS c
            ON a.sale_id = c.sale_id
            """)



#--------------------------------------------------
# e. Create a data frame and load the query.
#--------------------------------------------------


# Define column names
column_names = ['sale_id', 'saleprice', 'age', 'enghours', 
                'johndeere', 'spring', 'summer', 'winter', 
                'horsepower', 'diesel', 'fwd', 'manual', 
                'cab']

# Create an empty DataFrame with the specified column names
tractor_full = pd.DataFrame(columns = column_names)

for row in cur.fetchall():
    query_row = pd.DataFrame([list(row)], columns = column_names)
    tractor_full = pd.concat([tractor_full, query_row], axis = 0)



# Check to see the columns in the result.
tractor_full.describe()

tractor_full.columns


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(formula = 
                           "saleprice ~ age + enghours + johndeere \
                               + spring + summer + winter \
                                   + horsepower + diesel + fwd + manual + cab", 
                           data = tractor_full).fit()


# Display a summary table of regression results.
print(reg_model_full.summary())



##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
con.commit()


# Close the connection when finished. 
con.close()

# Then we can continue with this file when you have time
# to work on it later.



##################################################
# Extra code snippets
##################################################

# In case things go wrong, you can always drop the table
# and start over:
# cur.execute('DROP TABLE Sales')
# cur.execute('DROP TABLE Specs')
# cur.execute('DROP TABLE Perf')

# This can get the schema of the table,
# cur.execute("PRAGMA table_info('Sales')").fetchall()
# cur.execute("PRAGMA table_info('Specs')").fetchall()
# cur.execute("PRAGMA table_info('Perf')").fetchall()
# which states the names of the variables and the data types.



##################################################
# End
##################################################
