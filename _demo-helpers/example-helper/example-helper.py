# THIS SECTION ENSURES WE CAN USE LOCAL MODULES
# Add this below main imports but ABOVE internal imports
import sys
sys.path.insert(0, '.')
# THIS SECTION ENSURES WE CAN USE LOCAL MODULES

# PARAM CONSTRUCTOR IMPORT
from _assets.helper_param_constructor import helper_param_constructor

# STATIC CLASS DECLERATION
class example_helper(object):

    # THIS METHOD DEMONSTRATES HOW TO GET PARAMETERS FROM THE COMMAND LINE
    @staticmethod
    def start():
        params = helper_param_constructor.eval()
        for param in params:
            print(param[0], param[1])

# USE THIS FOR SCRIPT ENTRY
if __name__ == "__main__":
    example_helper.start()
# END