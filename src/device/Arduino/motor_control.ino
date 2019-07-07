#define DIR_A 12
#define DIR_B 13

#define BRK_A 9
#define BRK_B 8

#define GO_A 3
#define GO_B 11


int x;

void setup() {

  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  
  //Setup Channel A
  pinMode(DIR_A, OUTPUT); //Initiates Motor Channel A pin
  pinMode(BRK_A, OUTPUT); //Initiates Brake Channel A pin

  //Setup Channel B
  pinMode(DIR_B, OUTPUT); //Initiates Motor Channel A pin
  pinMode(BRK_B), OUTPUT);  //Initiates Brake Channel A pin
  
}

void idle() {

}

void loop(){

  /*if (Serial.available() > 0) {
        incoming = Serial.read();
        Serial.print("I received: ");
        Serial.println(incoming);
  }
        switch (incoming)
        {
        case 'D':
          Serial.println("Destra");
          break;
        case 'A':
          Serial.println("Sinistra");
          break;
        case 'W':
          Serial.println("Su");
          //Motor A forward @ full speed
          digitalWrite(12, HIGH); //Establishes forward direction of Channel A
          digitalWrite(9, LOW);   //Disengage the Brake for Channel A
          analogWrite(3, 255);   //Spins the motor on Channel A at full speed

          //Motor B forward @ full speed
          digitalWrite(13, LOW);  //Establishes backward direction of Channel B
          digitalWrite(8, LOW);   //Disengage the Brake for Channel B
          analogWrite(11, 255);    //Spins the motor on Channel B at full speed

          delay(3000);

          digitalWrite(9, HIGH);  //Engage the Brake for Channel A
          digitalWrite(8, HIGH);  //Engage the Brake for Channel B

          break;
        case 'S':
          Serial.println("Giu");
          //Motor A backward @ full speed
          digitalWrite(12, LOW); //Establishes forward direction of Channel A
          digitalWrite(9, LOW);   //Disengage the Brake for Channel A
          analogWrite(3, 255);   //Spins the motor on Channel A at full speed

          //Motor B backward @ full speed
          digitalWrite(13, HIGH);  //Establishes backward direction of Channel B
          digitalWrite(8, LOW);   //Disengage the Brake for Channel B
          analogWrite(11, 255);    //Spins the motor on Channel B at full speed

          delay(3000);

          digitalWrite(9, HIGH);  //Engage the Brake for Channel A
          digitalWrite(8, HIGH);  //Engage the Brake for Channel B

          break;
        
        default: {
          
          Serial.println("IDLE");

          digitalWrite(12, LOW); //Establishes forward direction of Channel A
          digitalWrite(9, LOW);   //Disengage the Brake for Channel A
          analogWrite(3, 122);   //Spins the motor on Channel A at full speed

          digitalWrite(13, HIGH);  //Establishes backward direction of Channel B
          digitalWrite(8, LOW);   //Disengage the Brake for Channel B
          analogWrite(11, 122);    //Spins the motor on Channel B at full speed

          break;
        }
        }
  
  //Motor A forward @ full speed
  digitalWrite(12, HIGH); //Establishes forward direction of Channel A
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  analogWrite(3, 255);   //Spins the motor on Channel A at full speed

  //Motor B backward @ half speed
  digitalWrite(13, LOW);  //Establishes backward direction of Channel B
  digitalWrite(8, LOW);   //Disengage the Brake for Channel B
  analogWrite(11, 123);    //Spins the motor on Channel B at half speed

  
  delay(3000);

  
  digitalWrite(9, HIGH);  //Engage the Brake for Channel A
  digitalWrite(9, HIGH);  //Engage the Brake for Channel B


  delay(1000);
  
  
  //Motor A forward @ full speed
  digitalWrite(12, LOW);  //Establishes backward direction of Channel A
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  analogWrite(3, 123);    //Spins the motor on Channel A at half speed
  
  //Motor B forward @ full speed
  digitalWrite(13, HIGH); //Establishes forward direction of Channel B
  digitalWrite(8, LOW);   //Disengage the Brake for Channel B
  analogWrite(11, 255);   //Spins the motor on Channel B at full speed
  
  
  delay(3000);
  
  
  digitalWrite(9, HIGH);  //Engage the Brake for Channel A
  digitalWrite(9, HIGH);  //Engage the Brake for Channel B
  
  
  delay(1000);
  */

if (Serial.available() > 2) {

  x = Serial.read() << 8;
  x |= Serial.read();

  Serial.write(x);

  ratio = x/640;

  //Motor A forward @ full speed
  digitalWrite(12, HIGH);           //Establishes backward direction of Channel A
  digitalWrite(9, LOW);             //Disengage the Brake for Channel A
  analogWrite(3, 255*ratio);        //Spins the motor on Channel A at half speed
  
  //Motor B forward @ full speed
  digitalWrite(13, HIGH);           //Establishes forward direction of Channel B
  digitalWrite(8, LOW);             //Disengage the Brake for Channel B
  analogWrite(11, 255*(1-ratio));   //Spins the motor on Channel B at full speed

}

else idle();

}
