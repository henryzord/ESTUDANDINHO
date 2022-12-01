import sqlite3

import flask

def main():
    app = flask.Flask(
        'Meu Servidor',
        template_folder='templates',
        static_folder='static'
    )

    @app.route('/', methods = ['GET'])
    def main_page():
        with sqlite3.connect('static/database/test.db') as con:
            cur = con.cursor()
            # retorna uma lista de tuplas
            answer = cur.execute('SELECT valor, nome FROM jogadores;').fetchall()
            texto_do_seletor = []
            for line in answer:
                texto_do_seletor.append(
                    '<option value="{0}">{1}</option>'.format(
                        line[0], line[1]
                    )
                )
            texto_do_seletor = '\n'.join(texto_do_seletor)

        return flask.render_template(
            'template3.html',
            meu_novo_paragrafo='<p>Brasil espanca Sérvia</p>',
            meu_seletor=texto_do_seletor

        )

    @app.route('/copa', methods=['GET'])
    def pagina_da_copa():
        return flask.render_template(
            'template4.html',
            meu_novo_paragrafo='<p>Brasil espanca Sérvia</p>'
        )

    @app.errorhandler(404)
    def page_not_found(page):
        return flask.render_template('template404.html'), 404


    @app.route('/jogadores', methods=['POST'])
    def jogadores():
        jogador = flask.request.form.get('selecionado')
        print('o jogador selecionado foi', jogador)

        response = flask.jsonify({'jogador':"Richarlison"})
        response.headers.add('Acess-Control-Allow-Origin', '*')
        return response

    app.register_error_handler(404, page_not_found)      
        
    app.run(debug = True)


if __name__ == '__main__':
    main()