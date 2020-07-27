def solution(s):
    i = (s+s).find(s, 1, -1)
    if (len(s) % 2 != 0):
            if(len(set(s)) == 1):
                return(str(len(s)))
                
            else:
                s = s[:-1]
                if len(set(s)) == 1:
                    return(str(len(s)))
                    
                elif i == -1:
                    sub = s[0:len(set(s))]
                    return(str(s.count(sub)))
                    
                else:
                    sub = s[:i]
                    return( str(s.count(sub)))
                    
    else:
        if len(set(s)) == 1:
            return( str(len(s)))
            
        else:
            sub = s[:i]
            return(str(s.count(sub)))
        
solution("abcabcabcabc")