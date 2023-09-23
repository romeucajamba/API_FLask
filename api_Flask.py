"""
Rest é um modelo para projetar arquiteturas de software baseado em comunicação
via rede.
Rest significa - Representational State Transfer - Transferência de Estado
Representacional.

Rest projeta a ideia de que todo recurso deveria responder aos mesmos métodos.
Mas ela acaba sendo apenas uma arquitetura, modo de aplicar as API e serviços webs.


Rest API é uma Api desenvolvida para utilizando os princípios da arquitetura Rest

Um Rest API é utilizado na comunicação/integração entre software através de serviços web.

Rest API é consumido através de requisições HTTP.

Rest API são geralmente representadas em seus formatos por JSON e XML, também são usadas páginas HTML
PDF e arquivos de imagens.

Ao implementar um Rest API, cada método deve ser responsável por um tipo diferente
de ação. Exemplo: Consulta, Alteração, Inclusão e Exclusão.

"""
"""
                    Métodos do protocolo HTTP
                    
Get - Método que solicita recurso, registros ou objeto do servidor por meio da URL
Nós usamos quando estmos buscando algo do servidor.
    
Post - Método usado para envio de arquivo/dados ou formulário HTML para o servidor.

Put - Aceita criar ou modificar um objeto do servidor

Delete _ Informa por meio da URL o objeto a ser deletado.    
"""

"""
URL - Uniform Resource Locator - Localizador de Recursos Universal ... Host que será acessado
Ex: apexiomCode.ao

URN - Uniform Resource Name - Nome do Recurso universal... Recurso que será identificado
Ex: /category/blog/

URI - Uniform Resource Identifier - Identificador de Recursos Universal... Identificador do recurso pode ser uma imagem
arquivo uma página EX: https://apexiomCode.com/category/blog
o URI une o protocolo URL e URN

Extensible Markup Language - A linguagem de marcação utilizado para compartilhamento de informações através de requisições 
"""