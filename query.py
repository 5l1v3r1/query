import os

def main():
	search_query = input("Search: ")
	
	all_files = os.listdir("./")
	txt_files = filter(lambda x: x[-4] == ".txt", all_files)
	
	for txt_file in txt_files:
		t_file = open(txt_file, "r")
		
		for line in t_file:
			if search_query in line:
				print(f"Search Query: {search_query}\n Found: {line}")
				
		t_file.close()

if __name__ == "__main__":
	main()
	
