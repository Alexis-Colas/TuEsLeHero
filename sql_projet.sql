DROP TABLE IF EXISTS destination;
DROP TABLE IF EXISTS page;
DROP TABLE IF EXISTS livre;

CREATE TABLE livre
(
    num_livre INT AUTO_INCREMENT,
    nom_livre VARCHAR(25),
    PRIMARY KEY (num_livre)
);

CREATE TABLE page
(
    id_page   INT AUTO_INCREMENT,
    num_page  INT,
    num_livre INT,
    PRIMARY KEY (id_page),
    FOREIGN KEY (num_livre) REFERENCES livre (num_livre)
);

CREATE TABLE destination
(
    id_dst INT AUTO_INCREMENT,
    page_d INT,
    page_a INT,
    PRIMARY KEY (id_dst),
    FOREIGN KEY (page_d) REFERENCES page (id_page),
    FOREIGN KEY (page_a) REFERENCES page (id_page)
);

/*INSERT*/

INSERT INTO livre(num_livre, nom_livre)
VALUES (NULL, 'livre1'),
       (NULL, 'livre2'),
       (NULL, 'livre3');

INSERT INTO page(id_page, num_page, num_livre)
VALUES (NULL, 1, 1),
       (NULL, 2, 1),
       (NULL, 3, 1),

       (NULL, 1, 2),
       (NULL, 2, 2),
       (NULL, 3, 2),
       (NULL, 4, 2),

       (NULL, 1, 3),
       (NULL, 2, 3);

INSERT INTO destination(id_dst, page_d, page_a)
VALUES (NULL, 1, 3),
       (NULL, 3, 2),

       (NULL, 4, 5),
       (NULL, 5, 6),
       (NULL, 5, 7),

       (NULL, 8, 9);
