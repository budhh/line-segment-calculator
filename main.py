

def import_function(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)

# Ask the user which function they want to use
choice = input("Enter 1 for 2D or 2 for 3D or 3 for 3D Functions: ")

if choice == '1':
    function = import_function('2d', 'func2d')
elif choice == '2':
    function = import_function('3d', 'func3d')
elif choice == '3':
    function = import_function('3dfunctions', 'func3d')
else:
    print("Invalid choice. Please enter 1 or 2.")
    exit()

# Call the chosen function
function()
