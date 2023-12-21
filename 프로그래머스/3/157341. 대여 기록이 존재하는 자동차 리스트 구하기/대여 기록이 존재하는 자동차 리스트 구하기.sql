-- 코드를 입력하세요
SELECT A.CAR_ID from CAR_RENTAL_COMPANY_CAR  as A
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as B
on A.CAR_ID = B.CAR_ID
where A.CAR_TYPE = '세단' and month(B.START_DATE) = '10'
group by A.CAR_ID
order by A.CAR_ID desc