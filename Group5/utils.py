

def eval_bool(bool_str):
    if bool_str == 'TRUE':
        return True
    elif bool_str == 'FALSE':
        return False
    else:
        raise Exception(f"This is not a valid format for a boolean value: {bool_str}, please validate your data.")
    

import pandas as pd

def style_df(df):
    return (df.style
            .set_properties(**{'font-family': 'Arial, sans-serif', 
                               'font-size': '16px', 
                               'line-height': '1.5',
                               'color': '#fff'}) 
            .set_table_styles([{'selector': 'thead',
                                'props': [('background-color', '#006600'), 
                                          ('color', '#fff')]},
                               {'selector': 'th',
                                'props': [('color', '#fff')]},
                               {'selector': 'td',
                                'props': [('border', 'none')]},
                               {'selector': 'tr:nth-of-type(odd)',
                                'props': [('background-color', '#51557E')]},  # change to dark purple
                               {'selector': 'tr:hover',
                                'props': [('background-color', '#51557E')]}]))  # change to dark purple
