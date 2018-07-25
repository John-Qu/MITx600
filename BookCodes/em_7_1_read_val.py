def read_val(val_type, request_msg, error_msg):
    while True:
        val = input(request_msg + " ")
        try:
            return(val_type(val))
        except ValueError:
            print(val, error_msg)


def test_read_val():
    print(read_val(int, "Enter an integer:", "is not an integer"))


test_read_val()