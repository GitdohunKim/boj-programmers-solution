-- 코드를 입력하세요
SELECT
    A.AUTHOR_ID,
    B.AUTHOR_NAME,
    A.CATEGORY,
    SUM(A.PRICE * C.SALES)AS TOTAL_SALES
FROM
    BOOK A
LEFT OUTER JOIN AUTHOR B ON
    A.AUTHOR_ID = B.AUTHOR_ID
LEFT OUTER JOIN BOOK_SALES C ON
    A.BOOK_ID = C.BOOK_ID AND
    SALES_DATE LIKE '2022-01%'
GROUP BY
    A.AUTHOR_ID,
    A.CATEGORY
ORDER BY
    A.AUTHOR_ID,
    A.CATEGORY DESC