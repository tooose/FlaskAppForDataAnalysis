# FlaskAppForDataAnalysis
Flask application for data analysis

Description
This Flask application provides two API endpoints to retrieve spending information from a SQLite database.

Installation

Make sure you have Python installed.
Install Flask using pip install Flask.
Install pymongo using pip install pymongo.
Install sqlite3 using pip install sqlite3.
Usage
Start the Flask application by running the Python script.
Access the following endpoints:
/total_spend/<int:user_id>: Get total spending by user ID.
/average_spending_by_age/: Get average spending by age range.
API Endpoints

Total Spend By User
Endpoint: /total_spend/<int:user_id>
Method: GET
Description: Retrieves the total spending of a user based on user ID.
Parameters:
user_id (int): ID of the user.
Response:
user_id (int): ID of the user.
total_spending (float): Total spending of the user.
Average Spending By Age
Endpoint: /average_spending_by_age/
Method: GET
Description: Retrieves the average spending by age range.
Response:
TBD
Database
SQLite Database Path: C:\\Users\\Juzer\\Desktop\\FlaskApp\\users_vouchers.db
Feel free to explore and use the API endpoints provided by this application!

