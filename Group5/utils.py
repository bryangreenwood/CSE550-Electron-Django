

def eval_bool(bool_str):
    if bool_str == 'TRUE':
        return True
    elif bool_str == 'FALSE':
        return False
    else:
        raise Exception(f"This is not a valid format for a boolean value: {bool_str}, please validate your data.")