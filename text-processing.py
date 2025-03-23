import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

dokumen = [
    "elearning di PTTIK diatas jam 6 malam kok selalu gak bisa dibuka ya?",
    "ub tidak punya lahan parkir yang layak. Dan jalanan selalu ramai karena di buka untuk umum. Seperti jalan tol saja. Brawijaya oh brawijaya",
    "Kelas Arsitektur dan Organisasi Komputer penuh, apakah tidak dibuka kelas lagi. Rugi kalo saya bisa ngambil 24 SKS tapi baru 18 SKS yg terpenuhi",
    "Informasi tata cara daftar ulang bagi mahasiswa baru PTIIK kurang jelas. Sehingga ketika tanggal terakhir syarat penyerahan berkas daftar ulang, banyak mahasiswa baru yang tidak membawa salah satu syarat daftar ulangnya."
    ]

# Langkah 1 - Tokenisasi
# Pretokenisasi - Case Folding
dokumen = [d.lower() for d in dokumen]

# Pretokenisasi - Menghilangkan angka, tanda baca dan karakter
dokumen = [re.sub(r'[^a-z\s]', '', d) for d in dokumen]

# Tokenisasi
token = [d.split() for d in dokumen]
print("\nHasil Tokenisasi:")
for i, words in enumerate(token):
    print(f"Dokumen {i+1}: {words}")

# Langkah 2 - Filtering (Stopword Removal)
stopword_factory = StopWordRemoverFactory()
stopwords = stopword_factory.get_stop_words()
token = [[word for word in sentence if word not in stopwords] for sentence in token]
print("\nHasil Stopword Removal:")
for i, words in enumerate(token):
    print(f"Dokumen {i+1}: {words}")

# Langkah 3 - Stemming
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()
token = [[stemmer.stem(word) for word in sentence] for sentence in token]
print("\nHasil Stemming:")
for i, words in enumerate(token):
    print(f"Dokumen {i+1}: {words}")

# Langkah 4 - Hasil Preprocessing
print("\n--------------------------------------------------")
print("Hasil Preprocessing:")
for i, words in enumerate(token):
    words = ", ".join(words)
    print(f"Dokumen {i+1}: {words}")
print("--------------------------------------------------")
