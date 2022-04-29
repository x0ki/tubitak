
nums_as_words = input(">>> ")
splitted_words = nums_as_words.split(" ")
num_dictioniry = {
    "zero" : '0',
    "one" : '1',
    "two" : '2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six": '6',
    "seven":'7',
    "eight":'8',
    "nine" :'9',
    "ten":'10',
    "eleven":'11',
    "twelve":'12',
    "thirteen":'13',
    "fourteen":'14',
    "fifteen":'15',
    "sixteen":'16',
    "seventeen":'17',
    "eighteen":'18',
    "nineteen":'19',
    "twenty":'2',
    "thirty":'3',
    "fourty":'4',
    "fifty":'5',
    "sixty":'6',
    "seventy":'7',
    "eighty":'8',
    "ninety":'9',
    "hundred":'100'
}
output = ""
for word in splitted_words:
    output += num_dictioniry.get(word,word)

first = int(output)
print(first)
print("\033[2;34;32m U just go a value error! propably u just did a mitake in the spelling!  \n")
