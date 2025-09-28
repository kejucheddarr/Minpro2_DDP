# Minpro2_DDP 
Nabila Salma Putri <br />
NIM 2509116065 <br />
Tema Program: Sistem Pendataan Obat di Rumah Sakit

# FLOWCHART
<img width="2451" height="2301" alt="Image" src="https://github.com/user-attachments/assets/b4edae82-c054-451b-8720-a15fb9f0d4a9" />

# OUTPUT

## Pilih Role
Saat kodenya di run di terminal, pengguna akan memilih untuk login sebagai apoteker atau admin gudang.
<img width="1144" height="191" alt="Image" src="https://github.com/user-attachments/assets/9f40c736-73e8-4ce7-8db7-a310769d8daa" />

## Apoteker
Jika pengguna memilih apoteker, maka akan disuruh untuk input nama dan password pengguna.
<img width="1147" height="169" alt="image" src="https://github.com/user-attachments/assets/8259a9ca-0fc2-484e-858c-ece512e5cb09" />
Jika nama dan password *benar*, maka pengguna akan masuk ke menu utama apoteker.
<img width="1147" height="267" alt="image" src="https://github.com/user-attachments/assets/f49b266e-a0d9-4568-8a57-514febdd5c23" />
Jika nama dan password *tidak benar*, maka pengguna akan balik ke menu login sebagai apoteker/admin gudang.
<img width="1144" height="270" alt="image" src="https://github.com/user-attachments/assets/6b645f8a-99dc-4afa-8e57-554df064b3d4" />

### Menu utama apoteker
<img width="1150" height="158" alt="image" src="https://github.com/user-attachments/assets/046bad39-d192-413e-a821-2558236fb4e5" />

### Opsi 1 Input data obat
Jika apoteker memilih opsi 1, pengguna bisa menginput nama obatnya, bentuk sediaannya, dan golongan obatnya, agar data bisa masuk ke list data obat.
<img width="1143" height="168" alt="image" src="https://github.com/user-attachments/assets/158dbb0b-2bd3-4305-9955-c4688850c830" />
Setelah menginput obat, datanya akan tersimpan ke list data obat. Program selesai
<img width="1148" height="158" alt="image" src="https://github.com/user-attachments/assets/f25eccff-756f-4301-a419-6323c1fced62" />

### Opsi 2 Cari obat
Jika apoteker memilih opsi 2, apoteker bisa mencari obat menggunakan 'search' atau 'filter'.
<img width="1145" height="166" alt="image" src="https://github.com/user-attachments/assets/bf4d30b3-6fb0-4bc9-a04d-6b75e458836a" />

#### - Mencari obat menggunakan 'Search'
Ketika apoteker memilih untuk menggunakan fitur 'search', apoteker dapat mencari dengan menginput nama obatnya. Jika obat yang dicari *ada* di dalam list data obat, maka akan muncul. Program selesai.
<img width="1145" height="141" alt="image" src="https://github.com/user-attachments/assets/5867130a-e70c-4444-8639-477552119b76" />
Jika obat yang dicari *tidak ada* di dalam list data obat, maka akan muncul tulisan 'Obat Tidak Tersedia', dan program akan berhenti selesai.
<img width="1139" height="108" alt="image" src="https://github.com/user-attachments/assets/3f83001c-7b7a-44df-a7de-94daed181d50" />

#### - Mencari obat menggunakan 'Filter'
Ketika apoteker memilih untuk menggunakan fitur 'filter', apoteker dapat mencari obat dengan pilih diantara kategori 'golongan' atau 'bentuk' obat.
<img width="1143" height="153" alt="image" src="https://github.com/user-attachments/assets/0d6513f9-f6a7-4a8c-8f32-211ca1871606" />
**- Kategori golongan** <br />
Jika pilih kategori golongan obat, apoteker dapat mencari obat dari golongannya (bebas, bebas terbatas, keras, narkotika). Kalau golongan yang di cari *ada* di list golongan, maka obat-obat yang termasuk di kategori golongan itu akan muncul. Program selesai. 
<img width="1141" height="122" alt="image" src="https://github.com/user-attachments/assets/e00d812d-9b17-47be-88d1-ce2246f196b3" />
Tapi, kalau golongan yang di input tidak ada di list golongan, maka akan muncul tulisan 'Golongan Obat Tidak Tersedia', dan program akan berhenti.
<img width="1141" height="97" alt="image" src="https://github.com/user-attachments/assets/cb823ced-7d10-435d-a91a-1e89b507d6c1" />
**- Kategori bentuk sediaan** <br />
Jika pilih kategori bentuk obat, maka apoteker dapat mencari obat dari bentuknya. Kalau bentuk yang di input *ada* di list bentuk, maka obat-obat yang termasuk di kategori bentuk itu akan muncul. Program selesai. 
<img width="1150" height="137" alt="image" src="https://github.com/user-attachments/assets/d172a2a3-7d8d-4598-8470-e6ed961d4248" />
Namun, jika bentuk yang di input *tidak ada* di list bentuk, maka akan muncul tulisan 'Bentuk Obat Tidak Tersedia', dan program akan berhenti.
<img width="1144" height="129" alt="image" src="https://github.com/user-attachments/assets/b3314e4e-7ce4-4a4d-b246-6faa7d7ee644" />

### Opsi 3 Keluar
Jika apoteker memilih opsi ini, maka program akan berhenti.
<img width="1143" height="185" alt="image" src="https://github.com/user-attachments/assets/46793e2c-0a92-4fab-94f5-97a9df863169" />

## Admin Gudang
Jika pengguna memilih admin gudang, maka akan disuruh untuk input nama dan password pengguna.
<img width="1148" height="135" alt="image" src="https://github.com/user-attachments/assets/f4f4accd-fa3a-4506-b345-9fe60fce6bd8" />
Jika nama dan password *benar*, maka akan masuk ke menu utama admin gudang.
