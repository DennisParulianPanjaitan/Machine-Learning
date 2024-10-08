from sklearn.preprocessing import OneHotEncoder

# Inisiasi obyek Ordinal Encoder
de = OneHotEncoder (drop='first')

# Definisikan dataa
# dalam bentuk 2d
data = [
['Politeknik Negeri Malang' ],
['Politeknik Elektronika Negeri Surabaya'],
['Politeknik Negeri Jakarata'],
['Politeknik Negeri Semarang' ]
]

# Transformasi Ordinal Encoder
transform_de = de.fit_transform(data)

print('Data Asli')
print(data)

print('Data Transformasi One-Hot Encoding')
print(transform_de.toarray())