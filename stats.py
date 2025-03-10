def get_num_words(text):
    words = text.split()
    return len(words)

def convert_lower(text):
    lowercase = text.lower()
    countlower = {}
    list1=lowercase
    for l in list1:
        if l in countlower:
            countlower[l] += 1
        else:
            countlower[l] = 1
    return(countlower)
    
#def sort_on(dict):
#    return dict["num"]
def sort_chars(char_count_dict):
    chars_list = []
    for char, count in char_count_dict.items():
        chars_list.append({"char": char, "count": count})
        
    def sort_on(dict):
        return dict["count"]  # We want to sort by the count value
    
    # Now we need to sort this list...
    chars_list.sort(reverse=True, key=sort_on) #sorting list
    return chars_list