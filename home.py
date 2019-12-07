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
            }
        ]
        return paths