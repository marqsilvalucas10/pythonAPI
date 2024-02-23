
dados = [
    {"nome":"Bruno","cidade":"Viana"},
    {"nome":"Guido", "cidade":"Amsterdan"}

]

template = """\
	<html>
        <body>
            <ul>
                <li>Nome:{dados[nome]}</li>
                <li>Nome:{dados[cidade]}</li>

            </ul>        

    	</body>
    </html>
"""
#renderizar

for item in dados:
    print(template.format(dados=item))


