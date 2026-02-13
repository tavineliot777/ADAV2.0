from rest_framework.test import APITestCase
from .models import Osso

class OssoBuscaTeste(APITestCase):

    def setUp(self):
        
        self.osso = Osso.objects.create(
            nome="femurTeste",
            descricao="Descrição teste..."
        )

    def test_buscar_osso_existente(self):
        
        dados = {"nome": "femurTeste", "descricao" : "Descrição teste..."}
        response = self.client.post('/api/osso/procurar_osso/',
            data=dados, 
            format='json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["nome"], "femurTeste")
        
        print("Teste de buscar_osso status=200 passou!")

    def test_buscar_osso_inexistente(self):
        dados = {"nome": "Costela"}
        response = self.client.post(
            '/api/osso/procurar_osso/', 
            data=dados, 
            format='json'
        )

        self.assertEqual(response.status_code, 404)
        
        print("Teste de buscar_osso status=404 passou!")

    def test_osso_Listar_Primeiro(self):

        response = self.client.get('/api/osso/listar/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['nome'], "femurTeste")
            
        print("Teste de osso_listar_Primeiro status=200 passou!")

    def test_osso_Listar_Todos(self):

        response = self.client.get("/api/osso/listar_todos/")
        self.assertEqual(response.status_code)




    def test_osso_Atualizar(self):
        
        dados = {"nome" : "femur2", "descricao": "descrição2..."}
        response = self.client.put(f'/api/osso/atualizar/{self.osso.id}/' , data=dados, format="json")

        self.assertEqual(response.status_code, 200)
        print("Teste de atualizar_osso status=200 Passou!")
    
    def test_osso_AtualizarExcept(self):

        dados = {"nome" : "femur2", "descricao" : "descrição2..."}
        id = 100
        response = self.client.put(f"/api/osso/atualizar/{id}/",data=dados, format="json")

        self.assertEqual(response.status_code, 404);
        print("Teste de atualizar_osso status=404 passou!");
    
    def test_deletar_osso(self):

        response = self.client.delete(f"/api/osso/deletar/{self.osso.id}/")
        self.assertEqual(response.status_code, 200)
        print("Teste de deletar status=200 passou!");
    
    def test_deletar_osso_except(self):
        id = 1033
        response = self.client.delete(f"/api/osso/deletar/{id}/")
        self.assertEqual(response.status_code, 404)
        print("Teste de deletar status=404 passou!")

    def test_criar_osso(self):
        dados = {"nome" : "qualquerNome", "descricao" : "seila..."}
        response = self.client.post("/api/osso/criar/", data=dados, format="json")
        self.assertEqual(response.status_code, 200)
        print("Teste de criar_osso status=200 passou!");
    
