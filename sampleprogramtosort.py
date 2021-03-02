import sys
import csv
#In order to use the code dynamic we can pass arguments from command line or from IDE too
from sys import argv
from operator import itemgetter

num_of_arguments = len(argv)

# As arguements are getting passed, in order to hint the user to go in correct direction, below are the steps are needed
# Conditions need to be checked before proceeding to the next steps
if num_of_arguments == 2 and argv[1] in ('-h', '-help'):
    print("Usage of the code : %s source_file.csv 1st_sort_col ... nth_sort_col" % argv[0])
    print("Example: %s sample.csv 1 2 -6" % argv[0])
    print("\tSorts sample.csv on 1st and 2nd columns (ascending, default is this pattern) then 6th descending.")
    sys.exit()
elif num_of_arguments < 3: # We need to pass minimum 3 arguement atleast
    usage = "Usage of the code: %s source_file.csv 1st_sort_col ... nth_sort_col" % argv[0]
    error = "You passed only %d arguments" % num_of_arguments
    sys.exit("%s -- %s" % (usage, error))
if '.csv' not in argv[1]: # For the code to execute, we need to have .csv file
    usage = "Usage: %s source_file.csv 1st_sort_col ... nth_sort_col" % argv[0]
    error = "You passed %r for source_file.csv" % argv[1]
    sys.exit("%s -- %s" % (usage, error))

# Genereated output will come with _output before .csv extension
source_file = argv[1]
output_file = source_file.replace('.csv', '_output.csv')

# First open the source file in read mode and also output file in write mode
try:
    source = open(source_file, 'r')
except:  #if file is not found or some errors
    e = sys.exc_info()[0]
    sys.exit("Error - Could not open input file %r: %s" % (source_file, e))
try: 
    targetFile = open(output_file, 'w')
except:
    e = sys.exc_info()[0]
    sys.exit("Error - Could not open output file %r: %s" % (output_file, e))
print("\nSorting output_data from %r into %r, inside out" % (source_file, output_file))

# creating a list of sorting tuples in which the first item is the index of 
# the data object you wish to sort and the second item is the type of sort,
# Ascending (Reverse is False) or Descending (Reverse is True)
sorts = []
for i in range (2, num_of_arguments): # Skip script name and input filename
	# Ensure you are passed Excel-like column numbers
    try: 
        sort_arguments = int(argv[i])
    except:
        e = sys.exc_info()[0]
        sys.exit("Error - Sort column %r not an integer: %s." % (argv[i], e))
    if sort_arguments == 0:
        sys.exit("Error - Use Excel-like column numbers from 1 to N")
            # Creation of tuple
    if sort_arguments > 0:
        sorts.append((sort_arguments - 1, True)) # Convert column num to index num
    else:
        sorts.append(((-1 * sort_arguments) - 1, True))

# Read in the data creating a label list and list of one tuple per row
reader = csv.reader(source)
row_count = 0 
output_data=[] 
for row in reader:
    row_count += 1
	# Place the first row into the header
    if row_count == 1:
        header = row
        continue
	# Append all non-header rows into a list of data as a tuple of cells
    output_data.append(tuple(row))

#reversed will do the magic in sorting.

for sort_step in reversed(sorts):
    print("before in output_data..")
    print('Sorting Column %d ("%s") Descending=%s' % \
	(sort_step[0] + 1, header[sort_step[0]], sort_step[1])) # +1 for Excel col num
    output_data = sorted(output_data, key=itemgetter(sort_step[0]), reverse=sort_step[1])
    #print("output_data..",output_data)
print('Done sorting %d output_data rows (excluding header row) from %r' % \
((row_count - 1), source_file))


# Now write all of this out to the new file
writer = csv.writer(targetFile)
writer.writerow(header) # Write the header in CSV format

for sorted_row in output_data: # Wrtie the sorted output_data, converting to CSV format
    writer.writerow(sorted_row)
print('Done writing %d rows (sorted output_data plus header) to %r\n' % \
(row_count, output_file))

# Always best to close 
source.closed
targetFile.closed
