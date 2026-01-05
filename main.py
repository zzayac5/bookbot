import sys
from stats import get_book_text,count_symbols,sorted_dicts 
from pretty import print_title, ch_count_title, end_line


def main():
	if len(sys.argv) > 1:
		print_title()
		get_book_text(sys.argv[1])
		char_dict = count_symbols(sys.argv[1])
		ch_count_title()
		sorted_dicts(char_dict)
		end_line()	
	else:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit(1)


if __name__ == "__main__":
	main()
