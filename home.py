class Home():
    """
    Allow us to generate API Main Page.
    """
    def home(self):
        paths = [
            {
                'titulo': 'Todas os cartões',
                'definicao': 'Mostrar todos os cartões existentes na DB',
                'link': '/acessos',
                'argumento': "None"
            },
            {
                'titulo': 'Todos os acessos por casa',
                'definicao': 'Mostrar todas os cartões com acesso a uma determinada casa',
                'link': '/acessos/<home>',
                'argumento': 'Número da casa, p.e, 1'
            },
            {
                'titulo': 'Acessos válidos por casa',
                'definicao' : 'Verifica se um cartão é valido para uma dara casa',
                'link' : '/isValid/<home>/<card_id>',
                'argumento' : 'Home, p.e, 1; Card_id, p.e, 01234567'
            }
        ]
        return paths