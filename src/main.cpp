#include <Arduino.h>

#define LED_PIN 2

unsigned long lastBlink = 0;
const unsigned long BLINK_INTERVAL = 500;
bool ledState = false;
int blinkCount = 0;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("ESP32 PlatformIO Demo - Version 2 (non-blocking)");
}

void loop() {
  if (millis() - lastBlink >= BLINK_INTERVAL) {
    lastBlink = millis();
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
    blinkCount++;

    Serial.print("Blink #");
    Serial.print(blinkCount);
    Serial.print(" | LED = ");
    Serial.println(ledState ? "ON" : "OFF");
  }
}
