-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, 
case 
    when TLNO is Null then 'NONE'
    else TLNO
end as TLNO
From PATIENT
where AGE <= 12 and GEND_CD = "W"
Order by AGE DESC, PT_NAME ASC