import sqlite3


class TelemetryRepository:

    def __init__(
        self,
        db_path="database/telemetry.db"
    ):

        self.db_path = db_path

    def initialize(self):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS telemetry_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT,
                timestamp TEXT,
                description TEXT
            )
            """
        )

        conn.commit()
        conn.close()

    def save_event(
        self,
        event_type,
        timestamp,
        description
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO telemetry_events (
                event_type,
                timestamp,
                description
            )
            VALUES (?, ?, ?)
            """,
            (
                event_type,
                timestamp,
                description
            )
        )

        conn.commit()
        conn.close()
    
    def get_all_events(self):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM telemetry_events
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    def count_events(self):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM telemetry_events
            """
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count
    
    def latest_events(
    self,
    limit=10
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM telemetry_events
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        rows = cursor.fetchall()

        conn.close()

        return rows