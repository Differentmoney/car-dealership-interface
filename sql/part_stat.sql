SELECT VendorName, SUM(Quantity) AS TotalParts, SUM(Price * Quantity) AS TotalPrice
FROM Part AS P
GROUP BY VendorName
ORDER BY TotalPrice DESC;
