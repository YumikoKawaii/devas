-- init conversation
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
create table if not exists messages
(
    `id` BIGINT auto_increment primary key,
    `conversation_id` varchar(36),
    `sender` varchar(36),
    `content` text,
    `content_type` varchar(36),
    `action_time` datetime default current_timestamp
) engine = InnoDB default charset =utf8mb4 collate =utf8mb4_unicode_ci;