-- https://school.programmers.co.kr/learn/courses/30/lessons/59041
-- 코드를 입력하세요
SELECT NAME, COUNT(*) as COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT > 1
ORDER BY NAME;
