def get_book_text (file_path):
        with open(file_path) as file:
                file_contents = file.read()
                list_words = file_contents.split()
                num_words = len(list_words)
                print (f"Found {num_words} total words")


def count_symbols (file_path) -> dict[str, int]:
	symbol_dict: dict[str, int] = {}
	with open(file_path, "r", encoding="utf-8") as file:
		text = file.read()
	for ch in text:
		symbol_dict[ch.lower()] = symbol_dict.get(ch.lower(), 0) +1
	return(symbol_dict)


def sorted_dicts (symbol_dict): 
	char_list = []
	char_key = "char"
	count_key = "num"
	for sym, count in symbol_dict.items():
		if sym.isalpha():
			char_list.append({
				char_key: sym,
				count_key: count
			})
		else:
			continue
	char_list.sort(reverse=True, key=lambda d: d["num"])
	for entry in char_list:
		print (f"{entry['char']}: {entry['num']}")

	





