#!/usr/bin/env python3
import sys
def main():
    jp_text = sys.argv[1]
    chs_text = sys.argv[2]
    json_text = sys.argv[3]

    f = open(json_text)
    f2 = open(jp_text)
    f3 = open(chs_text)

    chs = list()
    jp = list()

    global j_text
    j_text = f.read()

    for i in f3:#chs
        st = i
        if st[-1] == '\n':
            st = st[0:-1]
        chs.append(st)
    for i in f2:#jp
        st = i
        if st[-1] == '\n':
            st = st[0:-1]
        jp.append(st)
    
    f.close()
    f2.close()
    f3.close()

    if len(chs)!=len(jp):
        print(r'CHS / JP 文本行数不一致！')
        exit()
    else:
        for i in chs:
            chs_line = i
            jp_line = jp[chs.index(chs_line)]
            # parser '\n'
            print(jp_line,'\n',chs_line)
            j_text = j_text.replace(r'"' + jp_line + r'"',r'"' + chs_line + r'"')

        f_save = open(json_text,'w')
        f_save.write(j_text)

        f_save.close()    
        
try:
    if len(sys.argv)!=4:
        print('Usage:','replacer.py source_text target_text json_file')
        print('And we will replace SOURCE_TEXT -> TARGET_TEXT')
        exit()
    main()
except KeyboardInterrupt:
    exit()