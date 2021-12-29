if __name__ == '__main__':
    n1 = input("Enter the value of n: ") # this store the string number
    n2 = input("Enter the value of n: ") # this store the string number
    try:
        ans = int(n1) / int(n2)
    except ZeroDivisionError:
        print("Zero error")
        ans = None
    except ValueError:
        print("Value error or invalid input...")
        ans = None
    # except Exception as e:
    '''
    this is simple to know the name of the error
    '''
    #     print("Exception error name is : ",type(e).__name__) # this line print the name of the error that occur during the execution of program 
    #     ans = None
    print(f"The result of two values is: {ans}")