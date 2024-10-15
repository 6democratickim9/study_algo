-- https://school.programmers.co.kr/learn/courses/30/lessons/59408
-- 코드를 입력하세요
SELECT COUNT(*) AS count
FROM(
    SELECT NAME
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL 
    GROUP BY NAME
    HAVING COUNT(NAME) >= 1

) AS unique_names;