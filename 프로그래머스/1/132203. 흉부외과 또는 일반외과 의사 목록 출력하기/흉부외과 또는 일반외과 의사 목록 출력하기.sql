-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_DATE
from DOCTOR
where MCDP_CD in ("CS","GS")
order by HIRE_YMD desc, DR_NAME asc