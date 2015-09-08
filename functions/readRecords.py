import readTable
import readMeta

def getRecordsFromTextFile():
	data = {}
	tb = readMeta.tb
	for i in tb.keys():
		cols = readTable.getColumns(i.lower(),tb)
		vRecords = readTable.getRowsFromTable(i.lower(),cols)
		data = readTable.addTableToHash(data,i.lower(),vRecords)
	
	return data



records = getRecordsFromTextFile()

for k in records.keys():
	print("\t%s\t" % k.upper(), end="")
	print()

	for k in records[k].keys():
		print("\t%s\t " % k, end="")
		print()

	input('next')
