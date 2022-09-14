def same_necklace(necklace1, necklace2):
  if (len(necklace1) != len(necklace2)):
    return False
  if (necklace1 == necklace2):
    return True

  for s in necklace1:
    # move last character to the front
    necklace2 = necklace2[-1] + necklace2[:-1]
    if (necklace1 == necklace2):
      return True

  return False

print(same_necklace("nicole", "icolen"))
print(same_necklace("nicole", "lenico"))
print(same_necklace("nicole", "coneli"))
print(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
print(same_necklace("abc", "cba"))
print(same_necklace("xxyyy", "xxxyy"))
print(same_necklace("xyxxz", "xxyxz"))
print(same_necklace("x", "x"))
print(same_necklace("x", "xx"))
print(same_necklace("x", ""))
print(same_necklace("", ""))
