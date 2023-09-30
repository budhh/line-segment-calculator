def import_function(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)

# Ask the user which function they want to use
choice = \
    input(" \
1 for 2D \n \
2 for 2D Functions \n \
3 for 3D \n \
4 for 3D Functions \n \
Enter Here: ")

if choice == '1':
    function = import_function('2d', 'func')
    print("\nYou have chosen Option 1: 2D\n")
elif choice == '2':
    function = import_function('2dfunctions', 'func')
    print("\nYou have chosen Option 2: 2D Functions\n")
elif choice == '3':
    function = import_function('3d', 'func')
    print("\nYou have chosen Option 3: 3D\n")
elif choice == '4':
    function = import_function('3dfunctions', 'func')
    print("\nYou have chosen Option 4: 3D Functions\n")
else:
    print("Invalid choice.")
    exit()

function()
