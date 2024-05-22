import unittest
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
    
    def test_suma(self):
        # Enviar una solicitud POST al endpoint '/api/suma' con un JSON que contiene n1 y n2
        response = self.app.post('/api/suma', json={'n1': 5, 'n2': 3})
        
        # Verificar que la respuesta sea exitosa (código 200)
        self.assertEqual(response.status_code, 200)
        
        # Verificar que el resultado devuelto es el esperado
        self.assertEqual(response.data.decode('utf-8'), '8')
    
    def test_invalid_request(self):
        # Enviar una solicitud POST al endpoint '/api/suma' sin proporcionar n1 y n2
        response = self.app.post('/api/suma', json={})
        
        # Verificar que la respuesta sea un error (código 400)
        self.assertEqual(response.status_code, 400)
        
        # Verificar que el mensaje de error sea el esperado
        self.assertEqual(response.data.decode('utf-8'), 'Bad Request')

if __name__ == '__main__':
    unittest.main()
