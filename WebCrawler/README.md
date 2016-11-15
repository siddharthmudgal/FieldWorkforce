
## Task

## Web Crawler for Shopping.com

Implement a robust text scraper that will connect to a page on www.shopping.com, and return a result for a given keyword. Two queries can be performed using this program. The first query is getting the total number of results for a given keyword. The second query is to find all results for a given keywords on a specified page. Handle all the exceptions gracefully any feel free to use your favorite library.


### Following are the URLs
    `http://www.shopping.com/products?KW=<keword>`
    `http://www.shopping.com/products~PG-<number>?KW=<keyword>"`

### Queries: 
    Query 1: (requires a single argument)
    `your_program <keyword>`
    
    Query 2: (requires two arguments)
    `your_program <keyword> <page number>`

 
### The focus of this problem is on correctness and design.


## Instructions to run the program

1. Make sure python is installed
2. Make sure following module are installed
 * urllib2 
 * bs4 
 * cmd 
3. Either open the file in jupyter if installed or use the py file to run
4. Sample run commands
 * count http://www.shopping.com/products?KW=chair
  * to get total number of results on the page
 * result http://www.shopping.com/products~PG-<number>?KW=table\"
  * to get all results
 * quit
  * quits the application





