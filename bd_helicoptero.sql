CREATE TABLE Helicoptero (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo VARCHAR(100) NOT NULL,
    color VARCHAR(50) NOT NULL,
    combustible_inicial INTEGER NOT NULL,
    estado BOOLEAN DEFAULT FALSE
);


INSERT INTO Helicoptero (modelo, color, combustible_inicial) VALUES
('AH-64 Apache', 'Verde', 100),
('UH-60 Black Hawk', 'Negro', 120),
('CH-47 Chinook', 'Gris', 150),
('AH-1 Cobra', 'Camuflaje', 90),
('Mi-24 Hind', 'Verde oliva', 130),
('EC135', 'Blanco', 80),
('Bell 407', 'Azul', 85),
('Sikorsky S-76', 'Plateado', 110),
('Robinson R44', 'Rojo', 70),
('Kamov Ka-92', 'Amarillo', 140);


SELECT * FROM Helicoptero;


SELECT modelo, combustible_inicial FROM Helicoptero WHERE combustible_inicial > 100;


SELECT modelo, MAX(combustible_inicial) as max_combustible FROM Helicoptero;


SELECT color, COUNT(*) as cantidad FROM Helicoptero GROUP BY color;


SELECT modelo, color FROM Helicoptero ORDER BY modelo ASC;
