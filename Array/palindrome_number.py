class Solution:
    def isPalindrome(self, x: int) -> bool:
        # palindrome can not ever be negative number
        if x < 0:
            return False
        
        number_string = str(x)

        reversed_string = number_string[::-1]

        return number_string == reversed_string
            

if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome(121))
