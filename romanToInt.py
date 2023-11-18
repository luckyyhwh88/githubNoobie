class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        m = s.rfind("M")
        m_string = s[0:m+1]
        temp = s[m+1:]
        if m_string.find("C") != -1 :
            number += 1000*(len(m_string)-1)-100
        else :
            number +=1000*len(m_string)

        d = temp.rfind("D")
        d_string = temp[0:d+1]
        temp = temp[d+1:]
        if d_string.find("C") != -1 :
            number += 500*(len(d_string)-1)-100
        else :
            number +=500*len(d_string)

        c = temp.rfind("C")
        c_string = temp[0:c+1]
        temp = temp[c+1:]
        if c_string.find("X") != -1 :
            number += 100*(len(c_string)-1)-10
        else :
            number +=100*len(c_string)

        l = temp.rfind("L")
        l_string = temp[0:l+1]
        temp = temp[l+1:]
        if l_string.find("X") != -1 :
            number += 50*(len(l_string)-1)-10
        else :
            number +=50*len(l_string)


        x = temp.rfind("X")
        x_string = temp[0:x+1]
        temp = temp[x+1:]
        if x_string.find("I") != -1 :
            number += 10*(len(x_string)-1)-1
        else :
            number +=10*len(x_string)

        v = temp.rfind("V")
        v_string = temp[0:v+1]
        temp = temp[v+1:]
        if v_string.find("I") != -1 :
            number += 5*(len(v_string)-1)-1
        else :
            number +=5*len(v_string)

        number += len(temp)
        
        return number