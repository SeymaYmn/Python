# i is length of string1
# j is length of string2

def edit_distance(string1,string2,i,j ):
    if i==0:
        return j
    if j==0:
        return i

    if string1[i-1] == string2[j-1]:
        cost = 0
    else:
        cost = 1

    return  min((edit_distance(string1,string2,i-1,j-1)+cost),
                (edit_distance(string1,string2,i,j-1)+1),
                (edit_distance(string1,string2,i,j-1)+1))


def longest_common_substring(string1,string2,i,j):
    if i==0:
        return j
    if j==0:
        return i

    if string1[i-1] == string2[j-1]:
        cost=1
    else:
        cost=0

    return (longest_common_substring(string1,string2,i-1,j-1)+cost)


def longest_common_subsequence(string1,string2,i,j):
    if i==0:
        return j
    if j==0:
        return i
    
    if string1[i-1] == string2[j-1]:
        return longest_common_subsequence(string1,string2,i-1,j-1)
    else:
        return max(longest_common_subsequence(string1,string2,i-1,j),
                   longest_common_subsequence(string1,string2,i,j-1))




string1="kitten"
string2="sitting"
print edit_distance(string1,string2,len(string1),len(string2))
print longest_common_substring(string1,string2,len(string1),len(string2))
print longest_common_subsequence(string1,string2,len(string1),len(string2))









