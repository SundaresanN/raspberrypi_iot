text ="we're going to save this line in a text file"

save= open('example.txt','w')
save.write(text)
save.close()
