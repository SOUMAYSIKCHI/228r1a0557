file_name = input("Enter file name: ")
num_lines = 0
num_chars = 0
unique_words = set()
try:
    fp=open(file_name,"r")
    for i in fp:
        words = i.split()
        num_lines += 1
        unique_words.update(words)
        num_chars += len(i)
    print("Lines = ",num_lines)
    print("Words = ",len(unique_words))
    print("Characters = ",num_chars)
    fp.close()
except Exception:
    print("Enter valid filename")

'''
content in count.txt=
hell how are you
how are u
i am fine
'''
'''output :
Enter file name: count.txt
Lines =  3
Words =  8
Characters =  364

'''