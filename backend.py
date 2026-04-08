from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ticket_system"
)

cursor = db.cursor()

@app.route('/create_ticket', methods=['POST'])
def create_ticket():

    data = request.json

    name = data['name']
    email = data['email']
    issue = data['issue']
    priority = data['priority']

    # Ticket assignment logic
    if issue == "Technical":
        team = "Technical Support"
    elif issue == "Billing":
        team = "Billing Team"
    elif issue == "Account":
        team = "Account Team"
    else:
        team = "General Support"

    # Insert into database
    sql = "INSERT INTO tickets (name,email,issue_type,priority,assigned_team) VALUES (%s,%s,%s,%s,%s)"
    val = (name,email,issue,priority,team)

    cursor.execute(sql,val)
    db.commit()

    return jsonify({
        "message":"Ticket created successfully",
        "assigned_team":team
    })

if __name__ == '__main__':
    app.run(debug=True)