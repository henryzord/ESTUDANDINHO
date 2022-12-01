import flask

def main():
    app = flask.Flask(
        'Meu Servidor',
        template_folder='templates',
        static_folder='static'
    )

    @app.route('/', methods = ['GET'])
    def main_page():
        return flask.render_template(
            'template3.html',
             meu_novo_paragrafo='<p>Brasil espanca Sérvia</p>'
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