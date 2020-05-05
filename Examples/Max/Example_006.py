s = "jfsPOIKF\nwigWJGOIJWGoi\n10=103\n"
i = s.rfind("\n", 0, s.rfind("\n"))
s = s[i:]
s = s[0:s.find("=")]
print s
