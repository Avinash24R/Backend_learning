
def number_words(text:str):
    return len(text.split())

def get_char_freq(text:str) -> dict[str , int]:
    freq = {}
    for char in text.lower():
        freq[char] = freq.get(char , 0) + 1
    return freq
def sort_on(item):
    return item["num"]
def report_list(freq: dict):
    freq_list = []
    for key , val in freq.items():
        freq_list.append({"char":key, "num":val})
    freq_list.sort(reverse=True , key=sort_on)
    return freq_list

 