data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('the file is entirely read, it contains', len(data), 'pieces of comments')

sum_len = 0
for d in data:
	sum_len += len(d)

print("the average length of each piece of comment is", int(sum_len/len(data)))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("in total there are", len(new), "pieces of comment is less than 100 words")
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print("in total there are", len(good), "pieces of comment has a word of 'good'")
print(good[0])
print(good[1])