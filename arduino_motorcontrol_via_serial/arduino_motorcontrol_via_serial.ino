#include <string.h>
char inData[80];
byte index = 0;
int comPwm;
int comBrake;
int comDir;
int comSpeed;

const int pwmA = 3;
const int pwmB = 11;
const int brakeA = 9;
const int brakeB = 8;
const int dirA = 12;
const int dirB = 13;

void setup()
{
Serial.begin(9600);

//Setup Channel A
pinMode(dirA, OUTPUT); //Initiates Motor Channel A pin
pinMode(brakeA, OUTPUT); //Initiates Brake Channel A pin

//Setup Channel B
pinMode(dirB, OUTPUT); //Initiates Motor Channel A pin
pinMode(brakeB, OUTPUT); //Initiates Brake Channel A pin

// motor stopp
digitalWrite(dirA, LOW);
digitalWrite(dirB, LOW);
digitalWrite(brakeA, HIGH);
digitalWrite(brakeB, HIGH);
analogWrite(pwmA, 0);
analogWrite(pwmB, 0);
}

void loop()
{
   while(Serial.available() > 0)
   {
	char aChar = Serial.read();
	if(aChar == '\n' || index == 6)
	{
                // befehlsauswertung anfang
                // motor setzen
                int comPwm = 11;
                int comBrake = 8;
                int comDir = 13;
                  
                int serMotor = inData[0];
                if(serMotor == 0) {
                  comPwm = 3;
                  comBrake = 9;
                  comDir = 12;
                }
                Serial.print("Motor:");
                Serial.print(comPwm);
                Serial.print(",");
                Serial.print(comBrake);
                Serial.print(",");
                Serial.print(comDir);
                
                // richtung setzen
                int serDirection = inData[1];
                if(serDirection == 0) {
                  digitalWrite(comDir, LOW);
                } else {
                  digitalWrite(comDir, HIGH);
                }
                
                // bremse setzen
                int serBrake = inData[2];
                if(serBrake == 0) {
                  digitalWrite(comBrake, LOW);
                } else {
                  digitalWrite(comBrake, HIGH);
                }
                
                // geschwindigkeit setzen
                int comSpeed = inData[3]*100 + inData[4]*10 + inData[5];
                Serial.print(";Speed:");
                Serial.println(comSpeed);
                analogWrite(comPwm, comSpeed);
                
                // befehlsauswertung ende



	   index = 0;
	   inData[index] = NULL;
	    
	}
	else
	{
	   inData[index] = aChar-48;
	   index++;
	   inData[index] = '\0'; // Keep the string NULL terminated
	}
   }
}
 
