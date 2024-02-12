# Named APP.
from flask import Flask, json, jsonify, request

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

