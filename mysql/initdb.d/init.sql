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
  created_at    DATETIME(6)   NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  updated_at    DATETIME(6)   NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
  PRIMARY KEY (room_id)
);

CREATE TABLE IF NOT EXISTS `chat` (
  room_id       VARCHAR(100)  NOT NULL,
  user_id       INT           NOT NULL,
  message       TEXT          NOT NULL,
  created_at    DATETIME(6)   NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (created_at)
);