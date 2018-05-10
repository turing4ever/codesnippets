CREATE FUNCTION f_assert(int, int) 
    RETURNS boolean 
STABLE
AS $$
    select $1 = $2 
$$ LANGUAGE sql;
