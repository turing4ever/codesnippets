CREATE OR REPLACE FUNCTION assert(expected anyelement, got anyelement) RETURNS SETOF void
AS $$
BEGIN
  IF got!=expected THEN
    RAISE EXCEPTION 'got % results, expected %', got, expected;
  END IF;
END;
$$ LANGUAGE plpgsql;

select assert(0, 1);
