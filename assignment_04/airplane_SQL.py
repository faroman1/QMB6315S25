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
# Obtaining Data from a Database
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
# Question 1: Connect to a Database
#     and Obtain Sales Data
##################################################


#--------------------------------------------------
# a. Connect to the database called airplanes.db
#     and obtain a cursor object.
#--------------------------------------------------


con = None # Code goes here

cur = None # Code goes here


#--------------------------------------------------
# b. Submit a query to the database that obtains
#    the sales data.
#--------------------------------------------------

query_1 = """
            QUERY 
                GOES
            HERE
            """
print(query_1)
cur.execute(query_1)

#--------------------------------------------------
# c. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------

# Code goes here
airplane_sales = None 

# Could use a loop with a pd.concat() command.


# Describe the contents of the dataframe to check the result.
airplane_sales.describe()

airplane_sales.columns



#--------------------------------------------------
# Fit a regression model to check progress.
#--------------------------------------------------

reg_model_sales = sm.ols(formula = 
                           "price ~ age", 
                           data = airplane_sales).fit()


# Display a summary table of regression results.
print(reg_model_sales.summary())




##################################################
# Question 2: Obtain Specification Data
##################################################




#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the sales data joined with specification data.
#--------------------------------------------------

query_2 = """
            QUERY 
                GOES
            HERE
            """
print(query_2)
cur.execute(query_2)




#--------------------------------------------------
# b. Create a data frame and load the query
#     results into a dataframe.
#--------------------------------------------------



# Code goes here
airplane_sales_specs = None 

# Could use a loop with a pd.concat() command.



# Describe the contents of the dataframe to check the result.
airplane_sales_specs.describe()
airplane_sales_specs.columns



#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_sales_specs = sm.ols(formula = 
                           "price ~ age + passengers + wtop + fixgear + tdrag", 
                           data = airplane_sales_specs).fit()


# Display a summary table of regression results.
print(reg_model_sales_specs.summary())




##################################################
# Question 3: Obtain Performance Data
##################################################



#--------------------------------------------------
# a. Submit a query to the database that obtains
#    the sales data joined with specification data
#    and then joined with the performance data.
#--------------------------------------------------

query_3 = """
            QUERY 
                GOES
            HERE
            """
print(query_3)
cur.execute(query_3)




#--------------------------------------------------
# b. Create a data frame and load the query.
#--------------------------------------------------



# Code goes here
airplane_full = None 

# Could use a loop with a pd.concat() command.



# Check to see the columns in the result.
airplane_full.describe()

airplane_full.columns


#--------------------------------------------------
# Fit another regression model.
#--------------------------------------------------

reg_model_full = sm.ols(formula = 
                           """price ~ age + passengers
                           + wtop + fixgear + tdrag + 
                           horse + fuel + ceiling + cruise""", 
                           data = airplane_full).fit()


# Display a summary table of regression results.
print(reg_model_full.summary())



##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
# con.commit()
# No changes were necessary -- only reading.

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
