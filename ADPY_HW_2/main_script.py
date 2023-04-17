from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
text_file_name = 'text_file_1.txt'
with open("phonebook_raw.csv", encoding= 'utf-8') as f:
  rows = csv.reader(f)
  text =list(rows)


def list_deser(list):
  string = ''
  for element in list:
    for el in element:
      string += el
      string += ','
  return string


def deser(text):
  pattern = r'''(\w+)(\s*|\,*)?([А-ё]+)[ ,]*([А-ё]*)(\,*|\s*)?([А-ё]*)(\,*|\s*)?([А-ё– c]*)?(\,*|\s*)?(\+7|7|8)?\s?\(*(\d{3})?\)*[\s*|\-*|\-*]*(\d)?[\s*|\-*|\-*]*(\d)?[\s*|\-*|\-*]*(\d)?[\s*|\-*|\-*]*(\d)?[\s*|\-*|\-*]*(\d)?[\s*|\-*|\-*]*(\d)?[\s*|\-*|\-*]*(\d)?\s?\(*(доб.)?\s*(\d+)?\)*(\,*|\s*)?([A-z+@.0-9]+)?(\n)?'''
  result = re.sub(pattern,r'\1,\3,\4,\6,\8,+7(\11)\12\13\14-\15\16-\17\18\19\20,\22',text)
  full_pattern = r'([А-Я]\w+)[\s*|\,*]?([А-ё]+)[ ,]*([А-ё]*)[\,*|\s*]?([А-ё]*)[\,*|\s*]?([А-ё– c]*)?[\,*|\s*]?(\+7?\s?\(\d{3}?\)\d{3}?-\d{2}?-\d{2}?)?|(\+7\(\)--)?(доб\.\d{4}?)?[\,*|\s*]?([A-z\d.]*@[A-z]*\.ru)?[\,*|\s*]?'
  full_res = re.sub(full_pattern, r'\1,\2,\3,\4,\5,\6,\8,\9', result)
  return full_res


if __name__ == "__main__":



  with open("phonebook.csv", "w", encoding= 'utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')

## Вместо contacts_list подставьте свой список:
    datawriter.writerows(deser(list_deser(text)))
