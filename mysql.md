### 表格连接

左连接  from a  ***left join***  b  ***on***  a.c=b.c

不管右边是否为空

```mysql
select FirstName, LastName, City, State 
from person p left join address a
on p.personid = a.personid
```

### 排序

```mysql
order by   asc 升序（默认）
		   desc 降序
limit 1 offset 1
```

使用`limit`限制条数，`offset` 设置偏移值



### 空值问题

如果select返回结果为空，实际返回的是“”字符串，若想返回`NULL`，需要

```sql
SELECT   IFNULL( 
    (select a from table) , null 
) as nickname
```





## DoneList

175, 176

