--
-- Pet, customer, invoice API.
-- Database: `core`
-- Prepared SQL queries for 'Pet' definition.
--


--
-- SELECT template for table `Pet`
--
SELECT `name`, `amount`, `price`, `status`, `tags`
FROM `core`.`Pet`
WHERE 1;

--
-- INSERT template for table `Pet`
--
INSERT INTO `core`.`Pet`(`name`, `amount`, `price`, `status`, `tags`)
VALUES (?, ?, ?, ?, ?);

--
-- UPDATE template for table `Pet`
--
UPDATE `core`.`Pet`
SET `name`   = ?,
    `amount` = ?,
    `price`  = ?,
    `status` = ?,
    `tags`   = ?
WHERE 1;

--
-- DELETE template for table `Pet`
--
DELETE
FROM `core`.`Pet`
WHERE 0;

