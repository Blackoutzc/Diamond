# -*- coding:utf-8 -*-
"""
Interview Coding practice
Description:
The job is to construct a diamond , as below:
  *
 * *
* * *
 * *
  *
"""
import os


class Diamond(object):
    def __init__(self, pattern='*', char_num=10):
        """pattern should be a single char, like * or +
           char_num should be greater than 1
             1       *
             2      * *      pattern = "*"
             3     * * *     char_num = 3
             4      * *
             5       *
           :param pattern optional single char used to fill a diamond, above pattern = "*"
           :type pattern str or unicode
           :param char_num optional number of the maximum patterns within a single line
           :type char_num int (should be greater than 1)
        """
        self._pattern = Diamond.get_pattern(pattern)
        self._char_num = Diamond.get_char_num(char_num)
        self._lines_instance = None
        self._construct_lines()

    @staticmethod
    def get_pattern(pattern):
        """If pattern is a single char, return it else return *"""
        if isinstance(pattern, (str, unicode)) and len(pattern) == 1:
            return pattern
        else:
            return '*'

    @staticmethod
    def get_char_num(char_num):
        """Make sure char num is greater than 1, if not, return 20 by default"""
        if isinstance(char_num, int) and char_num > 2:
            return char_num
        else:
            return 20

    class Lines(object):
        """
        Lines class is a container, which includes a list to record every line,
        we can get every single line by index reference, index started by 1 not 0
        we can also use for loop to get line sequentially
        lines_string property is a convenient way to get the whole diamond string
        The following example illustrates every instance variable
             1       *          _base_num = 3
             2      * *         _line_nums = 5
             3     * * *        _single_char = '* '
             4      * *         _lines = ['  *  ',' * * ','* * *',' * * ','  *  ']
             5       *          middle_line_num = 3
        """
        def __init__(self, single_char, num):
            self._base_num = Diamond.get_char_num(num)
            self._line_nums = 2*self._base_num - 1
            self._single_char = Diamond.get_pattern(single_char) + ' '
            self._lines = []
            self._construct()

        def _construct(self):
            middle_line_num = self._base_num
            for i in xrange(1, self._line_nums+1):
                if i > middle_line_num:
                    i = self._line_nums - i + 1
                self._lines.append(((self._single_char*i).center(self._line_nums+1))[:-1])

        @property
        def lines_string(self):
            return os.linesep.join(self._lines)

        def __iter__(self):
            return iter(self._lines)

        def __getitem__(self, item):
            if isinstance(item, int) and (1 <= item <= self._line_nums):
                return self._lines[item - 1]
            else:
                return None

    def _construct_lines(self):
        self._lines_instance = Diamond.Lines(self._pattern, self._char_num)

    def print_lines(self):
        if isinstance(self._lines_instance, Diamond.Lines):
            print self._lines_instance.lines_string
            """
            #becasue an instance of Diamond.Lines is Iterable, we can do this
            for line in self._lines_instance:
                print line
            """


if __name__ == "__main__":
    d = Diamond(char_num=3, pattern="*")
    d.print_lines()
