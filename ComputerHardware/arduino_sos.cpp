// C++ code
//
int dot = 100;
int dash = 300;
int d_dot = 100;
int d_dash = 100;
int new_start = 400;

void setup()
{
  pinMode(13, OUTPUT);
}

void loop()
{
  for (int i = 0; i < 3; i++){
    digitalWrite(13, HIGH);
    delay(dot);
    digitalWrite(13, LOW);
    delay(d_dot);

  }
  for (int i = 0; i < 3; i++){
    digitalWrite(13, HIGH);
    delay(dash);
    digitalWrite(13, LOW);
    delay(d_dash);

  }
  for (int i = 0; i < 3; i++){
    digitalWrite(13, HIGH);
    delay(dot);
    digitalWrite(13, LOW);
    delay(d_dot);

  }
  
  delay(new_start);
}
