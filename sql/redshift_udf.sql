-- get all udfs
select * from pg_proc where proname ilike 'f\\_%';

create or replace function f_sql_percentage (float)
  returns text
-- convert float into percentage 99.99%
stable
as $$
  select to_char(100 * $1, '990D99%')
$$ language sql;

select f_sql_percentage(0.01);
-- drop function f_sql_percentage(float);
