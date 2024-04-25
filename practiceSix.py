def avglength(sentence):
    words = sentence.split()
    
    words = [word.strip(".,:;!?") for word in words]
    
    word_lengths = [len(word) for word in words]
    
    if len(word_lengths) > 0:
        avg_length = sum(word_lengths) / len(word_lengths)
        return avg_length
    else:
        return 0

sentence = "This is a sample sentence, showing how to calculate the average length of words."
avg = avglength(sentence)
print("میانگین طول کلمات:", avg)
