-- 코드를 입력하세요
SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, round(avg(B.REVIEW_SCORE),2) as SCORE
from REST_INFO as A
join REST_REVIEW as B
on A.REST_ID = B.REST_ID
where A.ADDRESS like "서울%"
Group by REST_NAME
order by SCORE desc, FAVORITES desc