CREATE OR REPLACE FUNCTION pg_temp.f_inc(int)
  RETURNS int AS 
$$
SELECT $1 + 1 
$$
LANGUAGE sql IMMUTABLE;

SELECT pg_temp.f_inc(4);
