-- 코드를 입력하세요
SELECT B.BOOK_ID, A.AUTHOR_NAME, Date_format(B.PUBLISHED_DATE,'%Y-%m-%d') from BOOK as B
join AUTHOR as A
on B.AUTHOR_ID = A.AUTHOR_ID 
where B.CATEGORY = '경제'
order by B.PUBLISHED_DATE asc