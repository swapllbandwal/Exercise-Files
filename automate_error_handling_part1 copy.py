try:
    num = int(input("enter a number : "))
    result = 10/num 
    print("The result is : ",result);
except ZeroDivisionError:
    print("you cann not devide by zero")
except Exception as e:
    print("exception error occurerd as : ", e)
finally:
    print("this sis finally block")