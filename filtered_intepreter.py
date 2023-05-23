# Old HyperBF

out_list = list()

def filtered_intepreter(code, targettext, inputrequired=False):
    """
    >   Increment the pointer.
    <   Decrement the pointer.
    +   Increment the byte at the pointer.
    -   Decrement the byte at the pointer.
    .   Output the byte at the pointer.
    ,   Input a byte and store it in the byte at the pointer.
    [   Jump forward past the matching ] if the byte at the pointer is zero.
    ]   Jump backward to the matching [ unless the byte at the pointer is zero.
    -----------------------------------------------------------------------------
    ^   Increment the second pointer.
    v   Decrement the second pointer.
    '   Increment the byte at the second pointer.
    ;   Decrement the byte at the second pointer.
    *   Output the byte at the second pointer.
    ~   Swap the first and second pointer's bytes.
    -----------------------------------------------------------------------------
    }   Increment the third pointer.
    {   Decrement the third pointer.
    `   Increment the byte at the third pointer.
    _   Decrement the byte at the third pointer.
    @   Output the byte at the third pointer.
    |   Swap the second and third pointer's bytes.
    /   Swap the third and first pointer's bytes.
    -----------------------------------------------------------------------------
    :   (byte at the pointer <-> SB_1) and (byte at the third pointer <-> SB_2).
    =   (SB_1 <-> SB_2).
    !   (SB_1 != SB_2) then (byte at the second pointer <-> SB_1).
    $   (SB_1 != SB_2) then (byte at the second pointer <-> SB_2).
    #   (SB_1 == SB_2) then (SB_1 -> SB_2 -> byte at the second pointer -> SB_1).
    %   (SB_1 == SB_2) then (SB_1 -> byte at the second pointer -> SB_2 -> SB_1).
    -----------------------------------------------------------------------------
    (   Jump forward past the matching ) if the byte at the pointer is equal to SB_1.
    )   Jump backward to the matching ( unless the byte at the pointer is equal to SB_1.
    -----------------------------------------------------------------------------
                                           END
    """
    if not ("." in code):
        return 0, None

    ttl = len(targettext)

    # print(code)

    fitness = 0
    array = [0]
    second_array = [0]
    third_array = [0]

    sb_1 = 0
    sb_2 = 0

    pointerLocation = 0
    second_pointerLocation = 0
    third_pointerLocation = 0
    i = 0
    # _iter_ = 0
    passesWithoutPrinting = 0
    output = str()
    # print(f"Running brainf*ck program read as: {code}")
    # print(array[pointerLocation], code[i])
    while i < len(code):
        if code[i] == '<':
            if pointerLocation > 0:
                pointerLocation -= 1
        elif code[i] == '>':
            pointerLocation += 1
            if len(array) <= pointerLocation:
                array.append(0)
        elif code[i] == '+':
            array[pointerLocation] += 1
            if array[pointerLocation] > 255:
                array[pointerLocation] = 0
        elif code[i] == '-':
            array[pointerLocation] -= 1
            if array[pointerLocation] < 0:
                array[pointerLocation] = 255
        elif code[i] == '.':
            output += chr(array[pointerLocation])
            passesWithoutPrinting = 0
        elif code[i] == ',':
            if inputrequired:
                x = ord(input("Input: "))
                array[pointerLocation] = x
            else:
                return 0, None
        elif code[i] == '[':
            if array[pointerLocation] == 0:
                try:
                    while code[i] != ']':
                        i += 1
                except IndexError:
                    return 0, None
        elif code[i] == ']':
            if array[pointerLocation] != 0:
                try:
                    while code[i] != '[':
                        i -= 1
                except IndexError:
                    return 0, None
        elif code[i] == '^':
            second_pointerLocation += 1
            if len(second_array) <= second_pointerLocation:
                second_array.append(0)
        elif code[i] == 'v':
            if second_pointerLocation > 0:
                second_pointerLocation -= 1
        elif code[i] == '\'':
            second_array[second_pointerLocation] += 1
            if second_array[second_pointerLocation] > 255:
                second_array[second_pointerLocation] = 0
        elif code[i] == ';':
            second_array[second_pointerLocation] -= 1
            if second_array[second_pointerLocation] < 0:
                second_array[second_pointerLocation] = 255
        elif code[i] == '*':
            output += chr(second_array[second_pointerLocation])
            passesWithoutPrinting = 0
        elif code[i] == '~':
            x = array[pointerLocation]
            y = second_array[second_pointerLocation]
            array[pointerLocation] = y
            second_array[second_pointerLocation] = x
        elif code[i] == '}':
            third_pointerLocation += 1
            if len(third_array) <= third_pointerLocation:
                third_array.append(0)
        elif code[i] == '{':
            if third_pointerLocation > 0:
                third_pointerLocation -= 1
        elif code[i] == '`':
            third_array[third_pointerLocation] += 1
            if third_array[third_pointerLocation] > 255:
                third_array[third_pointerLocation] = 0
        elif code[i] == '_':
            third_array[third_pointerLocation] -= 1
            if third_array[third_pointerLocation] < 0:
                third_array[third_pointerLocation] = 255
        elif code[i] == '@':
            output += chr(third_array[third_pointerLocation])
            passesWithoutPrinting = 0
        elif code[i] == '|':
            x = second_array[second_pointerLocation]
            y = third_array[third_pointerLocation]
            second_array[second_pointerLocation] = y
            third_array[third_pointerLocation] = x
        elif code[i] == '/':
            x = third_array[third_pointerLocation]
            y = array[pointerLocation]
            third_array[third_pointerLocation] = y
            array[pointerLocation] = x
        elif code[i] == ':':
            x = sb_1
            y = array[pointerLocation]
            sb_1 = y
            array[pointerLocation] = x
            x = sb_2
            y = third_array[third_pointerLocation]
            sb_2 = y
            third_array[third_pointerLocation] = x
        elif code[i] == '=':
            x = sb_1
            y = sb_2
            sb_1 = y
            sb_2 = x
        elif (code[i] == '!') and (sb_1 != sb_2):
            x = sb_1
            y = second_array[second_pointerLocation]
            sb_1 = y
            second_array[second_pointerLocation] = x
        elif (code[i] == '$') and (sb_1 != sb_2):
            x = sb_2
            y = second_array[second_pointerLocation]
            sb_2 = y
            second_array[second_pointerLocation] = x
        elif (code[i] == '#') and (sb_1 == sb_2):
            x = sb_1
            y = sb_2
            z = second_array[second_pointerLocation]
            sb_2 = x
            second_array[second_pointerLocation] = y
            sb_1 = z
        elif (code[i] == '%') and (sb_1 == sb_2):
            x = sb_1
            y = sb_2
            z = second_array[second_pointerLocation]
            second_array[second_pointerLocation] = x
            sb_2 = z
            sb_1 = y
        elif code[i] == '(':
            if array[pointerLocation] == sb_1:
                try:
                    while code[i] != ')':
                        i += 1
                except IndexError:
                    return 0, None
        elif code[i] == ')':
            if array[pointerLocation] != sb_2:
                try:
                    while code[i] != '(':
                        i -= 1
                except IndexError:
                    return 0, None

        
        if passesWithoutPrinting > 5000:
            return 0, None
        elif len(output) >= ttl:
            break
        
        passesWithoutPrinting += 1
        i += 1
        #_iter_ += 1
        #print(passesWithoutPrinting, i, array, output, _iter_)

    if len(output) < ttl:
        return 0, None
    else:
        for i in range(ttl):
            fitness += 256 - abs(ord(output[i]) - ord(targettext[i]))

    return fitness, output