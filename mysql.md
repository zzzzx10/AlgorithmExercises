### 表格连接

左连接  from a  ***left join***  b  ***on***  a.c=b.c ***and*** a.d>b.e

不管右边是否为空

```mysql
select FirstName, LastName, City, State 
from person p left join address a
on p.personid = a.personid ;
```

### 排序及偏移值

```mysql
order by   asc 升序（默认）,
		   desc 降序
limit 1 offset 1 ;
或者 limit offset,1
```

使用`limit`限制条数，`offset` 设置偏移值

多条排序用逗号隔开

### 空值问题

如果select返回结果为空，实际返回的是“”字符串，若想返回`NULL`，需要

```sql
SELECT   IFNULL( 
    (select a from table) , null 
) as nickname ;
或者 select(  select ... );
```

### 函数

```mysql
CREATE FUNCTION getN (N INT) RETURNS INT
BEGIN
  DECLARE M INT;  //使用前需要声明变量
  DECLARE output INT;
  SET M=N-1;
  SET output = (select * from 'table' where a > M);
  RETURN output;
END
```



### 日期格式

```mysql
DATE_FORMAT(date,format) 
```

format:  '%Y-%m'       ->   2019-09

格式	描述
%a	缩写星期名
%b	缩写月名
%c	月，数值
%D	带有英文前缀的月中的天
%d	月的天，数值(00-31)
%e	月的天，数值(0-31)
%f	微秒
%H	小时 (00-23)
%h	小时 (01-12)
%I	小时 (01-12)
%i	分钟，数值(00-59)
%j	年的天 (001-366)
%k	小时 (0-23)
%l	小时 (1-12)
%M	月名
%m	月，数值(00-12)
%p	AM 或 PM
%r	时间，12-小时（hh:mm:ss AM 或 PM）
%S	秒(00-59)
%s	秒(00-59)
%T	时间, 24-小时 (hh:mm:ss)
%U	周 (00-53) 星期日是一周的第一天
%u	周 (00-53) 星期一是一周的第一天
%V	周 (01-53) 星期日是一周的第一天，与 %X 使用
%v	周 (01-53) 星期一是一周的第一天，与 %x 使用
%W	星期名
%w	周的天 （0=星期日, 6=星期六）
%X	年，其中的星期日是周的第一天，4 位，与 %V 使用
%x	年，其中的星期一是周的第一天，4 位，与 %v 使用
%Y	年，4 位
%y	年，2 位

### 自定义变量-排序后加序号

变量名之前使用`@`符号。FROM子句中的`(@rank:= 0)`部分可以进行变量初始化

```mysql
SELECT (@rank := @rank+1) AS rank 
FROM ( SELECT * FROM table_name ) a,
	(SELECT @rank :=0) b 
```

并列的排序相同，增加自定义变量

```mysql
#两种变量case when then (else) end
SELECT a.mon AS r,a.sum AS x,
CASE 
WHEN @prevRank = a.sum THEN @curRank 
WHEN @prevRank := a.sum THEN @curRank := @curRank + 1
END AS j
FROM 
(SELECT DATE_FORMAT(t.order_time,'%Y-%m') AS mon, SUM(t.order_amount) AS sum
FROM orders t
WHERE YEAR(t.order_time) = 2018
GROUP BY MONTH(t.order_time)
ORDER BY SUM(t.order_amount) DESC) a,(SELECT @curRank :=0, @prevRank := NULL) b
```

```mysql
#两种变量 if(条件，1，0)
SELECT Score, Rank FROM
(SELECT Score,
@curRank := IF(@prevRank = Score, @curRank+0,@curRank:=@curRank+1) AS Rank,
@prevRank := Score
FROM Scores, (
SELECT @curRank :=0, @prevRank := NULL
) r
ORDER BY Score DESC) s
```

```mysql
#每组的前k个，使用三个变量
select d.name as Department, s.name as Employee, s.salary as Salary from 
(
select name,salary,departmentid, 
        case
        when @preid=departmentid and @presa = salary then @rank
        when @preid=departmentid and @presa:= salary then @rank:=@rank+1
        when @preid:=departmentid then @rank:=1
        end as rank
from employee , (select @preid:=null,@rank:=0,@presa:=null) b
order by departmentid,salary desc
) s join department d on s.departmentid = d.id
where rank<=3
```



## DoneList

175, 176，177,178,180-185

