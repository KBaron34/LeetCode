def canConstruct(ransomNote: str, magazine: str) -> bool:
    sransomNote = sorted(ransomNote)
    smagazine = sorted(magazine)
    i = 0
    j = 0
    count = 0
    while i < len(sransomNote) and j < len(smagazine):
        if sransomNote[i] == smagazine[j]:
            i += 1
            j += 1
            count += 1
        else:
            while j < len(smagazine):
                if sransomNote[i] == smagazine[j]:
                    j += 1
                    i += 1
                    count += 1
                    break
                else:
                    j += 1

    if count == len(sransomNote):
        return True
    else:
        return False

