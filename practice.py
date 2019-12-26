import extracter
import QAchecker

def dividend_revision_update(file):
	output_table = extracter.extract_table(file)
	output_table = QAchecker.Check_valid_date(output_table)
	output_table = QAchecker.Check_valid_amount(output_table)

	return output_table



dividend_revision_table = dividend_revision_update(file1)


## extracter.py
import cleanup
import counter
import QAchecker

def extract_table_ith(table, i):
	df = table[i]
	return df

def extract_table(table):
	table_row = counter.count_table_row(table)
	for table_number in range(0, table_row):
		selected_table = extract_table_ith(table, table_number)
		if QAchecker.is_table_dividend_rev(selected_table):
			break
		if table_number == table_row-1:
			print("Error: The dividend table does not exist in this file.")

	dividend_table = cleanup.table_extracter(table)



