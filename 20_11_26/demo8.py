f = open('F:\\record.txt')

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] != "======":
        (role,line_spoken) = each_line.split(':',1)
        if role == 'xiaojiayu':
            boy.append(line_spoken)
        else:
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy' + str(count) + '.txt'
        file_name_girl = 'girl' + str(count) + '.txt'

        boy_file = open("F:\\"+file_name_boy,'w')
        girl_file = open("F:\\"+file_name_girl,'w')
        print("1")
        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

f.close()
