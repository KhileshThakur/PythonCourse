import psycopg2

try:
    connection=psycopg2.connect(
        dbname="PythonConnectivity",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Database Connected") 
except Exception as e:
    print("Error: ", e)
    
    
#Cursor allows you to execute SQL query
def createTable():
    try:
        cursor = connection.cursor()
        create_table="""
        CREATE TABLE IF NOT EXISTS emp(
            id SERIAL PRIMARY
            name VARCHAR(50) 
            age INTEGER
            dept VARCHAR(50)
        );
        """
        cursor.execute(create_table)
        connection.commit()
        print("Table Created Successfully!")
    except Exception as e:
        print("Error: ", e)
        
        
def insert_data(connection, name, age, dept):
    try:
        with connection.cursor() as cursor:
            query="INSERT INTO  emp(name, age, dept) VALUES(%s, %s, %s)"
            cursor.execute(query, (name, age, dept))
            connection.commit()
            print(f"Data is inserted successfully! {name}, {age}, {dept}")
    except Exception as e:
        print("Error: ", e)
        

insert_data(connection, "Khilesh", 21, "IT")


def fetch_all_data(connection):
    try:
        with connection.cursor() as cursor:
            query="SELECT * FROM emp;"
            cursor.execute(query)
            rows=cursor.fetchall()
            print("Employee Information")
            for row in rows:
                print(row)
    except Exception as e:
        print("Error: ", e)
        
fetch_all_data(connection)


def fetch_by_dept(connection, dept):
    try:
        with connection.cursor() as cursor:
            query="SELECT * FROM emp WHERE dept=%s;"
            cursor.execute(query, (dept,))
            rows=cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print("Error: ", e)
fetch_by_dept(connection, "IT")


def update_info(connection, age, dept, name):
    try:
        with connection.cursor() as cursor:
            query="UPDATE emp SET age=%s, dept=%s WHERE name=%s;"
            cursor.execute(query, (age, dept, name))
            connection.commit()
            print(f"Emmployee {name, age, dept}")
    except Exception as e:
        print("Error : ", e)        

update_info(connection, 22, "PDA", "Khilesh")
fetch_all_data(connection)



def delete_info(connection, name):
    try:
        with connection.cursor() as cursor:
            query="DELETE FROM emp WHERE name=%s"
            cursor.execute(query, (name,))
            connection.commit()
            print(f"Employee {name} Deleted")
    except Exception as e:
        print("Error : ", e)

delete_info(connection, "Khilesh")
fetch_all_data(connection)

def close_fun(connection):
    if connection:
        connection.close()
        print("Database Connection Closed")
        
close_fun(connection)