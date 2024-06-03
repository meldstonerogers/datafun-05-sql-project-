-- Update author's name
UPDATE authors
SET first = 'John Ronald Reuel'
WHERE first = 'J.R.R.';

-- Remove the year of a certain title
UPDATE books
SET year_published = ' '
WHERE title = 'The Hobbit';