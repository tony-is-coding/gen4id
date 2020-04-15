# MIT License
#
# Copyright (c) 2020 tonyiscoding
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

######################################
#
#  a simple id generator for increase id ,  eg: mysql auto id
#
# ##############################

DIGITAL = "1234567890"
ALPHABETIC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
MIXED = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class IncreaseGen:
    def __init__(self, key_len: int, choose: str = MIXED, digit: bool = False, digit_bit: int = 2):
        self._choose = choose
        self._key_len = key_len
        self._digit = digit
        self._digit_bit = digit_bit
        if key_len <= digit_bit * 2:
            raise ValueError("ken len must double bigger then digit bit")

        self._code: str = ""

    def encode(self, increase_id: int) -> str:
        str_len = len(self._choose)
        ken_len = self._key_len - self._digit_bit
        for _ in range(ken_len):
            tmp_index = increase_id % str_len
            increase_id = increase_id // str_len
            self._code = "{}{}".format(self._choose[tmp_index], self._code)
        if not self._digit:
            self.digit()
        return self._code

    def decode(self):
        pass

    @classmethod
    def __digit(cls, s_code: str) -> str:
        """
        add the digit check bit
        :return:
        """
        i = 1
        tmp_sum = 0
        for num in s_code:  # number 为0-9
            if 0 == i % 2:
                tmp = int(ord(num)) * 2 % 10  # tmp 这种
            else:
                tmp = int(ord(num)) * 3 % 10
            tmp_sum += tmp
            i += 2
        if 0 == tmp_sum % 10:
            bit = 0
        elif tmp_sum > 100:
            bit = 10 - tmp_sum % 100 % 10
        else:
            bit = 10 - tmp_sum % 10
        return str(bit)

    @classmethod
    def __str_ins(cls, s: str, ins: str, index: int) -> str:
        """ insert a char into a immutable string
            index start of 0
        """
        return s[:index] + ins + s[index:]

    def digit(self) -> str:
        for i in range(self._digit_bit):
            self._code += self.__digit(self._code)
        return self._code

