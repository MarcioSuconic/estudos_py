import psycopg2

key_personal_api ="xau_WRAvk8hyv6cju9Z2qpihDAgic6MNwyhk5"
post_url = f"postgresql://k04237:{key_personal_api}@us-east-1.sql.xata.sh/marsoft:main?sslmode=require"


dsn = "postgresql://advmsuconic-s-workspace-k04237:xau_WRAvk8hyv6cju9Z2qpihDAgic6MNwyhk5@us-east-1.sql.xata.sh:5432/marsoft:main?sslmode=require"
cnn = psycopg2.connect(post_url)
#   dbname="marsoft:main",
#   user="advmsuconic-s-workspace-k04237",
#   password="xau_WRAvk8hyv6cju9Z2qpihDAgic6MNwyhk5",
#   host="us-east-1.sql.xata.sh",
#   port=5432,
# )

cur = cnn.cursor()
#"INSERT INTO `marsoft`.`msf_slj_familias_produtos` (`id`, `nome_familia_produtos`, `cod_familia_produtos`) VALUES ('10', 'Teste', 'TES');""
#sql = "DELETE FROM teste WHERE id=1"

for num in range(0,1000):
  nome = f"Marcio_{num}"
  email = f"marcio_{num}@teste.com"
  sql = f"INSERT INTO teste (nome,email) VALUES ('{nome}','{email}')"
  print(sql)
  cur.execute(sql)

sql = "SELECT count(id) FROM usuarios"
cur.execute(sql)
cur

cnn.commit()
# (1,)
#INSERT INTO `marsoft`.`msf_slj_familias_produtos` (`id`, `nome_familia_produtos`, `cod_familia_produtos`) VALUES ('10', 'Teste', 'TES');

