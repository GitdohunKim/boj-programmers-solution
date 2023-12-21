-- 코드를 입력하세요
SELECT B.CATEGORY, sum(S.SALES) as TOTAL_SALES
from BOOK as B
inner join BOOK_SALES as S
on B.BOOK_ID = S.BOOK_ID
where Year(S.SALES_DATE) = 2022 and MONTH(S.SALES_DATE) = 1
Group by B.CATEGORY
order by B.CATEGORY asc