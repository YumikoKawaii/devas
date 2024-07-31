-- init conversations
create table conversations
(
    `id` BIGINT auto_increment primary key,
    `user` varchar(36),
    `title` varchar(100),
    `server` varchar(36),
    `created_at` datetime default current_timestamp,
    `deleted_at` datetime
) engine = InnoDB default charset =utf8mb4 collate =utf8mb4_unicode_ci;

-- init messages
create table messages
(
    `id` BIGINT auto_increment primary key,
    `conversation_id` BIGINT,
    `sender` varchar(36),
    `content` text,
    `content_type` varchar(36),
    `action_time` datetime default current_timestamp
) engine = InnoDB default charset =utf8mb4 collate =utf8mb4_unicode_ci;

create table if not exists users
(
    `id` BIGINT auto_increment primary key,
    `email` varchar(100),
    `hash_password` varchar(100),
    `username` varchar(100) unique,
    # can be fetch first time from gravatar
    `avatar` varchar(100),
    `created_at` datetime default current_timestamp,
    `updated_at` datetime default current_timestamp,
    `is_active` tinyint(1)
) engine = InnoDB default charset =utf8mb4 collate =utf8mb4_unicode_ci;