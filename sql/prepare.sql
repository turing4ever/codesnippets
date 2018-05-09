-- Most questions an Analyst faces are repeating, therefore it's important to reuse code
-- Prepqred statements in posgtres and redshift is a great tool to encapsulate and parametize SQL code
-- For example, if you need run a SQL query to get data between date1 and date2. If you use prepared statement, you can 
-- resue your code easily without search and update the dates each time when you get a new request.

PREPARE fooplan (int, text, bool, numeric) AS
    INSERT INTO foo VALUES($1, $2, $3, $4);
EXECUTE fooplan(1, 'Hunter Valley', 't', 200.00);
DEALLOCATE fooplan; -- this is necessary avoid error complaining about prepared statement already exists 
-- This is better than using temp table to fake arguments
