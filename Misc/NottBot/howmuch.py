import time

lastcount = 0
while True:
	total = 0
	with open("result.csv", "r") as f:
		for i in f.read().split("\n"):
			total += 1
	print(f"total lines: {total}, increase: {total - lastcount}, lines/s: {(total - lastcount)/5}")
	lastcount = total
	time.sleep(5)
