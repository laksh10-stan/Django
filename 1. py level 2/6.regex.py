import re
# patterns = ['term1', 'term2']
# text = "this has term1"
# for pattern in patterns:
#     print("I'm searching for:" +pattern)
#     if re.search(pattern, text):
#         print("MATCH")
#     else:
#         print("NO MATCH")
# print(re.search('term1', text).start())
# print(type(re.search('term1', text)))

# split_term = "@"
# email = "laksh@gmail.com"
# print(re.split(split_term, email))

#print(re.findall('match', 'test a phrase match in match middle'))
# def multi_re_find(patterns, phrase):
#     for pat in patterns:
#         print("Searching for pattern {}".format(pat))
#         print(re.findall(pat, phrase))
#         print('\n')
# test_phrase = "sdsd..sssddd..sdddsdd...dsds...dssssss...sddddd"
# #test_patterns = ['sd*']    #0 or more
# # test_patterns = ['sd+']     #1 or more
# # test_patterns = ['sd?']     # 0 or 1
# # test_patterns = ['sd{2}']
# #test_patterns = ['sd{1,3}']
# test_patterns = ['s[sd]+']
#
#
# multi_re_find(test_patterns, test_phrase )


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')
test_phrase = "This is a string! But it has 45 punctuation. How can 1 we remove it?"

test_patterns = ['[^!.?]+']
test_patterns = ['[a-z]+']
test_patterns = ['[A-Z]+']
test_patterns = [r'\d+']
test_patterns = [r'\D+']
test_patterns = [r'\s+']
test_patterns = [r'\S+']
test_patterns = [r'\w+']
test_patterns = [r'\W+']




multi_re_find(test_patterns, test_phrase )
