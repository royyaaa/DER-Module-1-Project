# DER Module 1 Project

# <center><h2><strong><font color="blue">Data Engineering Module 1 Assignment</font></strong></h2></center>
This repository made for fully the data engineering module 1 assignment in UIII. This project done by:
-	**Selvi Oktaviani (05212510001)**
-	**Nikhla Isfa Khuraiya (05212510002)**

## Introduction
As we all know, brain is one of the most important part in our body. That’s why menjaga kesehatan otak sangat diperlukan. Namun, banyak hal yang bahkan menyebabkan otak kita mengalami kerusakan maupun penurunan fungsi yang masih sering diabaikan. Beberapa waktu terakhir, ada istilah baru untuk penurunan fungsi otak, yakni ‘brainrot’. Brainrot sendiri merupakan penurunan fungsi kognitif pada otak, intelektual, dan mental exhaustion yang disebabkan oleh konsumsi berlebih pada konten singkat berkualitas rendah yang biasa ditemukan di social media dan konten sepele yang tidak menantang. Kasus brainrot ini banyak dialami oleh adolescent, young adult, atau bahkan adult dan anak-anak yang sering menghabiskan waktunya dengan screen time.
Adanya fenomena ini, menjadikan banyak orang yang mulai tertarik untuk menelitinya bahkan mencari tahu apa yang bisa menyembuhkan atau mengatasi brainrot itu sendiri. Banyak orang yang sudah aware kepada dirinya sendiri dari fenomena brainrot. Hal itu menjadikan beberapa orang juga ingin membagikan ilmu lewat konten-konten yang mereka buat yang nantinya akan diupload pada sebuah platform. Salah satu platform populer yang banyak digunakan orang untuk mendapatkan informasi adalah youtube. Pengguna youtube tergolong tinggi jika dibandingkan dengan sosial media lainnya dimana youtube menyajikan berbagai macam konten (informasi) yang dapat disesuaikan dengan kebutuhan seseorang. 

## What did we do?
Dalam project ini, kami ingin mengetahui mengenai (pengaruh durasi lama video dengan viewers/ tren kesadaran masyarakat mengenai brainrot) yang nantinya dapat menunjukkan seberapa besar awareness yang timbul pada masyarakat mengenai brainrot itu sendiri.

## What data we used?
Adapun data yang digunakan dalam analisis ini diambil dari youtube dengan keyword dan region tertentu. Berikut struktur data yang digunakan dalam project ini:
| Variable | Descriptions |
|---------|------------|
| videoId | id dari masing-masing video yang didapatkan |
| title | judul dari video yang didapatkan |
| channel | channel pembuat video yang didapatkan |
| views | jumlah views dalam video yang didapatkan |
| like | jumlah like dalam video yang didapatkan |
| comments | jumlah komen dalam video yang didapatkan |
| publishedAt | waktu published video |
| duration | durasi dari video yang didapatkan |
| region | menunjukkan konten yang popular atau mungkin akan disarankan untuk suatu negara |

Region yang kami gunakan dalam pengerjaan project ini adalah Indonesia (ID), Malaysia (MY), dan Singapore (SG). Pengambilan region ini dilihat berdasarkan negara yang geografis, bahasa, maupun budayanya cenderung lebih dekat dengan indonesia. Adapun keyword yang digunakan dalam project ini adalah (list keyword). Dari keywords dan region yang ditentukan, data yang didapatkan adalah sejumlah (jumlah data).

## How the process was going?
berikut proses pengerjaan project ini:
1.	Data aquitition dengan melakukan fetching data using youtube API
2.	Pembersihan data: meliputi penghapusan konten yang tidak sesuai berdasarkan judul dan duplikasi data
3.	Analysis: conduct a simple Exploratory data analysis (EDA)

## Additional Information (maybe you need it)
Adapun keterangan letak file yang ada dalam project ini:
1.	Fetching data code: 
2.	Data cleaning code:
3.	EDA code:

## Any DISCALIMERS!!!
Here for the disclaimers

## References
Oxford University (2024) ‘Brain rot’ named Oxford Word of the Year 2024. Oxford University Press, Language and Literacy. https://corp.oup.com/news/brain-rot-namedoxford-word-of-the-year-2024/

Özbay, Ö. ‘Brain Rot’ Among University Students in the Digital Age: A Phenomenological Study. Curr Psychiatry Rep 28, 11 (2026). https://doi.org/10.1007/s11920-025-01658-w 
