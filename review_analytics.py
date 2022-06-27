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


