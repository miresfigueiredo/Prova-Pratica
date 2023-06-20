from flask import Flask, render_template, request, redirect

app = Flask(__name__)

disciplinas = []

@app.route('/')
@app.route('/listar_disciplinas')
def listar_disciplinas():
    return render_template('listar_disciplinas.html', disciplinas=disciplinas)

@app.route('/cadastrar_disciplina', methods=['GET', 'POST'])
def cadastrar_disciplina():
    if request.method == 'POST':
        
        disciplina = {
            'id': len(disciplinas)+1,
            'nome': request.form['disciplina'],
            'cargahoraria': request.form['cargahoraria'],
            'conteudo': request.form['conteudo']
        }
        disciplinas.append(disciplina)
        
        return redirect('/')
    return render_template('cadastrar_disciplina.html')

@app.route('/editar_disciplina/<int:id>', methods=['GET', 'POST'])
def editar_disciplina(id):
    for disciplina in disciplinas:
        if disciplina['id'] == id:
            if request.method == 'POST':
                disciplina['nome'] = request.form['disciplina']
                disciplina['cargahoraria'] = request.form['cargahoraria']
                disciplina['conteudo'] = request.form['conteudo']
                return redirect('/')
            return render_template('editar_disciplina.html', disciplina=disciplina)
    return redirect('/listar_disciplinas')

@app.route('/excluir_disciplina/<int:id>')
def excluir_disciplina(id):
    for disciplina in disciplinas:
        if disciplina['id'] == id:
            disciplinas.remove(disciplina)
            break
    return redirect('/listar_disciplinas')

if __name__ == '__main__':
    app.run(debug=True)
