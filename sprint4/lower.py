def letter_count(string):
    index = 0
    counter = 0
    res=[]
    while index<len(string):
        if string[index] in res:
            res = res[res.index(string[index])+1:]
        if string[index] not in res:
            res.append(string[index])
            if len(res)>counter:
                counter=len(res)
        index+=1
    return counter


print(letter_count('abcabcbb'))
print(letter_count('fprarfpoz'))    
print(letter_count('vdoejgvnubksokvsjlxtqqptanegzlzxbzckzrczhjvxybfgkkbdbqzaiceubawpkkdxisvbhzbvtklemyrdalboelmtywujlztbeehkyprhwxugzhkisqvumdiclysvdxvfcgkmvpdsjeodzzxephrlbhrnyomhbldmvhwhvtciiahdqllcqhdeumgluqjkcgcdksvpypdlvwbzsoeeqvpnaxauljtnimbzoxtzobcftclunuhogukkstqrmehpwiogkpmcijakbzgrgfbnjemkcqotguldyzafrefygakxfjqpsyhidqhfkgslbjtdljkhykybjegpnzngaaxpmloseotledyowkbxfzdbrfyccwelvatdqbqjkynnotwzujfjydvtxoskalenehehmgztlauvsnlohghswkmjegrvlnyleaecmfjbtlmbqhgnhztpgirpszqrsnsqljfxqhadaqujpzwgysxzyksmsmwbjffywsbzktxqwgkauivppgmisomniajxmwgjnfhhelbsrhmwuzkdmtahzzsvlxnbvsmmzagieriaemfjxfkipwncfzvmznnehdxgguufspidpviokmmsaywhbxkcbuvjcwnetxgmbaslkbchnmgxgzilpamyourrgpdwdeqcqioipvypmtaojbmebyfqgxkxaoaqrqybzkybhmxrcbjagamdfouaunbupctksmqjzekblegrwqtrusiqbusqabljerkahkyajwuflruxxtspeeqkqijbhppeinlsgfrotudhhtkcglxnmowyebhgsxfbwrrmhpvxvasispoljjauytpauerxirlzifofyaenoeqcrvnkihiojsxfjlmrwevfxmeukjxkpigrzxfqsnexxzokfzgviveltmdbusdvdryazfgzvhvwxucofojfkdmjdzeqchvripidnowbummaiiempkpvojenpkbtongrpscisrnhvibhdvdeueirecqvhvzbdxhrqpg'))    

