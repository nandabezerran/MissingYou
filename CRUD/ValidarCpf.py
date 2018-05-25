#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/missingYou/api/v1.0/validarCpf/<string:cpf>', methods=['GET'])
def validarCpf(cpf):
	if (len(cpf) == 11):
		# Calcular primeiro digito verificador
		sm = 0
		peso = 10
		for i in range(0, 9):
			sm = sm + (int(cpf[i]) * peso)
			peso = peso - 1
		primeiroDigito = 11 - (sm % 11)
		if ((primeiroDigito == 10) or (primeiroDigito == 11)):
			primeiroDigito = 0

		# calculo do segundo digito vefiricado
		sm = 0
		peso = 11
		for i in range(0, 10):
			sm = sm + (int(cpf[i]) * peso)
			peso = peso - 1

		segundoDigito = 11 - (sm % 11)
		if ((segundoDigito == 10) or (segundoDigito == 11)):
			segundoDigito = 0

		if ((primeiroDigito == int(cpf[9])) and (segundoDigito == int(cpf[10]))):
			return 'operacao foi realizada com sucesso',200
		else:
			return 'cpf invalido',412
	else:
		return 'cpf invalido',412

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)