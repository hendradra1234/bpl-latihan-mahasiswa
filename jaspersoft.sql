SELECT *
FROM mahasiswa, matkul, ambil
WHERE mahasiswa.nim - ambil.nim
AND matkul.kd_matkul = ambil.kd_matkul;