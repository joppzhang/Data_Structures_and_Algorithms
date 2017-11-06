import random

def get_next(str,next_list):
	next_list[0] = -1
	j = 0
	k = -1
	while j < len(str) - 1:
		if k == -1 or str[j] == str[k]:
			j = j + 1
			k = k + 1
			next_list[j] = k
		else:
			k = next_list[k]

def main():
	str = "asdasdasdasdffasdasdasdasdqwezxczxczxc"
	next_list = [-2 for i in range(0,len(str))]
	get_next(str,next_list)
	print(next_list)

if __name__=='__main__':
	main()