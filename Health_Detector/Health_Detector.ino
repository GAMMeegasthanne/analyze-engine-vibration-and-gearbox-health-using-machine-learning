const int greenLedPin = 13;
const int redLedPin = 12;

void setup() {
  pinMode(greenLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == 'R') {
      digitalWrite(greenLedPin, LOW);
      digitalWrite(redLedPin, HIGH);
    } else if (command == 'G') {
      digitalWrite(redLedPin, LOW);
      digitalWrite(greenLedPin, HIGH);
    }
  }
}
