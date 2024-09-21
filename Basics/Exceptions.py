import sys

def linux_fun():
    print(f'Curent Platform is {sys.platform}')
    if sys.platform != "win32":
        raise Exception(f"This code is run only on liux system current plateform is  {sys.platform}")
    else:
        print("Success!")

def system_info():
    import platform
    print(platform.architecture())
    print(platform.machine())
    print(platform.processor())

def exception_1():
    user_input = int(input("Enter int value: "))
    num = 100
    try:
        ans = int(num/user_input)
        print(ans)            
    except:
        print("Exception Occured")

def exception_2():
    usr_in = int(input("Enter int number: "))
    try:
        assert usr_in%2==0
        print("Even")
    except ZeroDivisionError as zd:
        print("Exception Zero", zd.__traceback__)
    except Exception as e:
        print("Exception ", e)
    else:
        print("Sucess!")
    finally:
        print("Code End!")


def exception_3():
    try:
        usr_in = int(input("Enter the number: "))
        ans = 10/usr_in
        print(ans)
    except ValueError as v:
        print(f'Value Error Occure ', v)
    except ZeroDivisionError as z:
        print(f'Zero Division Error ', z)
    except Exception as e:
        print(f'Exception Occured ', e)
    else:
        print(f'Code run successfully')
    finally:
        print(f'Code End')


if __name__ == '__main__':
    # exception_1()
    # exception_2()
    exception_3()

    # linux_fun()
    # system_info()