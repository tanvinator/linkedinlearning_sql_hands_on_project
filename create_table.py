#Importing libraries 
import pandas as pd
import pyodbc


#use this statement in order to see all the columns in the dataframe
#pd.set_option('display.max_columns', None )

# Importing CSV
#in jupyter single slash doesn't work. You will get path from system like this:
#path = 'C:\Users\tanvi\Desktop\SQL\LinkedIn Learning\Ex_Files_Hands_On_Data_Sci_1\Exercise Files\dates.csv'
#but convert it like this
path_dates = 'C:\\Users\\tanvi\\Desktop\\SQL\\LinkedIn Learning\\Ex_Files_Hands_On_Data_Sci_1\\Exercise Files\\dates.csv'
path_employees = 'C:\\Users\\tanvi\\Desktop\\SQL\\LinkedIn Learning\\Ex_Files_Hands_On_Data_Sci_1\\Exercise Files\\employees.csv'
data_dates = pd.read_csv(path_dates)
data_employees = pd.read_csv(path_employees)

###### TIP:
#To study the tables you can use these 

#to get information about type and quality of data
#data_dates.info()

#to get details about the variation in data of a particular column
#data_employees['ParentEmployeeKey'].describe()
#######

#Converting date type data into acceptable date format using pandas
data_dates['FullDateAlternateKey'] = pd.to_datetime(data_dates['FullDateAlternateKey'])
#to visualize if it worked:
# data_dates[DateAlternateKey'].head()
#if you have multiple columns with date type data, make a list and insert a for loop
date_cols_data_employees = ['HireDate', 'BirthDate', 'StartDate', 'EndDate']
for date in date_cols_data_employees:
    data_employees[date] = pd.to_datetime(data_employees[date])
    #to visualize: 
    # print(data_employees[date].head())


# Connect to SQL Server
conn = pyodbc.connect("DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=localhost;DATABASE=linkedin;USER=root;PASSWORD= *********;OPTION=3;")
cursor = conn.cursor()


# Create Tables
# Key points: 
#
# 1. Take care of the column count, and names
#     A tip will be to print a list of column names using the code below and easily copying and pasting column names:
# cols_dates = list(data_dates.columns)
#cols_employees = list(data_employees.columns)
#
# 2. Take care of the datatypes. Refer to the dataframe display and use correct data types
#    Data types that can be used are:
#     INT (# of digits), VARCHAR(# of characters), DATE (YYYY-MM-DD),
#     DECIMAL(# of sig figs, # of decimal places),
#     FLOAT(# of sig figs, # of decimal places), etc.
#
# 3. Take care that decimal datatype does not take in NULL values
#
# 4. Take care of the date format.
#
# 5. For writing phone numbers, use VARCHAR, because INT value may remove ending or beginning zeros, also the format might be different in different countries
#
# TABLE: dates 
cursor.execute('CREATE TABLE IF NOT EXISTS dates (DateKey INT(20),  FullDateAlternateKey DATE, DayNumberOfWeek INT(2), EnglishDayNameOfWeek VARCHAR(15), SpanishDayNameOfWeek VARCHAR(15), FrenchDayNameOfWeek VARCHAR(15), DayNumberOfMonth INT(3), DayNumberOfYear INT(4), WeekNumberOfYear INT(3), EnglishMonthName VARCHAR(15), SpanishMonthName VARCHAR(15), FrenchMonthName VARCHAR(15), MonthNumberOfYear INT(3), CalendarQuarter INT(2), CalendarYear INT(5), CalendarSemester INT(3), FiscalQuarter INT(2), FiscalYear INT(5), FiscalSemester INT(2))')
#TABLE : employees
cursor.execute('CREATE TABLE IF NOT EXISTS employees (EmployeeKey INT(4),  ParentEmployeeKey VARCHAR(50), EmployeeNationalIDAlternateKey INT(15), ParentEmployeeNationalIDAlternateKey VARCHAR(15), SalesTerritoryKey INT(3), FirstName VARCHAR(20), LastName VARCHAR(20), MiddleName VARCHAR(20), NameStyle INT(5), Title VARCHAR(150), HireDate DATE, BirthDate DATE, LoginID VARCHAR(128), EmailAddress VARCHAR(128), Phone VARCHAR(25), MaritalStatus VARCHAR(5), EmergencyContactName VARCHAR(40), EmergencyContactPhone VARCHAR(20), SalariedFlag INT(5), Gender VARCHAR(5), PayFrequency INT(2), BaseRate DECIMAL(6,2), VacationHours INT(3), SickLeaveHours INT(3), CurrentFlag INT(2), SalesPersonFlag INT(2), DepartmentName VARCHAR(50), StartDate DATE, EndDate DATE, Status VARCHAR(20))')

# Insert DataFrame to Table: dates
for row in data_dates.itertuples():
    cursor.execute('''
                INSERT INTO dates
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.DateKey , 
                row.FullDateAlternateKey ,
                row.DayNumberOfWeek ,
                row.EnglishDayNameOfWeek ,
                row.SpanishDayNameOfWeek ,
                row.FrenchDayNameOfWeek ,
                row.DayNumberOfMonth ,
                row.DayNumberOfYear ,
                row.WeekNumberOfYear ,
                row.EnglishMonthName ,
                row.SpanishMonthName ,
                row.FrenchMonthName ,
                row.MonthNumberOfYear ,
                row.CalendarQuarter ,
                row.CalendarYear ,
                row.CalendarSemester ,
                row.FiscalQuarter ,
                row.FiscalYear ,
                row.FiscalSemester
                  )

# Insert DataFrame to Table: employees
for row in data_employees.itertuples():
    cursor.execute('''
                INSERT INTO employees
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.EmployeeKey , 
                row.ParentEmployeeKey ,
                row.EmployeeNationalIDAlternateKey ,
                row.ParentEmployeeNationalIDAlternateKey ,
                row.SalesTerritoryKey ,
                row.FirstName ,
                row.LastName ,
                row.MiddleName ,
                row.NameStyle ,
                row.Title ,
                row.HireDate ,
                row.BirthDate ,
                row.LoginID ,
                row.EmailAddress ,
                row.Phone ,
                row.MaritalStatus ,
                row.EmergencyContactName ,
                row.EmergencyContactPhone ,
                row.SalariedFlag ,
                row.Gender ,
                row.PayFrequency ,
                row.BaseRate ,
                row.VacationHours ,
                row.SickLeaveHours ,
                row.CurrentFlag ,
                row.SalesPersonFlag ,
                row.DepartmentName ,
                row.StartDate ,
                row.EndDate ,
                row.Status
                  )

#Final step:
#to commit the values into the table
conn.commit()

print('Hooray! tables created in database')

# Now run your queries in MYSQL and enjoy quering.
#************************************************************#






