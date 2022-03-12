select c.color, ifnull(month.numSold,0) as month, ifnull(year.numSold,0) as year, ifnull(alltime.numSold,0) as alltime
from (select color 
from color 
union all
select 'multiple') as c
left join
(select color, count(color) as numSold
from(
select s.vin, count(s.vin)
from sellvehicle as s 
inner join vehiclecolor as vc on s.vin=vc.vin
group by s.vin
having count(s.vin)=1) as k, vehiclecolor as vc, color as c
where vc.vin=k.vin and c.colorid=vc.colorid
group by color
union all
select 'multiple', count(vin)
from(
select s.vin, count(s.vin) as cc
from sellvehicle as s 
inner join vehiclecolor as vc on s.vin=vc.vin
inner join color c on c.colorid=vc.colorid
group by s.vin
having cc>1) as t
) as alltime
on c.color = alltime.color
left join
(select color, count(color) as numSold
from(
select s.vin, count(s.vin)
from sellvehicle as s 
inner join vehiclecolor as vc on s.vin=vc.vin
where datediff((SELECT MAX(soldDate) SDate
FROM sellVehicle), solddate)<=30
group by s.vin
having count(s.vin)=1) as k, vehiclecolor as vc, color as c
where vc.vin=k.vin and c.colorid=vc.colorid 
group by color
union all
select 'multiple', count(vin)
from(
select s.vin, count(s.vin) as cc
from sellvehicle as s 
inner join vehiclecolor as vc on s.vin=vc.vin
inner join color c on c.colorid=vc.colorid
where datediff((SELECT MAX(soldDate) SDate
FROM sellVehicle), solddate)<=30
group by s.vin
having cc>1) as t) as month
on c.color = month.color
left join
(select color, count(color) as numsold
from(
select s.vin, count(s.vin)
from sellvehicle as s 
inner join vehiclecolor as vc on s.vin=vc.vin
where datediff((SELECT MAX(soldDate) SDate
FROM sellVehicle), solddate)<=365
group by s.vin
having count(s.vin)=1) as k, vehiclecolor as vc, color as c
where vc.vin=k.vin and c.colorid=vc.colorid 
group by color
union all
select 'multiple', count(vin)
from(
select s.vin, count(s.vin) as cc
from sellvehicle as s 
inner join vehiclecolor as vc on s.vin=vc.vin
inner join color c on c.colorid=vc.colorid
where datediff((SELECT MAX(soldDate) SDate
FROM sellVehicle), solddate)<=365
group by s.vin
having cc>1) as t) as year
on c.color=year.color
order by c.color;