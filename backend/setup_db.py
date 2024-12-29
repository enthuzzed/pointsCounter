import sqlite3

# Database file path
DATABASE = 'database/trader.db'

def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        wallet_address TEXT UNIQUE,
        points INTEGER DEFAULT 0,
        last_claimed TIMESTAMP
    );
    ''')

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == '__main__':
    setup_database()
