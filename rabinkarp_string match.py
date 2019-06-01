

# text = "FORGEEKS"
text = "AAAABCD"
pattern = "ABCD"


pattern_len = len(pattern)
text_len = len(text)

text_hash,pattern_hash = 0,0


for i in range(pattern_len):
    text_hash += ord(text[i]) * (26 ** (pattern_len-i-1))
    pattern_hash += ord(pattern[i]) * (26 ** (pattern_len-i-1))
    prev_text_hash = text_hash



for i in range(text_len-pattern_len+1):
    # print(i,text[i:i+pattern_len],text_hash)
    if(text_hash == pattern_hash):
        if(text[i:i+pattern_len] == pattern):
            print("Match at: ",i)
            break
           

   
    temp =  ord(text[i]) * (26 ** (pattern_len -1))
    text_hash = prev_text_hash - temp
    text_hash = text_hash * 26
    text_hash += ord(text[i+pattern_len])
    # print("tem",temp)
    
    
    prev_text_hash = text_hash
 