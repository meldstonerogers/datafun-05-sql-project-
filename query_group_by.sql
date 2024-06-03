-- Get the total number of books by author
SELECT author_id, COUNT(book_id)
FROM books 
GROUP BY author_id;