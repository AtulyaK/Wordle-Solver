import csv
in_txt = csv.reader(open('text_list/word_list.txt', "r"), delimiter = '\n')
out_csv = csv.writer(open('text_list/word_list.csv', 'w'))

out_csv.writerows(in_txt)