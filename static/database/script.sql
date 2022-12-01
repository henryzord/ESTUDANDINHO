PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE jogadores(
    id_jogador INTEGER NOT NULL,
    valor TEXT NOT NULL,
    nome TEXT NOT NULL,
    PRIMARY KEY(id_jogador)
);

INSERT INTO jogadores(id_jogador, valor, nome) VALUES
    (1, 'neymar_jr', 'Neymar Jr.');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES
    (2, 'vinicius_jr', 'Vinicius Jr.');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES
    (3, 'daniel_alves', 'Daniel Alves');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES
    (4, 'casemiro', 'Casemiro');

COMMIT;
