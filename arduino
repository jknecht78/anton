void setup() {
  // Start the serial connection
  Serial.begin(115200);
}

void loop() {
  // Check if data is available to read
  if (Serial.available()) {
    // Read the incoming byte
    String incoming_message = Serial.readStringUntil('\n');
    
    // Print the incoming message
    Serial.println("Received from Raspberry Pi: " + incoming_message);
    
    // Send a reply back to the Raspberry Pi
    Serial.println("Hello from Arduino!");
  }
}
