"""
Programmer  :   EOF
Date        :   2015.04.10
File        :   itr.py
E-mail      :   jasonleaster@gmail.com
"""

"""
Varible Description:

    @ret_string :   We put the returning string into this varible
    @base       :   Here is the base number for Roman counting process
    @table      :   We could use the base number to index the corresponding
                    representation in Roman Numbers
    @base_len   :   The length of @base
    @counter    :   A copy of @base_len
    @index      :   The current base number.

"""
class Solution:

    def intToRoman(self, num):

        ret_string = "" 

        base  = [1, 5, 10, 50, 100, 500, 1000]

        table = {1 :"I", 5  :"V", 10 :"X", \
                50:"L", 100:"C", 500:"D", 1000:"M"}

        base_len = len(base)
        counter  = base_len
        while counter > 0:
            
            index = base[counter-1]
            tmp = num / index

            while tmp > 0:
                if self.hight_bit(num) == 9:
                    counter -= 1
                    index = base[counter - 1]
                    ret_string += table[ base[counter - 1]    ] +\
                                  table[ base[counter + 1]]
                    break;

                elif self.hight_bit(num) == 4:
                    index = base[counter - 1]
                    ret_string += table[ base[counter - 1]    ] +\
                                  table[ base[counter    ]    ]
                    break;

                else:
                    ret_string += table[index]
                    tmp -= 1;

            num  %= index
            counter -= 1

        return ret_string

    # We use this function to get the hightest bit in num conveniently :)
    def hight_bit(self, num):
        tmp = num
        while tmp > 10:
            tmp /= 10

        return  tmp
            

#----------- just for testing -----------------

s = Solution()

number = 4
print s.intToRoman(number)

number = 18
print s.intToRoman(number)

number = 3999
print s.intToRoman(number)

number = 1600
print s.intToRoman(number)

number = 321
print s.intToRoman(number)

number = 400
print s.intToRoman(number)
