# Named APP.
from flask import Flask, json, jsonify, request
import pymongo
from pymongo import MongoClient
import sqlite3

app = Flask(__name__)




@app.route('/total_spend/<int:user_id>', methods=['GET'])
def totalSpendByUser(user_id):
    print(user_id)
    # return jsonify({"userId" : user_id})

    #db path
    db_path = 'C:\\Users\\Juzer\\Desktop\\FlaskApp\\users_vouchers.db'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('select sum(money_spent) from user_spending where user_id = ? group by user_id', (user_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        user_info = {
            'user_id': user_id,
            'total_spending': result[0]
        }
        return jsonify(user_info)
    else:
         return jsonify({'error': 'User not found'}), 404


@app.route('/average_spending_by_age/', methods=['GET'])
def averageSpendingByAgeRange():

    db_path = 'C:\\Users\\Juzer\\Desktop\\FlaskApp\\users_vouchers.db'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
    SELECT
    AVG(CASE WHEN age >= 18 AND age < 24 THEN us.money_spent END) AS avg_money_spent_18_23,
    AVG(CASE WHEN age >= 25 AND age < 30 THEN us.money_spent END) AS avg_money_spent_25_29,
    AVG(CASE WHEN age >= 31 AND age < 36 THEN us.money_spent END) AS avg_money_spent_31_36,
    AVG(CASE WHEN age >= 37 AND age < 47 THEN us.money_spent END) AS avg_money_spent_37_46,
    AVG(CASE WHEN age >= 48 AND age < 200 THEN us.money_spent END) AS avg_money_spent_48_199
    FROM user_spending us
    JOIN user_info ui ON us.user_id = ui.user_id;
                   ''')
    
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        user_info = {
            'age_18_24': result[0],
            'age_25_30': result[1],
            'age_31_36': result[2],
            'age_37_46': result[3],
            'age_47': result[4]
        }
        return jsonify(user_info)
    else:
         return jsonify({'error': 'No Data found'}), 404

@app.route('/write_to_mongodb/', methods=['POST'])
def write_to_mongodb():
    client = MongoClient()
    db=client.test_db
    myCollection = db.test_kolekcija
    data = request.get_json()
    posts = db.posts
    
      # Validate the input JSON
    if 'user_id' not in data or 'total_spending' not in data:
        return jsonify({'error': 'Invalid input JSON'}), 400
    
    # post_id = posts.insert_one({'user_id': user_id, 'total_spending': total_spending}).inserted_id
    try:
        posts.insert_one(data)
        return jsonify({'message': 'Data written to MongoDB successfully.'}), 201
    except Exception as e:
        return jsonify({'message': f'Error writing to MongoDB: {str(e)}'}), 500