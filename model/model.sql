CREATE TABLE shows (
        id INT NOT NULL,
        url VARCHAR(192) NOT NULL,
        name VARCHAR(129) NOT NULL,
        season INT NOT NULL,
        number FLOAT,
        type VARCHAR(21) NOT NULL,
        airdate CHAR(10) NOT NULL,
        airtime CHAR(5) NOT NULL,
        airstamp CHAR(25) NOT NULL,
        runtime FLOAT,
        rating FLOAT,
        summary VARCHAR(2250),
        genres VARCHAR(32) NOT NULL,
        officialSite VARCHAR(250),
        nameShow VARCHAR(65),
        averageRuntime FLOAT,
        PRIMARY KEY (id)
);