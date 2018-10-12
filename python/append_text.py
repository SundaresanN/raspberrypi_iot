text = "lets append this line to previous example.txt\n"
save = open('example.txt','a')
save.write('\n')
save.write(text)
save.close()
