-- 코드를 입력하세요

select concat('/home/grep/src/', b.board_id, '/', f.file_id, f.file_name, f.file_ext) FILE_PATH
from used_goods_file f, 
(select board_id
from used_goods_board
order by views desc
limit 1) b
where f.board_id = b.board_id
order by file_id desc;