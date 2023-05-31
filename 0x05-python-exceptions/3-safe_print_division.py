#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = int(a)/int(b)
        print("Inside result: {}".format(result))
    except Exception:
        return None
    finally:
        print("{}".format(result))
