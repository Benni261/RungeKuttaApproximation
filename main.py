import sys

match sys.argv[1]:
    case "1":
        from equation1 import execute
    case "2":
        from equation2 import execute
    case "3":
        from equation3 import execute
    case _:
        raise ValueError("Invalid argument. Use 1, 2, or 3.")
    
# print(sys.argv)
execute(step_size=float(sys.argv[2]), x_stoppper=float(sys.argv[3]))