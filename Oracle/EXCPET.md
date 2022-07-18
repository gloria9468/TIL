# EXTRACT (날짜 추출하기)
###

~~~
select extract('날짜요소' from 컬럼) from 테이블A;
~~~

실제로 적용해서 만들었던 쿼리로는... 
~~~
SELECT (SELECT NAME FROM USR_GLOBAL WHERE USER_ID = H.USER_ID ) NAME, 
        SUBSTR(HOLIDAY, -2) GET_DATE 
FROM TB_TRIP_SCHEDULE_USER_HOLIDAY H
WHERE '2022' = EXTRACT(YEAR FROM TO_DATE(HOLIDAY, 'YYYY.MM.DD'))
AND '7' = EXTRACT(MONTH FROM TO_DATE(HOLIDAY, 'YYYY.MM.DD'))
~~~

맥북으로 바꾸고 아직 오라클을 쓰지 못해서 데이터베이스에서 사용해서 쓸 수가 없다.. 
<br>
<br>
<br>
<span style='color:blue; font-weight:bolder; font-size :20px;' >다음에는 실제 데이터베이스에서 활용한 것을 올려보자.</span>