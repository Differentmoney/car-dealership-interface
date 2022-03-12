SELECT R.StartDate, R.CompleteDate, R.Vin, Odometer, PC.Total, CONCAT(U.FirstName,' ', U.LastName) name
FROM Repair R, User U, 
(SELECT P.Vin, P.CustomerID, P.StartDate, SUM(Price*Quantity) AS Total 
 FROM Part P
 GROUP BY P.Vin, P.CustomerID, P.StartDate) AS PC
WHERE PC.Vin=R.Vin AND  PC.CustomerID=R.CustomerID AND PC.StartDate=R.StartDate AND U.Username = R.Username
ORDER BY 
StartDate ASC, 
CompleteDate DESC, 
R.Vin ASC;
