from sklearn.feature_extraction.text import TfidfVectorizer

# Baca file corpus.txt
with open('corpus.txt', 'r') as file:
    corpus = file.readlines()

# Hapus newline dari setiap baris
corpus = [line.strip() for line in corpus]

# Inisiasi obyek TfidfVectorizer
vect = TfidfVectorizer(stop_words='english')

# Pembobotan TF-IDF
resp = vect.fit_transform(corpus)

# Cetak Hasil
print(resp)

print(vect.get_feature_names_out())