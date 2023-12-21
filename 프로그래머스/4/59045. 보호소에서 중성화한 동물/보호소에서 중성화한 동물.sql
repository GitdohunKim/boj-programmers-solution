-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME from animal_ins as A
inner join animal_outs as B
on A.ANIMAL_ID = B.ANIMAL_ID
where not A.SEX_UPON_INTAKE = B.SEX_UPON_OUTCOME