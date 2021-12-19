def Convert (decimal_number, base_to_convert):
    
    numDec = decimal_number
    base = base_to_convert
    
    #Base em 2
    if (base == "Bin" or base == 2):
        numBin = [5]
        del numBin[0]
        
        if (numDec == 0):
            return "null"

        while (numDec > 1):
            numBin.append(numDec % 2)
            numDec = int(numDec / 2)
                    
            if numDec <= 1:
                numBin.append(numDec)
             
        i = len(numBin) - 1
        result = ""
        while (i != -1):
            result = result + str(numBin[i])
            i = i - 1
        
        return int(result)
    
    #Base em 8
    elif (base == "Oct" or base == 8):
        numOct = [5]
        del numOct[0]
        
        if (numDec == 0):
            return 0

        while (numDec > 1):
            numOct.append(numDec % 8)
            numDec = int(numDec / 8)
                    
            if numDec <= 1:
                numOct.append(numDec)
             
        i = len(numOct) - 1
        result = ""
        while (i != -1):
            result = result + str(numOct[i])
            i = i - 1
        
        return int(result)

    #Base em 16
    elif (base == "Hex" or base == 16):
        numHex = [5]
        del numHex[0]
        
        if (numDec == 0):
            return 0

        while (numDec > 1):
            if ((numDec %  16) == 10):
                numHex.append("A")
            elif ((numDec %  16) == 11):
                numHex.append("B")
            elif ((numDec %  16) == 12):
                numHex.append("C")
            elif ((numDec %  16) == 13):
                numHex.append("D")
            elif ((numDec %  16) == 14):
                numHex.append("E")
            elif ((numDec %  16) == 15):
                numHex.append("F")
            else:
                numHex.append(numDec % 16)
                
            numDec = int(numDec / 16)

            if numDec <= 1:
                numHex.append(numDec)
             
        i = len(numHex) - 1
        result = ""
        while (i != -1):
            result = result + str(numHex[i])
            i = i - 1
        
        return result

    #ERROR
    else:
        return "base_to_convert: invalid"
