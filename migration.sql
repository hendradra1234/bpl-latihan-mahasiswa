-- Table: Mahasiswa
CREATE TABLE mahasiswa (
    nim VARCHAR(10) PRIMARY KEY,
    nm_mahasiswa VARCHAR(30) NOT NULL
);

-- Table: matkul
CREATE TABLE matkul (
    kd_matkul VARCHAR(5) PRIMARY KEY,
    nmma_matkul VARCHAR(30) NOT NULL,
    sks ENUM('2', '3', '4')
);

-- Table: ambil (Relation Table)
CREATE TABLE ambil (
    nim VARCHAR(10),
    kd_matkul VARCHAR(5),
    semester ENUM("Gasal", "Genap"),
    thn_akademik INT,
    presensi INT,
    tugas INT,
    uts INT,
    uas INT,
    PRIMARY KEY (nim, kd_matkul),
    FOREIGN KEY (nim) REFERENCES Mahasiswa(nim) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (kd_matkul) REFERENCES matkul(kd_matkul) ON DELETE CASCADE ON UPDATE CASCADE
);