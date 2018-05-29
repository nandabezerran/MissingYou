import psycopg2

def connect_db():
	conexao = psycopg2.connect(
		database= "MissingYouBanco", 
		user="Missingyouufc", 
		password="Missingyouufc2018",
		host="missingyoudb.ce2hc9ksfuzl.sa-east-1.rds.amazonaws.com", 
		port="5432"
	)

	return conexao