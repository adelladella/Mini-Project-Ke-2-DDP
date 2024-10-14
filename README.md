# Mini-Project-Ke-2-DDP
Berisi mengenai Laporan Mini Project Praktikum Dasar-dasar pemrograman ke 2. 

# Mini Project Dasar Pemrograman_Adella Putri
Untuk memenuhi tugas Mini Project praktikum Dasar-dasar pemrograman 2024.

Nama  : Adella Putri

NIM   : 2409116006

Kelas : A sistem Informasi 2024

Judul dan tema project : HiCheck!
Haid Checker, sistem pemantauan siklus haid(Menstruasi) dan mengatasi gejalanya untuk wanita.

yang dimana, sistem ini berisi mengenai informasi dan pemantauan siklus Menstruasi wanita, yang tidak hanya memperkirakan kapan menstruasi berikutnya, tetapi juga memberikan tips untuk mengatasi gejala yang mungkin muncul saat menstruasi. Serta dilengkapi berbagai fitur admin lengkap dengan CRUD nya.

# FlowChart
![Flowchart Haid Checker drawio](https://github.com/user-attachments/assets/b93ee91d-f9d3-4312-a2bb-89079bc903b8)

# Penjelasan output
# **1. Bagian awal atau Header :**

![Cuplikan layar 2024-10-14 180657](https://github.com/user-attachments/assets/ddf40a5a-4eda-4a7f-b502-1da01b278f7e)
- Saat pertama kali program dijalankan, pengguna akan melihat pesan selamat datang.

# **2. Proses Login**
- Pertama-tama, user akan diminta menginputkan Username lalu setelah itu Password.
- Jika user meninputkan USN dan PW sebagai Pengguna, output nya berupa :
  
  ![Cuplikan layar 2024-10-14 180722](https://github.com/user-attachments/assets/22721c24-2826-44c4-9212-423871c0aaeb)
  
  Otomatis akan terlogin sebagai pengguna.
- Jika Jika user meninputkan USN dan PW sebagai Admin, output nya berupa :

  ![Cuplikan layar 2024-10-14 182804](https://github.com/user-attachments/assets/bfb3b073-68f7-4c1a-be09-cc76b7403a6a)
  
  Otomatis akan terlogin sebagai admin.
- Jika Login tidak sesuai dengan data yang ada, maka output nya :
  
  ![Cuplikan layar 2024-10-14 183021](https://github.com/user-attachments/assets/409d1689-c953-4634-8496-e8f298adda1e)

# **3. Tampilan Menu Awal**
- Jika user yang login adalah sebagai pengguna, mereka akan melihat menu Pengguna:

  ![Cuplikan layar 2024-10-14 183527](https://github.com/user-attachments/assets/8aef0a2f-a9ed-463c-be19-0cc523f44e0e)
  
- Jika user yang login adalah admin, mereka akan melihat menu Admin:

  ![Cuplikan layar 2024-10-14 183741](https://github.com/user-attachments/assets/1dcbd077-2922-456e-a7e0-99e5fc9f3de0)
  
# **4. Tampilan Menu Sebagai Pengguna :**
- Jika Pengguna memilih pilihan **Menu 1.** Output nya :

  ![Cuplikan layar 2024-10-14 184228](https://github.com/user-attachments/assets/845533ae-042e-40c1-8b27-ff69fb97387b)

  - Pengguna akan diminta input data kapan terakhir atau data menstruasi berupa Tanggal, Bulan, dan Tahun.
  - Setelah itu, pengguna diminta input lama durasi menstruasi.
  - Setelah itu, data yang di input akan otomatis tersimpan.


- Jika Pengguna memilih pilihan **Menu 2.** Output nya :

  ![Cuplikan layar 2024-10-14 184632](https://github.com/user-attachments/assets/6053d688-af7d-4236-b5bb-a977850eabac)

   - Maka secara otomatis akan tertampil table dari data menstruasi yang telah di input sebelumnya.


- Jika Pengguna memilih pilihan **Menu 3.** Output nya :

  ![Cuplikan layar 2024-10-14 184844](https://github.com/user-attachments/assets/2bc65794-738e-450d-b5a2-b825a841ed1e)
  
   - Akan secara otomatis tertampil perkiraan haid berikut nya,
     melalui data durasi lama menstruasi pengguna, ditambah dengan rata-rata siklus menstruasi wanita yang berlangsung selama 28 hari.

  
- Jika Pengguna memilih pilihan **Menu 4.** Output nya :

   ![Cuplikan layar 2024-10-14 185251](https://github.com/user-attachments/assets/5eb0b10c-b924-4d0f-9feb-c587aa5736f0)
  
   - Secara otomatis tertampil Tips and Trick atau tata cara dalam penanganan gejala haid dalam bentuk table.

     
- Jika Pengguna memilih pilihan **Menu 5.** Output nya :

  ![Cuplikan layar 2024-10-14 185534](https://github.com/user-attachments/assets/7054fda7-a34f-471a-9e1d-5b4b72cba42a)
  
  - Otomatis program akan berhenti.
  - Namun, user akan di tanya apa ingin menggunakan program kembali atau tidak,
    
    jika Ya(y), maka user akan diarahkan kembali ke tampilan utama input USN dan PW.
    
    jika Tidak(n), maka program akan berhenti dan tidak menampilkan apa-apa lagi.

# **5. Tampilan Menu Sebagai Admin :**
**- Jika Admin memilih pilihan Menu 1. Output nya :**

  ![Cuplikan layar 2024-10-14 190526](https://github.com/user-attachments/assets/dfa21745-738b-44fa-af0a-a889ac0ec811)

  - Yang dimana, didalam menu Admin **1(Kelola Admin)**, terdapat menu lain lagi yang dapat mengelola keseluruhan data para Admin di dalam program ini.
    - Dan jika user menginput **Menu 1** pada menu kelola admin, output nya berupa :
      
      ![Cuplikan layar 2024-10-14 190837](https://github.com/user-attachments/assets/06d3fe82-b46e-43af-add9-a1e6e18e9200)
      
      disini User akan menginputkan USN dan PW dari admin baru yang akan di tambahkan, lalu data dari pengguna baru pun berhasil di tambahkan.
      
      
    - Dan jika user menginput **Menu 2** pada menu kelola admin, output nya berupa :

      ![Cuplikan layar 2024-10-14 191059](https://github.com/user-attachments/assets/b1f63f25-bd4b-4325-aa74-14d7aa0b3781)

      disini User akan menginputkan cukup USN dari admin yang ingin di hapus, jika sudah maka akan keluar output bahwa admin telah di hapus.
      

    - Dan jika user menginput **Menu 3** pada menu kelola admin, output nya berupa :

      ![Cuplikan layar 2024-10-14 191251](https://github.com/user-attachments/assets/20b24eb1-a3ac-4d23-9651-e9eef9fc08fa)

      disini User akan melihat tampilan dari data admin di dalam program berupa table.
      

    - Dan jika user menginput **Menu 4** pada menu kelola admin, output nya berupa :

      ![Cuplikan layar 2024-10-14 191442](https://github.com/user-attachments/assets/ceffed55-94c4-4483-b9a2-30f5fd0dbf7b)

      disini User akan diarahkan kembali ke menu awal yang tampil sebagai Admin, dan lanjut ke pembahasan menu berikut nya.
      
  
**- Jika Admin memilih pilihan Menu 2. Output nya :**

  ![Cuplikan layar 2024-10-14 191646](https://github.com/user-attachments/assets/905553d5-3965-4cdd-9b79-0fc170740ea9)

  - Yang dimana, didalam menu **Admin 2(Kelola Pengguna)**, terdapat menu lain lagi yang dapat mengelola keseluruhan data para Pengguna di dalam program ini.
    - Dan jika user menginput **Menu 1** pada menu kelola pengguna, output nya berupa :
    
      ![Cuplikan layar 2024-10-14 192210](https://github.com/user-attachments/assets/ed70a4b2-4a77-43d5-965f-51b879f948e2)

      disini User akan menginputkan USN dan PW dari Pengguna baru yang akan di tambahkan, lalu data dari pengguna baru pun berhasil di tambahkan.
      

    - Dan jika user menginput **Menu 2** pada menu kelola Pengguna, output nya berupa :
      
      ![Cuplikan layar 2024-10-14 192552](https://github.com/user-attachments/assets/6212e8f3-60b9-458c-ae2d-aa47a4307c1e)

      disini User akan menginputkan cukup USN dari pengguna yang ingin di hapus, jika sudah maka akan keluar output bahwa pengguna telah di hapus.
      

    - Dan jika user menginput **Menu 3** pada menu kelola Pengguna, output nya berupa :
   
      ![Cuplikan layar 2024-10-14 192832](https://github.com/user-attachments/assets/0e8713e7-e42f-4cb6-8b3f-b90ce36221a8)

      disini User akan melihat tampilan dari data pegguna di dalam program berupa table.
      

    - Dan jika user menginput **Menu 4** pada menu kelola Pengguna, output nya berupa :
   
      ![Cuplikan layar 2024-10-14 193147](https://github.com/user-attachments/assets/459d8507-f8f7-4daf-be3c-5254c152f163)

      disini User akan diminta menginput USN dari pengguna yang ingin di tampilkan datanya, lalu akan tertampil data dari pengguna berupa daftar table.
      

    - Dan jika user menginput **Menu 5** pada menu kelola Pengguna, output nya berupa :

      ![Cuplikan layar 2024-10-14 193503](https://github.com/user-attachments/assets/9197fe3e-7136-4e76-9c05-62584b0d4e61)

      disini User akan diminta menginputkan cukup USN dari pengguna yang ingin di hapus, jika sudah maka akan keluar output bahwa data dari pengguna telah di hapus.

      namun disini, sedang tidak ada data pengguna yang ingin user hapus, dan jika user salah menginputkan USN dari pengguna,
      maka output nya akan keluar bahwa data pengguna yang di input salah itu tidak di temukan.

    - Dan jika user menginput **Menu 6** pada menu kelola Pengguna, output nya berupa :
      
      ![Cuplikan layar 2024-10-14 193844](https://github.com/user-attachments/assets/64c19174-bbd3-4c66-99c3-44d669e7e49d)

      maka disini user akan diarahkan ke menu awalan sebagai admin.

  
   **- Jika Admin memilih pilihan Menu 3. Output nya :**

   
![Cuplikan layar 2024-10-14 194005](https://github.com/user-attachments/assets/11a91daf-326e-4000-b17e-d51f1958411a)

 - Otomatis program akan berhenti.
 - Namun, user akan di tanya apa ingin menggunakan program kembali atau tidak,
   
      jika Ya(y), maka user akan diarahkan kembali ke tampilan utama input USN dan PW.
   
      jika Tidak(n), maka program akan berhenti dan tidak menampilkan apa-apa lagi.
