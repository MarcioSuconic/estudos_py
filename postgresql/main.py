from manage_sql import POSTGRESQL

key_personal_api ="xau_WRAvk8hyv6cju9Z2qpihDAgic6MNwyhk5"
#"xau_Fphbi636QbNxc4GKM5F81mZ0VpbE2Wyk"
post_url = f"postgresql://k04237:{key_personal_api}@us-east-1.sql.xata.sh/marsoft:main?sslmode=require"

print(post_url)

db = POSTGRESQL(
    postgre_url=post_url
    )

db.create_table(tablename="usuarios",
                columns=[db.Column(name='nome', column_type=db.Column_types.Char(255).varchar),
                        db.Column(name='email', column_type=db.Column_types.Char(255).varchar)])
                        
print(db.select_data("usuarios",["email"]))