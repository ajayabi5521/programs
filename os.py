import os

def get_system_info():
    #Fetches and displays system information.#
    print(f"Operating System: {os.name}")
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"System Path: {os.environ.get('PATH')}")
    print(f"User Home Directory: {os.path.expanduser('~')}")
    
def list_files_and_dirs(path="."):
    #Lists files and directories in a given path.#
    try:
        items = os.listdir(path)
        print(f"Contents of '{path}': {items}")
    except FileNotFoundError:
        print(f"Path not found: {path}")

def create_directory(dir_name):
    #Creates a new directory.#
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully!")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists!")

def remove_directory(dir_name):
    #Removes an existing directory.#
    try:
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' removed successfully!")
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found!")
    except OSError:
        print(f"Directory '{dir_name}' is not empty or cannot be removed!")

def create_file(file_name, content="Hello, this is a sample file!"):
    #Creates a file and writes content to it.#
    with open(file_name, "w") as f:
        f.write(content)
    print(f"File '{file_name}' created successfully!")

def read_file(file_name):
    #Reads and prints the content of a file.#
    try:
        with open(file_name, "r") as f:
            content = f.read()
            print(f"Contents of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found!")

def delete_file(file_name):
    #Deletes a file.#
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully!")
    except FileNotFoundError:
        print(f"File '{file_name}' not found!")

def rename_file(old_name, new_name):
    #Renames a file.#
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}'")
    except FileNotFoundError:
        print(f"File '{old_name}' not found!")

def get_environment_variable(var_name):
    #Fetches and displays an environment variable.#
    value = os.environ.get(var_name)
    if value:
        print(f"Environment Variable '{var_name}': {value}")
    else:
        print(f"Environment Variable '{var_name}' not found!")

def execute_system_command(command):
    #Executes a system command.#
    result = os.system(command)
    print(f"Executed Command: {command}, Exit Code: {result}")

if __name__ == "__main__":
    print("Starting OS Module Demonstration...\n")
    
    # System Info
    get_system_info()
    
    # Directory Operations
    list_files_and_dirs()
    create_directory("test_folder")
    list_files_and_dirs()
    remove_directory("test_folder")
    
    # File Operations
    create_file("test_file.txt")
    read_file("test_file.txt")
    rename_file("test_file.txt", "renamed_file.txt")
    delete_file("renamed_file.txt")
    
    # Environment Variables
    get_environment_variable("PATH")
    
    # System Commands
    execute_system_command("dir" if os.name == "nt" else "ls")
    
    print("\nOS Module Demonstration Completed.")
 #

""" 
import sys

def get_system_info():
    #Displays system-related information.#
    print(f"Python Version: {sys.version}")
    print(f"Version Info: {sys.version_info}")
    print(f"Platform: {sys.platform}")
    print(f"Max Unicode Character: {sys.maxunicode}")
    print(f"Recursion Limit: {sys.getrecursionlimit()}")

def list_sys_paths():
    #Lists all paths where Python searches for modules.#
    print("\nPython Module Search Paths:")
    for path in sys.path:
        print(f"- {path}")

def set_recursion_limit(limit):
    #Sets a new recursion limit.#
    sys.setrecursionlimit(limit)
    print(f"\nNew Recursion Limit Set To: {sys.getrecursionlimit()}")

def get_command_line_args():
    #Displays command-line arguments passed to the script.#
    print("\nCommand-Line Arguments:")
    for index, arg in enumerate(sys.argv):
        print(f"{index}: {arg}")

def check_python_exit():
    #Exits the Python script with a message.#
    print("\nExiting script now...")
    sys.exit(0)

if __name__ == "__main__":
    print("\nStarting sys Module Demonstration...\n")
    
    # System Information
    get_system_info()
    
    # Python Module Search Paths
    list_sys_paths()
    
    # Recursion Limit
    set_recursion_limit(2000)  # Change recursion limit to 2000
    
    # Command-Line Arguments
    get_command_line_args()
    
    # Exit Script (Uncomment to test)
    # check_python_exit()

    print("\nsys Module Demonstration Completed.")


import math

def basic_operations():
    #Performs basic mathematical operations.#
    print(f"Addition (5 + 3): {5 + 3}")
    print(f"Subtraction (5 - 3): {5 - 3}")
    print(f"Multiplication (5 * 3): {5 * 3}")
    print(f"Division (5 / 3): {5 / 3}")
    print(f"Floor Division (5 // 3): {5 // 3}")
    print(f"Modulus (5 % 3): {5 % 3}")
    print(f"Exponentiation (5 ** 3): {5 ** 3}")

def advanced_math_functions():
    #Performs advanced math operations using the math module.#
    num = 16
    angle = math.radians(30)  # Convert degrees to radians

    print(f"\nSquare Root of {num}: {math.sqrt(num)}")
    print(f"Factorial of 5: {math.factorial(5)}")
    print(f"Greatest Common Divisor (GCD) of 48 and 18: {math.gcd(48, 18)}")
    print(f"LCM of 12 and 15: {math.lcm(12, 15)}")  # Python 3.9+
    print(f"Absolute Value of -10: {math.fabs(-10)}")
    print(f"Ceiling of 3.2: {math.ceil(3.2)}")
    print(f"Floor of 3.8: {math.floor(3.8)}")
    print(f"Power (2^5): {math.pow(2, 5)}")
    print(f"Logarithm (log(100)): {math.log(100)}")
    print(f"Logarithm base 10 (log10(1000)): {math.log10(1000)}")
    print(f"Exponential (e^3): {math.exp(3)}")

def trigonometric_functions():
    #Demonstrates trigonometric functions in math module.#
    angle_deg = 30
    angle_rad = math.radians(angle_deg)

    print(f"\nSine of {angle_deg}°: {math.sin(angle_rad)}")
    print(f"Cosine of {angle_deg}°: {math.cos(angle_rad)}")
    print(f"Tangent of {angle_deg}°: {math.tan(angle_rad)}")
    print(f"Arcsine of 0.5 (in degrees): {math.degrees(math.asin(0.5))}")
    print(f"Arccosine of 0.5 (in degrees): {math.degrees(math.acos(0.5))}")
    print(f"Arctangent of 1 (in degrees): {math.degrees(math.atan(1))}")

def constants():
    #Displays mathematical constants.#
    print(f"\nPi (π): {math.pi}")
    print(f"Euler's Number (e): {math.e}")
    print(f"Golden Ratio (φ): {math.tau / 2}")

if __name__ == "__main__":
    print("\nStarting math Module Demonstration...\n")
    
    # Basic Math Operations
    basic_operations()
    
    # Advanced Math Functions
    advanced_math_functions()
    
    # Trigonometric Functions
    trigonometric_functions()
    
    # Mathematical Constants
    constants()
    
    print("\nmath Module Demonstration Completed.")
 

"""
