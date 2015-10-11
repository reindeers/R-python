# from "Python for data analysis"

import json
path = '/home/sever/usagov_bitly_data2013-05-17-1368832207'
records = [json.loads(line) for line in open(path)]

#counting tzn in pure python
time_zones = [rec["tz"] for rec in records if "tz" in rec]


def get_cnt(sec):
	cnt = {}
	for x in sec:
		if x in cnt:
			cnt[x] += 1
		else:
			cnt[x] = 1
	return cnt 

def top_cnt(tmzn_list, n=10):
	tzn_pairs = [(tmzn, cnt) for tmzn, cnt in tmzn_list.items()]
	tzn_pairs.sort()
	return tzn_pairs[-n:]

lst = get_cnt(time_zones)
#print top_cnt(lst)

# same result with collections

from collections import defaultdict

def get_cnt2(sec):
	cnt = defaultdict(int)
	for x in sec:
		cnt[x] += 1
	return cnt

from collections import Counter

lst2 = Counter(time_zones)
#print lst2.most_common(10)

# with pandas

from pandas import DataFrame, Series
import pandas as pd

frame = DataFrame(records)

#print frame["tz"][:10]

tz_cnt = frame["tz"].value_counts()
#print tz_cnt[:10]

clean_tz = frame["tz"].fillna("Missing")
clean_tz[clean_tz == ""] = "Unkown"
tz_cnt2 = clean_tz.value_counts()

#print tz_cnt2[:10]


