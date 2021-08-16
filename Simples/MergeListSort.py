class TestImpl:
	def mergeArrays(self, list1, list2):
		resultList= list(set(list1) | set(list2))
		resultList.sort()
		print(resultList)

