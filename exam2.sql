-- 2.1
select s.*
from student as s
         inner join test as t on s.student_id = t.student_id
where s.class = 'A'
  and s.grade = 1
order by t.math desc limit 1;

-- 2.2
insert into student (student_id, student_name, class, grade) values (5, 'D', 'A', 2);