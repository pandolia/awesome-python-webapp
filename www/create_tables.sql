drop database if exists test;

create database test;

use test;

grant select, insert, update, delete on test.* to 'test_admin'@'localhost'
identified by '123';

grant all on test.* to 'test_root'@'localhost'
identified by '123';

-- generating SQL for users:
drop table if exists `users`;
create table `users` (
  `id` varchar(50) not null,
  `email` varchar(50) not null,
  `password` varchar(50) not null,
  `admin` bool not null,
  `name` varchar(50) not null,
  `image` varchar(500) not null,
  `created_at` real not null,
  primary key(`id`)
) engine=inodb default charset=utf8;

-- generating SQL for blogs:
drop table if exists `blogs`;
create table `blogs` (
  `id` varchar(50) not null,
  `user_id` varchar(50) not null,
  `user_name` varchar(50) not null,
  `user_image` varchar(500) not null,
  `name` varchar(50) not null,
  `summary` varchar(200) not null,
  `content` text not null,
  `created_at` real not null,
  primary key(`id`)
) engine=inodb default charset=utf8;

-- generating SQL for comments:
drop table if exists `comments`;
create table `comments` (
  `id` varchar(50) not null,
  `blog_id` varchar(50) not null,
  `user_id` varchar(50) not null,
  `user_name` varchar(50) not null,
  `user_image` varchar(500) not null,
  `content` text not null,
  `created_at` real not null,
  primary key(`id`)
) engine=inodb default charset=utf8;

