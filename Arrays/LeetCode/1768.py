# SOL. 1 - > Two pointers

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1, word2=list(word1),list(word2)
        i,j=0,0
        result=[]
        while i<len(word1) and j<len(word2):
            result+=[word1[i],word2[j]]
            i,j=i+1,j+1
        if len(word1)>i:
            result+=word1[i:]
        elif len(word2)>j:
            result+=word2[j:]
        return(''.join(result))
    
    
# SOL. 2 - > ONE-LINER

word1 = "abcd"
word2 = "pq"
print("".join(a + b for a, b in zip(word1, word2))+word1[len(word2):]+word2[len(word1):])

# SOL. 3 
merged_string = []
for i in range(min(len(word1), len(word2))):
  merged_string.extend([word1[i], word2[i]])
merged_string.extend(word1[i+1:] if len(word1) > len(word2) else word2[i+1:])
print(''.join(merged_string))