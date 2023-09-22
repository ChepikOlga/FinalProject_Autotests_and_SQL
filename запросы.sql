SELECT c.login, COUNT(o.id) FROM "Orders" AS o INNER JOIN "Couriers" AS c ON c.id = o."courierId" WHERE o."inDelivery" GROUP BY c.login;

SELECT track, CASE WHEN finished THEN 2 WHEN cancelled THEN -1 WHEN "inDelivery" THEN 1 ELSE 0 END  as "Anotherstatus" FROM "Orders";