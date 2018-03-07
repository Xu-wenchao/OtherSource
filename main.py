import requests


with open('url.txt', 'r') as f:
    file_num = 1
    while 1:
        line = f.readline()
        if not line:
            break
        response = requests.get(line[0: line.rindex('\n')])
        fw = open('files/' + line[line.rindex('/') + 1: line.rindex('\n')], 'wb')
        fw.write(response.content)
        fw.close()
        print('files/' + line[line.rindex('/') + 1: line.rindex('\n')])
        print(str(file_num) + ' files has download...')
        file_num += 1
    f.close()

