from typing import List

# THIS SECTION ENSURES WE CAN USE LOCAL MODULES
# Add this below main imports but ABOVE internal imports
import sys
sys.path.insert(0, '.')
# THIS SECTION ENSURES WE CAN USE LOCAL MODULES

class helper_param_constructor(object):

    # Returns parameters in a list of tuples where index 0 is the key, and index 1 is the value
    # eg: param: -name=LUKE -> [(name, LUKE)]
    def eval() -> List[tuple]:
        params = []
        index = 0
        for arg in sys.argv:
            if (index == 0):  # First param is filename
                key_val = ('file_name', arg)
            else:
                key_val_split = arg.replace('-', '').split('=')
                key_val = (key_val_split[0], key_val_split[1])
                
            params.append(key_val)
            index += 1

        return params