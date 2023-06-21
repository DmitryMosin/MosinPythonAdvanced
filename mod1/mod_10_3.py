import sqlite3

if __name__ == "__main__":

    with sqlite3.connect("hw_3_database.db") as conn:
        cursor = conn.cursor()

        # =====================================================================
        # ===== TASK 1: How many records (rows) are stored in each table? =====
        # =====================================================================

        for i in range(1, 4):

            cursor.execute(f"""
                SELECT COUNT(*) as 'records_count'
                FROM table_{i}
            """)

            result = cursor.fetchone()
            print(f'In table_{i} - {result}')

        # =======================================================================================
        # ===== TASK 2: How many unique orders are there in table_1? ============================
        # ===== (Let's call unique records that has not previously been found in the table) =====
        # =======================================================================================

        cursor.execute("""
            SELECT COUNT(*) as 'Unique_records_count'
            FROM ( 
                SELECT DISTINCT value
                FROM table_1 ) as 'Unique_records'
        """)

        result = cursor.fetchone()
        print(result)

        # ===================================================================
        # ===== TASK 3: How many records from table_1 occur in table_2? =====
        # ===================================================================

        cursor.execute("""
            SELECT COUNT(*) as 'Intersect_count'
            FROM (
                SELECT value
                FROM table_1
                INTERSECT 
                SELECT value
                FROM table_2
            ) as 'Intersect_tables'
        """)

        result = cursor.fetchone()
        print(result)

        # ==================================================================================
        # ===== TASK 4: How many records from table_1 occur in table_2 and in table_3? =====
        # ==================================================================================

        cursor.execute("""
            SELECT COUNT(*) as 'Intersect_count' 
            FROM (
                SELECT value
                FROM table_1
                INTERSECT 
                SELECT value
                FROM table_2
                INTERSECT 
                SELECT value
                FROM table_3
            ) as 'Intersect_tables'
        """)

        result = cursor.fetchone()
        print(result)


