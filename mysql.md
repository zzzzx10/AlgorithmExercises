左连接  from a **left join** b **on** a.c=b.c

不管右边是否为空

```mysql
select FirstName, LastName, City, State 
from person p left join address a
on p.personid = a.personid
```

