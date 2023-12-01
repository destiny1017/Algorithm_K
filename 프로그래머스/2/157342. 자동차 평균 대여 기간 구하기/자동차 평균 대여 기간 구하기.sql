-- 코드를 입력하세요
SELECT h.car_id, round(avg(timestampdiff(day, h.start_date, h.end_date) + 1), 1) average_duration
from car_rental_company_rental_history h
group by h.car_id
having average_duration >= 7
order by average_duration desc, car_id desc;

# select h.car_id, timestampdiff(day, h.start_date, h.end_date)
# from car_rental_company_rental_history h
# where h.car_id < 10
# order by h.car_id desc;