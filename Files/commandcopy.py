from sys import argv

if len(argv) == 3:
    try:
        fp1 = open(argv[1], "r")
        fp2 = open(argv[2], "w+")
        for i in fp1:
            fp2.write(i)
        print("File is copied successfully")
        fp2.seek(0, 0)
        content = fp2.read()
        print(content)

    except Exception:
        print("Error occurred while copying the file")

else:
    print("Usage: python script.py source_file destination_file")

# python commandcopy.py csa.text mech.text
