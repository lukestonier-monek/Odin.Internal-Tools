# THIS SECTION ENSURES WE CAN USE LOCAL MODULES
# Add this below main imports but ABOVE internal imports
import sys
sys.path.insert(0, '.')
# THIS SECTION ENSURES WE CAN USE LOCAL MODULES

# REQUIRED PARAMETERS:
# NONE
class helper_param_constructor(object):
    # Returns parameters in a key value pair, file_name will ALWAYS exist
    # eg: param: -name=LUKE -> { 'file_name': '...', 'name': 'LUKE' }
    def eval() -> object:
        params = {}
        index = 0
        for arg in sys.argv:
            if (index == 0):  # First param is filename
                params['file_name'] = arg
            else:
                key_val_split = arg.replace('-', '').split('=')
                params[key_val_split[0]] = key_val_split[1]
                
            index += 1

        return params