# Odin.INTERNAL-TOOLS

This project is to help with development and maintenance of the Odin Project.

## Guide
There are folders for certain types of helpers, within each folder you should create a sub folder for what part of Odin the tool is created for

Each helper required a README file with execution instructions and documentation to understand what the helper achieves

There is a demo helper file located in the _demo-helpers folder in which you can copy to create a new helper function

## Adding to package.json
Once a function has been completed use the following script template to add it to the package.json scripts array:

## Running helpers
Simply use the npm run [SCRIPT-KEY] command to execute a helper, any parameters that are required should follow: 
### DONT FORGET THE '--' BETWEEN THE SCRIPT NAME AND PARAMS TO BE PASSED
eg: npm run _demo-helpers/example-helper -- -name=LUKE
**use the 'eval' method in the 'helper_param_constructor' class to access the passed parameters in a list of tuples**

# FORMATTING
View the example-helper to see how files should be formatted and imports are used, comments are added to point out core elements required