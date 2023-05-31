#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    for i in range(list_length):
        new_list = []
        try:
            div = my_list_1[i]/my_list_2[i]
            return div
        except TypeError:
            print("wrong type")
            div = 0
            return div
        except ZeroDivisionError:
            print("division by 0")
            div = 0
            return div
        except IndexError:
            print("out of range")
            div = 0
            return div
        finally:
            new_list[i] = div
    print(new_list)
