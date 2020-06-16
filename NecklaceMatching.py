#https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/
def same_necklace(string1, string2):
      global result
        result = False
          if (len(string1) != len(string2) ):
                  print(False)
                      return None
                    if (len(string1) == 0):
                            print(True)
                                return None
                              list2 = list(string2)
                                char1 = list2[0]
                                  for i in range(len(string1)):
                                          list2 = list(string2)
                                              char1 = list2.pop()
                                                  string2 = char1 + ''.join(list2)
                                                      #print(string2)
                                                          if (string1 == string2):
                                                                    result = True
                                                                      print(result)
                                                                      same_necklace("nicole", "icolen")
                                                                      same_necklace("nicole", "lenico")
                                                                      same_necklace("nicole", "coneli") 
                                                                      same_necklace("aabaaaaabaab", "aabaabaabaaa")
                                                                      same_necklace("abc", "cba")
                                                                      same_necklace("xxyyy", "xxxyy")
                                                                      same_necklace("xyxxz", "xxyxz")
                                                                      same_necklace("x", "x")
                                                                      same_necklace("x", "xx")
                                                                      same_necklace("x", "")
                                                                      same_necklace("", "")
