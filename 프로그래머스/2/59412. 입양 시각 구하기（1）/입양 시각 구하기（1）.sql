-- 코드를 입력하세요
SELECT HOUR(DATETIME) as  HOUR, count(*)
from ANIMAL_OUTS
where hour(DATETIME) <'20:00' and hour(DATETIME) >='9:00'
Group by Hour(DATETIME)
order by HOUR asc