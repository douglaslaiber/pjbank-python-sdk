#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pjbank.contadigital import ContaDigital


class Transacoes(ContaDigital):
    """docstring for Transacoes."""

    def __init__(self, credencial=None, chave=None):
        super(Transacoes, self).__init__(credencial, chave)

    def nova_transacao(self, dados):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._post(['transacoes'], headers, dados)
        return response.json()

    def detalhes(self, id_operacao):
        headers = self.headers_chave
        headers.update(self.headers_content)
        response = self._get(['transacoes', id_operacao], headers)
        return response.json()
