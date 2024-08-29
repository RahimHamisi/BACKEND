#include <WiFi.h>
#include <DHT.h>
#include <HTTPClient.h>

// WiFi credentials
const char* ssid = "SODE_RIDC";          
const char* password = "mikazo.com";    


const char* serverName = "http:// 172.17.17.124:8000/graphql/"; 
String graphqlQuery = String("{ \"query\": \"mutation { createReading(input: {temperature: \\\"") +
                      String(temperature) + "\\\", humidity: \\\"" + String(humidity) +
                      "\\\"}) { reading { temperature, humidity, time } } }\" }";


#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

static unsigned long lastTime = 0;
static unsigned long timerDelay = 60; // Send data every 60 seconds

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if ((millis() - lastTime) > timerDelay) {
    float temperature = dht.readTemperature(); // Read temperature in Celsius

    if (isnan(temperature)) {
      Serial.println("Failed to read from DHT sensor!");
      return;
    }

    Serial.print("Temperature: ");
    Serial.println(temperature);

    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;

      String query = String(graphqlQuery);
      query.replace("%.2f", String(temperature, 2)); 

      Serial.print("Sending request to: ");
      Serial.println(serverName);
      Serial.print("Query: ");
      Serial.println(query);

      http.begin(serverName);
      http.addHeader("Content-Type", "application/json");

      // Send HTTP POST request
      int httpResponseCode = http.POST(query);

      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
      if (httpResponseCode > 0) {
        String response = http.getString();
        Serial.print("Response: ");
        Serial.println(response);
      } else {
        Serial.print("Error on sending POST: ");
        Serial.println(httpResponseCode);
        Serial.print("Error message: ");
        Serial.println(http.errorToString(httpResponseCode).c_str());
      }
      http.end();
    } else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }
}
