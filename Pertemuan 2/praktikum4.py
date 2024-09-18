from sklearn.preprocessing import OneHotEncoder

# Inisiasi obyek Ordinal Encoder
ohe = OneHotEncoder ()

# Definisikan dataa
# dalam bentuk 2d
data = [
['Politeknik Negeri Malang' ],
['Politeknik Elektronika Negeri Surabaya'],
['Politeknik Negeri Jakarata'],
['Politeknik Negeri Semarang' ]
]

# Transformasi Ordinal Encoder
transform_ohe = ohe.fit_transform(data)

print('Data Asli')
print(data)

print('Data Transformasi One-Hot Encoding')
print(transform_ohe.toarray())