import sqlite3
import os

DB_PATH = 'dcim_metrics.db'

def initialize_database():
    if os.path.exists(DB_PATH):
        print(f"[*] {DB_PATH} already exists. Skipping initialization.")
        return

    print(f"[*] Initializing new database: {DB_PATH}...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create Telemetry Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp_ns INTEGER NOT NULL,
            rack_id INTEGER NOT NULL,
            cpu_power_mw INTEGER NOT NULL,
            anomaly_score REAL DEFAULT 0.0
        )
    ''')
    
    conn.commit()
    conn.close()
    print("[+] Database initialization complete.")

if __name__ == "__main__":
    initialize_database()