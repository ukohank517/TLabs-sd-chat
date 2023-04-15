CREATE TABLE IF NOT EXISTS `room_member` (
  room_id       VARCHAR(100)  NOT NULL,
  user_id       INT           NOT NULL,
  ip_address    VARCHAR(100)  NOT NULL,
  created_at    DATETIME(6)   NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (room_id, user_id)
);

CREATE TABLE IF NOT EXISTS `image` (
  room_id       VARCHAR(100)  NOT NULL,
  prompt        TEXT          NOT NULL,
  image_url     TEXT          NOT NULL,
  created_at    DATETIME(6)   NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  updated_at    DATETIME(6)   NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (room_id)
);

CREATE TABLE IF NOT EXISTS `chat` (
  room_id       VARCHAR(100)  NOT NULL,
  user_id       INT           NOT NULL,
  message       TEXT          NOT NULL,
  created_at    DATETIME(6)   NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (created_at)
);


-- INSERT INTO `chat` (room_id, user_id, message, created_at)
-- VALUES
-- ('testroom', 1, 'hello i am user1', '2019-05-02 12:48:35'),
-- ('testroom', 2, 'hello i am user2', '2019-05-02 12:48:36'),
-- ('testroom', 3, 'hello i am user3', '2019-05-02 12:48:37'),
-- ('testroom', 4, 'hello i am user4', '2019-05-02 12:48:38'),
-- ('testroom', 5, 'hello i am user5', '2019-05-02 12:48:39'),
-- ('testroom', 1, 'Oh message 1', '2019-05-02 12:48:40'),
-- ('testroom', 2, 'Oh message 2', '2019-05-02 12:48:41'),
-- ('testroom', 3, 'Oh message 3', '2019-05-02 12:48:42'),
-- ('testroom', 4, 'Oh message 4', '2019-05-02 12:48:43'),
-- ('testroom', 5, 'Oh message5', '2019-05-02 12:48:44');


