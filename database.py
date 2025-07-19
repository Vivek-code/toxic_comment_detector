# database.py

import sqlite3
from datetime import datetime

DB_NAME = "chat_moderation.db"

def init_db():
    """Initializes the database with a new, cleaner table structure."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Table to store incoming comments (no changes here)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comment_text TEXT NOT NULL,
        timestamp DATETIME NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending'
    );
    """)

    # NEW, SIMPLIFIED table for analysis results
    # We now have dedicated columns for each score.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comment_id INTEGER,
        is_toxic BOOLEAN NOT NULL,
        toxic REAL,
        severe_toxic REAL,
        obscene REAL,
        threat REAL,
        insult REAL,
        identity_hate REAL,
        FOREIGN KEY (comment_id) REFERENCES comments (id)
    );
    """)
    conn.commit()
    conn.close()

def add_comment(comment_text):
    """Adds a new comment to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comments (comment_text, timestamp) VALUES (?, ?)",
                   (comment_text, datetime.now()))
    conn.commit()
    conn.close()

def get_pending_comment():
    """Fetches the oldest pending comment."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, comment_text FROM comments WHERE status = 'pending' ORDER BY timestamp ASC LIMIT 1")
    comment = cursor.fetchone()
    conn.close()
    return comment

def add_analysis_result(comment_id, is_toxic, scores):
    """Adds the analysis result using the new flat structure."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO analysis_results 
        (comment_id, is_toxic, toxic, severe_toxic, obscene, threat, insult, identity_hate) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        comment_id, is_toxic,
        scores.get('toxic', 0.0),
        scores.get('severe_toxic', 0.0),
        scores.get('obscene', 0.0),
        scores.get('threat', 0.0),
        scores.get('insult', 0.0),
        scores.get('identity_hate', 0.0)
    ))
    
    cursor.execute("UPDATE comments SET status = 'analyzed' WHERE id = ?", (comment_id,))
    conn.commit()
    conn.close()

def get_all_analytics():
    """Retrieves all analysis results in a clean, flat format."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = """
    SELECT
        c.comment_text,
        c.timestamp,
        r.is_toxic,
        r.toxic,
        r.severe_toxic,
        r.obscene,
        r.threat,
        r.insult,
        r.identity_hate
    FROM comments c
    JOIN analysis_results r ON c.id = r.comment_id
    ORDER BY c.timestamp DESC
    """
    cursor.execute(query)
    results = cursor.fetchall()
    # Also fetch the column names from the cursor description
    columns = [description[0] for description in cursor.description]
    conn.close()
    return columns, results