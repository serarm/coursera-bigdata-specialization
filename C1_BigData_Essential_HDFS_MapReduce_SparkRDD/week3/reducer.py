
import sys

current_key = None
word_sum = 0
c_word_sum=0
for line in sys.stdin:
    try:
        key, count = line.strip().split('\t', 1)
        c_count,t_count = map(int,count.split(":"))
    except ValueError as e:
        continue
    if current_key != key:
        if current_key and c_word_sum>0 and float(c_word_sum)/word_sum<0.005:
            print "%s\t%d" % (current_key, str(c_word_sum)+":"+str(word_sum))
        word_sum = 0
        c_word_sum=0
        current_key = key
    word_sum += t_count
    c_word_sum+=c_count

if current_key and c_word_sum>0 and float(c_word_sum)/word_sum<0.005:
    print "%s\t%d" % (current_key, str(c_word_sum)+":"+str(word_sum))