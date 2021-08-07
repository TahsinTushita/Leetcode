class Solution:
    def plusOne(self, digits) -> int:
        strDigitList = [str(digit) for digit in digits]
        strDigits = "".join(strDigitList)
        intDigits = int(strDigits)
        intDigits += 1
        strDigits = str(intDigits)
        digits = [int(digit) for digit in strDigits]

        return digits

if __name__ == '__main__':
    s1 = Solution()
    print(s1.plusOne([1,2,3]))