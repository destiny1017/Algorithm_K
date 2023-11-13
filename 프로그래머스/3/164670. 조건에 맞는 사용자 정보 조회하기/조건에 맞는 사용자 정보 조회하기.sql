-- 코드를 입력하세요
select u.user_id, u.nickname, concat(u.city, ' ', u.street_address1, ' ', u.street_address2) 전체주소, concat(substr(u.tlno, 1, 3),'-',substr(u.tlno, 4, 4),'-',substr(u.tlno, 8, 4)) 전화번호 
from used_goods_user u 
right join
(SELECT b.writer_id 
from used_goods_board b
group by b.writer_id
having count(b.writer_id) > 2) b
on b.writer_id = u.user_id
order by b.writer_id desc