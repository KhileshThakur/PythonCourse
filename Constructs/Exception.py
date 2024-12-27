# try:
#     x=10/0
# except ZeroDivisionError:
#     print("Cannot Divide by 0")
    
# try:
#     x=int("hello")
# except ZeroDivisionError:
#     print("Cannot Divide by Zero")
# except ValueError:
#     print("invalid value")
    
    
    
# try:
#     x=10/0
# except Exception as e:
#     print(f"Error:{e}")
    
    

# try:
#     x=10/2
# except Exception as e:
#     print(f"Error:{e}")
# else:
#     print("divison success",x)
    


# try:
#     x=10/0
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     print("execution complete")
    

# def check_age(age):
#     if age<18:
#         raise ValueError("Age must be 18 or more")
#     print("Access Granted")
# try:
#     check_age(13)
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     print("Executed!")
# try:
#     check_age('adr')
# except Exception as e:
#     print(e)
    
    
    
    
# x=4
# assert x>5, "x is greater than 5"
# print("pass")


# def div(a,b):
#     assert b!=0, "Denominator should not be zero"
#     return a/b
# print(div(10/2))
# print(div(10/0))


# '''
# User input an integer. If the user enters invalid input
# the programs should retry up to 3 times before exitting an error
# '''

# max_attempt=3
# count=0
# while count < max_attempt:
#     try:
#         inp = input("Enter No. ")
#         number = int(inp)
#         print(f"You entered the no {number}")
#         break
#     except ValueError:
#         count+=1
#         rem_attempts = max_attempt-count
#         if rem_attempts >0:
#             print(f"Invalid input: {rem_attempts } attempts")
#         else:
#             print("program exited")
        
'''
Read a list of nos from a file 
calculate their sum
if the file is empty raise an EmptyFileError
if the file does nto exist raise FileNotFoundError
'''
class EmptyFileError(Exception):
    pass

def calculate_sum_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = file.readlines()
            if not numbers:
                raise EmptyFileError("The file is empty.")
            return sum(map(int, numbers))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except EmptyFileError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: File contains invalid data (non-numeric values).")

# Example usage
file_path = "numbers.txt" 
result = calculate_sum_from_file(file_path)
if result is not None:
    print("Sum of numbers:", result)

