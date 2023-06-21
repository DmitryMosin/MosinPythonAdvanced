import sqlite3

if __name__ == "__main__":

    with sqlite3.connect("hw_4_database.db") as conn:
        cursor = conn.cursor()

        # ================================================================================
        # ===== TASK 1: Find out how many people from island N are below the poverty =====
        # ===== line, that is, they receive less than 5,000 guilders per year ============
        # ================================================================================

        cursor.execute(f"""
            SELECT COUNT(*) as 'poor_count'
            FROM salaries
            WHERE salaries.salary < 5000
        """)

        result = cursor.fetchone()
        print(result)

        # =================================================================
        # ===== TASK 2: Calculate the average salary for the island N =====
        # =================================================================

        cursor.execute(f"""
            SELECT AVG(salaries.salary) as 'avg_salary'
            FROM salaries
        """)

        result = cursor.fetchone()
        print(result)

        # ================================================================
        # ===== TASK 3: Calculate the median salary for the island N =====
        # ================================================================

        # Get the median borders
        cursor.execute(f"""
            SELECT COUNT(*) as 'salaries_count'
            FROM salaries
        """)
        salaries_count = cursor.fetchone()[0]
        if salaries_count % 2 == 0:
            lower_bound = int((salaries_count - 2) / 2)
            steps = 2
        else:
            lower_bound = int((salaries_count + 1) / 2)
            steps = 1

        # Get the median
        cursor.execute(f"""
            SELECT AVG(salary) as 'median_salary'
            FROM (
                SELECT salary
                FROM salaries
                ORDER BY salaries.salary
                LIMIT {steps}
                OFFSET {lower_bound}
            ) as 'median_range'
        """)

        result = cursor.fetchone()
        print(result)

        # ===============================================================================
        # ===== TASK 4: Calculate the number of social inequality F, defined ============
        # ===== as F = T/K, where T is the total income of 10% of the wealthiest ========
        # ===== inhabitants of the island N, K is the total income of the remaining =====
        # ===== 90% of people. Print the answer as a percentage with an accuracy ========
        # ===== of two decimal places. ==================================================
        # ===============================================================================







