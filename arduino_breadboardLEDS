int LED1 = 9;
int LED2 = 11;

void setup() {
    pinMode(LED1, OUTPUT);
  	pinMode(LED2, OUTPUT);
}

void loop() {
  for (int i = 0; i < 5; i++){
  	digitalWrite(LED1, HIGH);
  	delay(500);
  	digitalWrite(LED1, LOW);
  	delay(500);
  }
  for (int i = 0; i < 3; i++){
  	digitalWrite(LED2, HIGH);
  	delay(500);
  	digitalWrite(LED2, LOW);
  	delay(500);
  }
  for (int br = 255; br >= 0; br--){
  	analogWrite(LED1, br);
    analogWrite(LED2, br);
    delay(5);
  }
  delay(1000);
}
