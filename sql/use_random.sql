-- Use random() to sample large table to speed up the query during testing phase
-- Quite often, you shall need to test your query while writing it, or you simply want to insepct some sample data. 
SELECT * 
FROM Large_table
WHERE Random() < 0.01 -- random() returns random value in the range 0.0 <= x < 1.0, uniform distribution
LIMIT 100
; 
