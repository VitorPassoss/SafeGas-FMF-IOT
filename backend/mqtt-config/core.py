import paho.mqtt.client as mqtt
import time
import websocket
import json

class HandleConnect:
    SENSOR_GAS = "IOT/FMF/SENSORGAS"
    TEMP_UMID = "IOT/FMF/TEMP/HUMIDADE"
    SENSOR_PESO = "IOT/FMF/SENSORCARGA"

    def on_connect(self, client, userdata, flags, rc):
        print("Conectado ao broker MQTT com código de resultado: " + str(rc))
        # Inscreva-se em um tópico para receber mensagens
        client.subscribe(self.SENSOR_GAS)
        client.subscribe(self.TEMP_UMID)
        client.subscribe(self.SENSOR_PESO)

    def on_message(self, client, userdata, msg):
        print("Nova mensagem recebida no tópico " + msg.topic + ": " + str(msg.payload))

        obj_resolver = self.format_received(msg.topic, msg.payload)

        print(obj_resolver)

        # Converte o objeto diretamente para uma string JSON
        payload_json = json.dumps(obj_resolver)

        ws.send(payload_json)

    def format_received(self, topic, payload):
        if topic == self.SENSOR_GAS:
            formated_value = payload.decode('utf-8').replace('b', '')
            formated_value = int(formated_value)

            if formated_value > 900:
                obj_send = {
                    'sensorGas': formated_value,
                    'vazamento': True
                }
            else:
                obj_send = {
                    'sensorGas': formated_value,
                    'vazamento': False
                }
            return obj_send

        if topic == self.TEMP_UMID:
            # Convertendo payload de bytes para string e removendo 'b'
            payload_str = payload.decode('utf-8').replace('b', '')

            valores = payload_str.split(',')

            temperatura = float(valores[0])
            umidade = float(valores[1])

            obj_send = {
                'temperatura': temperatura,
                'umidade': umidade
            }

            return obj_send
        
        if topic == self.SENSOR_PESO:
            formated_value = payload.decode('utf-8').replace('b', '')
            try:
                peso_float = float(formated_value)
                

                if peso_float < 0:
                    peso_float = 0
                

                # peso_float = round(peso_float - 9.000, 3)

                obs_send = {
                    'quantidade_peso':peso_float
                }
                print(peso_float)
                return obs_send
            except ValueError:
                print("Erro: A string não representa um número válido.")




handler = HandleConnect()

client = mqtt.Client()
client.on_connect = handler.on_connect
client.on_message = handler.on_message

client.connect("test.mosquitto.org", 1883, 60)
ws = websocket.WebSocket()
ws.connect("ws://localhost:8000/ws/iot")

client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando o cliente MQTT...")
    client.loop_stop()
    client.disconnect()
