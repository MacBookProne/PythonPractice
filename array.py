def array_tests():

	jo = [2, 3, 4, 5, 6]

	jo.pop() #pops the last number in the array

	jo.append(9) #adds the number 1 to the array

	print(jo) #prints array.

	print("Index of 9: ", jo.index(9)) #indexing the given value


	jo.remove(9)
	print("Removal of 9:", jo)

	jo.reverse()
	print("Reversed:", jo)
	print("Sorted Return", sorted(jo))


	jo.sort()
	print("Sorted In Place", jo)


	jo.append(11)

	print(jo)

	print("Index of 9:", jo.index(11))

	jo.append(100)

	print(jo)

	jo.sort()
	print("New sort", jo )
def main():
    array_tests()


if __name__ == "__main__":
    main()
