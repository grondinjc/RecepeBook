BEGIN TRANSACTION;
DROP TABLE IF EXISTS Recepe;
DROP TABLE IF EXISTS Tag;
DROP TABLE IF EXISTS RecepeTagAssoc;
COMMIT;



-- ------------------
-- ----- Tables -----
-- ------------------
BEGIN TRANSACTION;



CREATE TABLE Recepe (
    id           INTEGER                NOT NULL,
    name         VARCHAR(200)           NOT NULL,
    tags_id      INTEGER                NOT NULL,
    video        BLOB,
    
    CONSTRAINT pk_recepe PRIMARY KEY (id),
    CONSTRAINT fk_tags FOREIGN KEY (tags_id) REFERENCES RecepeTagAssoc (recepe_id)
);


CREATE TABLE Tag (
    id           INTEGER                NOT NULL,
    name         VARCHAR(30)            NOT NULL,

    CONSTRAINT pk_tag PRIMARY KEY (id)
);


CREATE TABLE RecepeTagAssoc (
    id           INTEGER NOT NULL,
    recepe_id    INTEGER NOT NULL,
    tag_id       INTEGER NOT NULL,

    CONSTRAINT pk_recepetagassoc PRIMARY KEY (id),
    CONSTRAINT fk_recepeid FOREIGN KEY (recepe_id) REFERENCES Recepe (id),
    CONSTRAINT fk_tagid FOREIGN KEY (tag_id) REFERENCES Tag (id)
);



COMMIT;