SELECT 
    COUNT(book_id) AS total_books,
    AVG(year_published) AS average_year_published,
    MAX(year_published) AS most_recent_publication
FROM 
    books;
