# Subarrays with equal 1s and 0s

# Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.

array = [ 1 , 0 , 0 , 1 , 0 ,  1 , 1 ]
ans = []

for interval_length in range ( 0 , len ( array ) ) :
    
    for index in range ( 0 , len ( array ) - interval_length ) :
        
        temp = array [ index : index + interval_length + 1 ]
        count_0 = temp .count ( 0 )
        count_1 = temp .count ( 1 )
        
        if count_0 == count_1 : 
            interval = [ index , index + interval_length ]
            ans .append ( interval )

print ( ans )