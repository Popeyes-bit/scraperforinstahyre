Walkthrough of code:
 The code has four main functions namely:-
	def append_list_as_row(file_name, list_of_elem) -- it writes the data in csv'
	def save(file_name,header) -- checks for data..csv in cwd and if it doesn't find data.csv file, it creates the file with tempelate
	def scroll(times) -- scrolls the page to the end
	def visit(newurl) --scrapes the website (Important)


  Diving into def visit(newurl)
	This function takes input as the parent page and scrapes the data of child pages (8 childs in our case) and returns a boolean if everything goes as per the code.
	The function writes the data to test.csv in the working directory.(Even if you encounter any error the data gets saved iteratively so ypu wont loose any data.

  
In the last few lines a while loop is written which is the fuel for the code and the loop stops only when we get a "false" value after def visit(newurl)
the loop prints the index number of child pages that are being scraped and also prints the time taken by every Parent Page(indexed page)


 