import sys
if len(sys.argv) == 2 and int(sys.argv[1]) < int(101) and int(sys.argv[1])%3 == 0 and int(sys.argv[1])%5 == 0:
        print("fizzbuzz")
        
elif len(sys.argv) == 2 and int(sys.argv[1]) < int(101) and int(sys.argv[1])%3 == 0:
    print("fizz")
    
elif len(sys.argv) == 2 and int(sys.argv[1]) < int(101) and int(sys.argv[1])%5 == 0:
        print("buzz")
        
elif len(sys.argv) == 2 and int(sys.argv[1]) < int(101):
        print(sys.argv[1])    
    
elif len(sys.argv) < 2:
    my_input = raw_input("Please insert a number to proceed")
    print my_input
    
elif len(sys.argv) > 2:
    my_input = raw_input("Please insert only one number at a time")
    print my_input

else:
    my_input2 = raw_input("Please insert a number between only between 1-100")
    print my_input2
    


    