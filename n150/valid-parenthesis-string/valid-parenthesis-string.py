# https://leetcode.com/problems/valid-parenthesis-string

'''
Key Insight:
    - At first I tried to just use counters for the number of ')' and '*'
      characters
    - However, this can lead to erroneous answers where you use
      superflous leading asterix's to balance open parenthesis which
      come after the asterix's which does not work
    - I then tried to set `n_asterix = 0` whenever a new open
      parenthesis was encountered, but this fails strings like
      '***(()'
    - The insight is you need to use stacks instead of counters for the
      open parenthesis and the asterices, stacking up the character's
      index.
      You loop over all the characters, checking that each close parenthesis
      can balance with an opener
    - At the end, you then start popping from `st_open` and `st_asterix`,
      so long as the open index is less than the asterix index
    - The terminal condition is that the number of open parenthesis goes
      to zero, i.e. the stack is exhausted
'''

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st_open = []
        st_asterix = []

        # loop over chars, stacking up open parathesis and asterix,
        # and balancing them with all close parathesis
        for i, ch in enumerate(s):
            if ch == ')':
                if len(st_open) > 0:
                    st_open.pop()
                elif len(st_asterix) > 0:
                    st_asterix.pop()
                else:
                    return False
            elif ch == '(':
                st_open.append(i)
            elif ch == '*':
                st_asterix.append(i)

        # try to balance any remaining unclosed openers, making sure the
        # opener index is lower that the asterix index
        while (
                len(st_open) > 0
                and len(st_asterix) > 0
                and st_asterix[-1] > st_open[-1]
        ):
            st_open.pop()
            st_asterix.pop()

        return len(st_open) == 0

        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
        ("(", False), 
        ("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())", False),
        ("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()", True),
        ("(**()", True),
        ("***(()", False),
    ]
    for (s, solution) in tests:
        result = sol.checkValidString(s)
        assert result == solution, \
            f"result {result} != solution {solution}, s={s}"
    print("✅ All tests passed")

