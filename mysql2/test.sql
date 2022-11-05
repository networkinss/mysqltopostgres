CREATE TABLE `test_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_2` int(11) NOT NULL,
  `sting_line` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `type` enum('type_1','type_2') COLLATE utf8_unicode_ci NOT NULL COMMENT '(DC2Type:order_type)',
  PRIMARY KEY (`id`),
  UNIQUE KEY `UNIQ_123` (`id_2`),
) ENGINE=InnoDB;

INSERT INTO `orders` VALUES (1,'2','McDonald\'s','type_1')
INSERT INTO `orders` VALUES (2,'1','KFC','type_2')