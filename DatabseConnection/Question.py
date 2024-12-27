'''
Create a table grades with columns
student_id, subject and score

- insert grades for multiple students 
- calculate the average score of student across all subjects 
- find the highest score in a specific subject 
- display the top 3 students based on their average score
'''

import psycopg2

# Establish the connection to the PostgreSQL database
def get_connection():
    try:
        connection = psycopg2.connect(
            dbname="PythonConnectivity",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
    

def create_table():
    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                student_id INT PRIMARY KEY,
                subject VARCHAR(50),
                score INT
            )
        ''')
        connection.commit()
        print("Table created successfully.")
    except Exception as e:
        print("Error creating table:", e)
    finally:
        cursor.close()
        connection.close()


def insert_grades(data):
    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        cursor.executemany('''
            INSERT INTO grades (student_id, subject, score) VALUES (%s, %s, %s)
        ''', data)
        connection.commit()
        print("Grades inserted successfully.")
    except Exception as e:
        print("Error inserting grades:", e)
    finally:
        cursor.close()
        connection.close()


def calculate_average_scores(student_id):
    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        cursor.execute('''
            SELECT AVG(score) AS average_score
            FROM grades
            WHERE student_id = %s
        ''', (student_id,))
        result = cursor.fetchone()  # Use fetchone for a single result
        return result[0]  # Return the average score
    except Exception as e:
        print("Error calculating average scores:", e)
    finally:
        cursor.close()
        connection.close()



def find_highest_score(subject):
    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        cursor.execute('''
            SELECT subject, MAX(score) AS highest_score
            FROM grades
            WHERE subject = %s
            GROUP BY subject
        ''', (subject,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print("Error finding highest score:", e)
    finally:
        cursor.close()
        connection.close()

def get_top_students(limit=3):
    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    try:
        cursor.execute('''
            WITH student_averages AS (
                SELECT student_id, AVG(score) AS average_score
                FROM grades
                GROUP BY student_id
            )
            SELECT student_id, average_score
            FROM student_averages
            ORDER BY average_score DESC
            LIMIT %s
        ''', (limit,))
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Error retrieving top students:", e)
    finally:
        cursor.close()
        connection.close()







grades_data = [
    (1, 'Math', 85), (15, 'Science', 90), (11, 'English', 88),
    (2, 'Math', 78), (21, 'Science', 82), (12, 'English', 80),
    (3, 'Math', 92), (31, 'Science', 87), (13, 'English', 85),
    (4, 'Math', 70), (41, 'Science', 75), (14, 'English', 72)
]


# create_table()
# insert_grades(grades_data)
average_score = calculate_average_scores(1)
print(f"Average score for student {1}: {average_score}")
print(find_highest_score('Math'))
print(get_top_students())
