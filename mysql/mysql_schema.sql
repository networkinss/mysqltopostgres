/* SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO"; */
/* SET AUTOCOMMIT = 0; */
/* START TRANSACTION; */
/* SET time_zone = "+00:00"; */
--
-- Database: `core`
--
CREATE DATABASE IF NOT EXISTS `core` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Customer` generated from model 'Customer'
--

CREATE TABLE IF NOT EXISTS `core`.`Customer`
(
    `firstname` TEXT NOT NULL,
    `lastname`  TEXT NOT NULL,
    `age`       INT  NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

--
-- Table structure for table `ErrorModel` generated from model 'ErrorModel'
--

CREATE TABLE IF NOT EXISTS `core`.`ErrorModel`
(
    `code`    INT  NOT NULL,
    `message` TEXT NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

--
-- Table structure for table `Invoice` generated from model 'Invoice'
--

CREATE TABLE IF NOT EXISTS `core`.`Invoice`
(
    `product` TEXT           NOT NULL,
    `amount`  INT            NOT NULL,
    `price`   DECIMAL(20, 9) NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

--
-- Table structure for table `Pet` generated from model 'Pet'
--

CREATE TABLE IF NOT EXISTS `core`.`Pet`
(
    `name`   TEXT           NOT NULL,
    `amount` INT            NOT NULL,
    `price`  DECIMAL(20, 9) NOT NULL,
    `status` TEXT           NOT NULL,
    `tags`   JSON           NOT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;


