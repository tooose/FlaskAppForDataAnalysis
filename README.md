Certainly! Below is the `README.md` file for your code:

```markdown
# Flask Application for Analyzing User Spending

This Flask application provides endpoints for analyzing user spending data stored in a SQLite database and writing aggregated results to a MongoDB database.

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Install the required dependencies:

```bash
pip install flask pymongo
```

3. Ensure you have SQLite and MongoDB installed and running on your system.

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Access the following endpoints:

- `/total_spend/<int:user_id>`: Retrieves the total spending by a user based on user ID.
- `/average_spending_by_age/`: Calculates the average spending by age range.
- `/write_to_mongodb/`: Writes data to MongoDB.

## Endpoints

### Total Spend by User

- **URL:** `/total_spend/<int:user_id>`
- **Method:** GET
- **Parameters:**
  - `user_id`: Integer representing the user ID.
- **Response:**
  - JSON object with the following structure:
    ```json
    {
        "user_id": <user_id>,
        "total_spending": <total_spending>
    }
    ```
  
### Average Spending by Age Range

- **URL:** `/average_spending_by_age/`
- **Method:** GET
- **Response:**
  - JSON object with the average spending for different age ranges:
    ```json
    {
        "age_18_24": <avg_spending>,
        "age_25_30": <avg_spending>,
        "age_31_36": <avg_spending>,
        "age_37_46": <avg_spending>,
        "age_47": <avg_spending>
    }
    ```

### Write to MongoDB

- **URL:** `/write_to_mongodb/`
- **Method:** POST
- **Body:** JSON object containing `user_id` and `total_spending`.
- **Response:**
  - Success:
    ```json
    {
        "message": "Data written to MongoDB successfully."
    }
    ```
  - Error:
    ```json
    {
        "message": "Error writing to MongoDB: <error_message>"
    }
    ```

## Database Configuration

- SQLite database path: `C:\\Users\\Juzer\\Desktop\\FlaskApp\\users_vouchers.db`
- MongoDB connection: Localhost

## Dependencies

- Flask: Web framework for Python.
- PyMongo: Python driver for MongoDB.

