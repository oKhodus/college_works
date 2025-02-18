int ledPins[] = {3, 6, 9, 11};
int states[4];

void setup() {
  	Serial.begin(9600);
  	
    for (int i = 0; i < 4; i++) {
        pinMode(ledPins[i], OUTPUT);
    }
}

void loop() {
    Serial.println("Enter a number (0-15):");
    
    while (Serial.available() == 0) {
    }

    int number = Serial.parseInt();  
    

    if (number < 0 || number > 15) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 4; j++) {
                digitalWrite(ledPins[j], HIGH);
            }
            delay(500);
            for (int j = 0; j < 4; j++) {
                digitalWrite(ledPins[j], LOW);
            }
            delay(500);
        }
        return;
    }

    for (int i = 0; i < 4; i++) {
        states[i] = (number >> i) & 1;
    }

    for (int i = 0; i < 4; i++) {
        if (states[i] == 1) {
            digitalWrite(ledPins[i], HIGH);
        } else {
            digitalWrite(ledPins[i], LOW);
        }
    }
    
    delay(1000);
}
