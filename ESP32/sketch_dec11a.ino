
#include <WiFi.h>
#include <Arduino.h>
#include <PubSubClient.h>
#include "DHT.h"

int dht11_pin = 23;          //dht11  // Humidity //Temperature
int air_quality_pin = 32;    //mq2 // air_quality



WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);
char *mqttServer = "broker.hivemq.com";
int mqttPort = 1883;

void setupMQTT() {
  mqttClient.setServer(mqttServer, mqttPort);
  //mqttClient.setCallback(callback);
}

void reconnect() {
  Serial.println("Connecting to MQTT Broker...");
  while (!mqttClient.connected()) {
    Serial.println("Reconnecting to MQTT Broker..");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);

    if (mqttClient.connect(clientId.c_str())) {
      Serial.println("Connected.");
      mqttClient.subscribe("humidity/33445566");
      mqttClient.subscribe("temperature/33445566");
      mqttClient.subscribe("air/quality/33445566");
      mqttClient.subscribe("pre/humidity/33445566");
      delay(2000);

    }
  }
}




DHT dht(dht11_pin, DHT11);

const char* ssid = "SSID";
const char* password = "Password";

unsigned long previousMillis = 0;
unsigned long interval = 30000;

void initWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi ..");

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
}


void setup() {
  Serial.begin(19200);

  initWiFi();
  dht.begin();
  setupMQTT();
  pinMode(air_quality_pin, INPUT);


}

void loop() {
  unsigned long currentMillis = millis();
  if ((WiFi.status() != WL_CONNECTED) && (currentMillis - previousMillis >= interval)) {
    WiFi.disconnect();
    previousMillis = currentMillis;

    if (WiFi.status() != WL_CONNECTED) {
      initWiFi();

    }

    setupMQTT();
    if (!mqttClient.connected())
      reconnect();
    mqttClient.loop();
  }

  //start coding
  else {


    if (!mqttClient.connected())
      reconnect();
    mqttClient.loop();

    float Humidity = dht.readHumidity();
    float Temperature = dht.readTemperature();

    if (isnan(Humidity) || isnan(Temperature)) {

      Serial.println(F("Failed to read from DHT sensor!"));
      return;
    }
    Serial.print(F("original Humidity: "));
    Serial.print(Humidity);
    Serial.print(F("%  Temperature: "));
    Serial.print(Temperature);
    Serial.println(F("°C "));

    char Humidity_str[8];
    dtostrf(Humidity, 1, 2, Humidity_str);
    mqttClient.publish("humidity/33445566", Humidity_str);


    char Temperature_str[8];
    dtostrf(Temperature, 1, 2, Temperature_str);
    mqttClient.publish("temperature/33445566", Temperature_str);


    float air_quality = (analogRead(air_quality_pin));
    Serial.print(F("AIR: "));
    Serial.println(air_quality);
    char air_quality_str[8];
    dtostrf(air_quality, 1, 2, air_quality_str);
    mqttClient.publish("air/quality/33445566", air_quality_str);
    delay(1000);
    

    long double pred_humi = ((-1.2504109682152187 * Temperature) + (-1989.4947530261543 * (air_quality/10000)) + 126.70601295195848);
    Serial.print("predicted humidity : ");
    char pred_humi_chr[8];
    dtostrf(pred_humi, 1, 2, pred_humi_chr);
    mqttClient.publish("pre/humidity/33445566", pred_humi_chr);
    Serial.println(pred_humi_chr);
    
    Serial.println(F("............................................"));
    delay(1000);
  }



}

void callback(char* topic, char * message, unsigned int length) {
  Serial.print("Callback - ");
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
  }
}
