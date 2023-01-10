class Solution:
  def isNumber(self, s: str) -> bool:
    s = s.strip()
    if not s:
      return False

    foundNum = False
    foundDot = False
    foundE = False

    for i, c in enumerate(s):
      if c == '.':
        if foundDot or foundE:
          return False
        foundDot = True
      elif c.lower() == 'e':
        if foundE or not foundNum:
          return False
        foundE = True
        foundNum = False
      elif c in '+-':
        if i > 0 and s[i - 1] != 'e':
          return False
        foundNum = False
      else:
        if not c.isdigit():
          return False
        foundNum = True

    return foundNum
