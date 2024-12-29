from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import sqlite3
import os
from flask_cors import CORS

# Flask App Initialization
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

DATABASE = 'database/trader.db'

# Database Connection Function
def db_connect():
    retries = 5
    for i in range(retries):
        try:
            conn = sqlite3.connect(DATABASE, check_same_thread=False)
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA journal_mode=WAL;")  # Enable WAL mode
            return conn
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e):
                import time
                time.sleep(0.1)  # Wait 100ms before retrying
            else:
                raise
    raise sqlite3.OperationalError("Database is locked after multiple retries.")

# Register Wallet Endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    wallet = data.get('wallet_address')

    if not wallet:
        return jsonify({"status": "fail", "message": "Wallet address is required."}), 400

    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (wallet_address, points) 
            VALUES (?, 0)
            ON CONFLICT(wallet_address) DO NOTHING
        """, (wallet,))
        conn.commit()
        return jsonify({"status": "success", "message": "69er Detected!"})
    except sqlite3.OperationalError as e:
        return jsonify({"status": "fail", "message": str(e)}), 500
    finally:
        cur.close()
        conn.close()

# Claim Points Endpoint
@app.route('/claim_points', methods=['POST'])
def claim_points():
    data = request.json
    wallet = data.get('wallet_address')

    if not wallet:
        return jsonify({"status": "fail", "message": "Wallet address is required."}), 400

    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM users WHERE wallet_address = ?
        """, (wallet,))
        user = cur.fetchone()

        if user:
            last_claimed = user['last_claimed']
            if last_claimed:
                last_claimed_dt = datetime.strptime(last_claimed, '%Y-%m-%d %H:%M:%S')
                if datetime.now() - last_claimed_dt < timedelta(hours=24):
                    return jsonify({
                        "status": "fail",
                        "message": "Once a day is the way!",
                        "points": user['points']
                    })

            # Update Points and Last Claimed
            new_points = user['points'] + 10
            cur.execute("""
                UPDATE users SET points = ?, last_claimed = ? WHERE wallet_address = ?
            """, (new_points, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), wallet))
            conn.commit()
            return jsonify({
                "status": "success",
                "message": "Points claimed successfully.",
                "points": new_points
            })

        return jsonify({"status": "fail", "message": "Wallet not found."}), 404
    except sqlite3.OperationalError as e:
        return jsonify({"status": "fail", "message": str(e)}), 500
    finally:
        cur.close()
        conn.close()

# Fetch Total Points Endpoint
@app.route('/total_points', methods=['POST'])
def total_points():
    data = request.json
    wallet = data.get('wallet_address')

    if not wallet:
        return jsonify({"status": "fail", "message": "Wallet address is required."}), 400

    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT points FROM users WHERE wallet_address = ?
        """, (wallet,))
        user = cur.fetchone()

        if user:
            return jsonify({
                "status": "success",
                "points": user['points']
            })

        return jsonify({"status": "fail", "message": "Wallet not found."}), 404
    except sqlite3.OperationalError as e:
        return jsonify({"status": "fail", "message": str(e)}), 500
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    os.makedirs('database', exist_ok=True)
    app.run(debug=True, threaded=True)
