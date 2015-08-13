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
);

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
);

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
);

