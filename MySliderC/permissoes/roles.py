from rolepermissions.roles import AbstractUserRole


class Administrador(AbstractUserRole):
    available_permissions = {'acesso_total': True}


class OperadorMarketing(AbstractUserRole):
    available_permissions = {'editar_grade': True,
                             'criar_grade': True, 'deletar_grade': True, }
    
class Usuario(AbstractUserRole):
    available_permissions = {'redefinir_senha': True,
                             'manter_usuário': True, 'logar_sistema': True,
                              'autocadastro':True, 'adicionar_conteúdo':True,
                               'editar_grade_do_setor': True }
