-- 2022년 10월에 작성된 게시글 제목(title), 게시글 ID(board_id), // used_goods_board 
-- 댓글 ID(reply_id), 댓글 작성자 ID(writer_id), 댓글 내용(contents), 댓글 작성일(created_date) // used_goods_reply
-- 댓글 작성일 오름차순 정렬 , 게시글 제목 오름차순 정렬
SELECT A.TITLE,
    A.BOARD_ID,
    B.REPLY_ID,
    B.WRITER_ID,
    B.CONTENTS,
    DATE_FORMAT(B.CREATED_DATE, '%Y-%M-%D') AS CREATED_DATE
FROM USED_GOODS_BOARD AS A
    JOIN USED_GOODS_REPLY AS B ON A.BOARD_ID = B.BOARD_ID
WHERE A.CREATED_DATE LIKE '2022-10-%'
ORDER BY CREATED_DATE,
    TITLE;