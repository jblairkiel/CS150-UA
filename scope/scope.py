def statistics(a,b,c,d,e):
    def mean():
        
        return (a+b+c+d+e)/5

    def boundary(end):
        
        def minimum():
            if (a<b and a<c and a<d and a<e):
                return a
            elif (b<c and b<d and b<e):
                return b
            elif (c<d and c<e):
                return c
            elif(d<e):
                return d
            else:
                return e

        def maximum():
            if (a>b and a>c and a>d and a>e):
                return a
            elif (b>c and b>d and b>e):
                return b
            elif (c>d and c>e):
                return c
            elif (d>e):
                return d
            else:
                return e

            if (end == 'lower'):
                return minimum()
            elif (end == 'upper'):
                return maximum()
            else:
                return 'Error'

        def helper():
            print("The mean is:", mean())
            print("The lower bound is:", boundary('lower'))
            print("The upper bound is:", boundary('upper'))

        helper()


nums = eval(input("Enter in 5 numbers using array notation: "))
statistics(nums[0], nums[1], nums[2], nums [3], nums[4])
