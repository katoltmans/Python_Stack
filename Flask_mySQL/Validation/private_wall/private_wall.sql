-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema private_wall_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `private_wall_schema` ;

-- -----------------------------------------------------
-- Schema private_wall_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `private_wall_schema` DEFAULT CHARACTER SET utf8 ;
USE `private_wall_schema` ;

-- -----------------------------------------------------
-- Table `private_wall_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `private_wall_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `private_wall_schema`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `private_wall_schema`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `message` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `private_wall_schema`.`users_has_messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `private_wall_schema`.`users_has_messages` (
  `users_id` INT NOT NULL,
  `messages_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `messages_id`),
  INDEX `fk_users_has_messages_messages1_idx` (`messages_id` ASC) VISIBLE,
  INDEX `fk_users_has_messages_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_messages_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `private_wall_schema`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_messages_messages1`
    FOREIGN KEY (`messages_id`)
    REFERENCES `private_wall_schema`.`messages` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
