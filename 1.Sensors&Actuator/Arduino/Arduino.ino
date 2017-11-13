#include <Time.h>
#include <TimeLib.h>

#include <TimedAction.h>

#include <ArduinoJson.h>

#include <IRremote.h>
#include <IRremoteInt.h>

#include <SR04.h>
#define TRIG_PIN 12
#define ECHO_PIN 11
SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);

//#include <SimpleDHT.h> int pinDHT11 = 2; SimpleDHT11 dht11;
#include <DHT.h>
DHT dht;

int lightPin = 2;

const int SW_pin = 4; // digital pin connected to switch output
const int X_pin = 0; // analog pin connected to X output
const int Y_pin = 1; // analog pin connected to Y output

int latchPin = 9; // connect to the ST_CP of 74HC595 (pin 3,latch pin)
int clockPin = 10; // connect to the SH_CP of 74HC595 (pin 4, clock pin)
int dataPin = 8; // connect to the DS of 74HC595 (pin 2)



/*全局变量*/
long ti=1351824120;
int ir=1;
int di=311;
int te=1;
int hu=2;
int li=999;
int x=888;
int y=-999;
int s=0;


/*构建缓冲区并生成JSON*/
void jsonBuffer(unsigned long ti, int di, int te, int hu, int li) {
StaticJsonBuffer<66> jsonBuffer;
//const int BUFFER_SIZE1 = JSON_OBJECT_SIZE(6); 64
JsonObject& rootB = jsonBuffer.createObject();
rootB["Triger"] =0;
rootB["Time"] =ti;
rootB["Distance"] =di;
rootB["Temperature"] =te;
rootB["Humity"] =hu;
rootB["Light"] =li;
//rootB.prettyPrintTo(Serial);
rootB.printTo(Serial);
Serial.println();
}

void joyStick(int swich,int x, int y,int power,int ir){
StaticJsonBuffer<77> joyStick;
//const int BUFFER_SIZE2 = JSON_OBJECT_SIZE(5) + JSON_ARRAY_SIZE(2); 74
JsonObject& rootS = joyStick.createObject();
rootS["Triger"] =1;
rootS["IR"] =ir;
rootS["Swich"] =swich;
rootS["Power"] = power;
JsonArray& Stick= rootS.createNestedArray("Stick");
Stick.add(x);
Stick.add(y);
//rootS.prettyPrintTo(Serial);
rootS.printTo(Serial);
Serial.println();
}
/*===============================================*/
/*个位数显*/
byte seven_seg_digits[23] =   { 
                            B11111100,  // = 0      0
                            B01100000,  // = 1      1
                            B11011010,  // = 2      2
                            B11110010,  // = 3      3
                            B01100110,  // = 4      4
                            B10110110,  // = 5      5
                            B10111110,  // = 6      6
                            B11100000,  // = 7      7
                            B11111110,  // = 8      8
                            B11110110,  // = 9      9
                            B00001110,  // = |-     10
                            B01100010,  // = -|     11
                            B10001100,  // = ┌     12
                            B00011100,  // = └     13
                            B10000000,  // = ┬     14
                            B00010000,  // = ┴     15
                            B11001110,  // = p      16
                            B11001111,  // = p.     17
                            B11100110,  // = q      18
                            B11000110,  // = o     19
                            B10011110,   // = E     20
                            B11011110, // = e    21
                            B11111111  // = 8.   22
                             };

void sevenSegWrite(byte digit) {
  digitalWrite(latchPin, LOW); // set the latchPin to low potential, before sending data
  shiftOut(dataPin, clockPin, LSBFIRST, seven_seg_digits[digit]);     // the original data (bit pattern)
  digitalWrite(latchPin, HIGH);   // set the latchPin to high potential, after sending data
}


/*===============================================*/
/*IR控制模块*/
int receiver = 13; // Signal Pin of IR receiver to Arduino Digital Pin 13
/*-----( Declare objects )-----*/
IRrecv irrecv(receiver);     // create instance of 'irrecv'
decode_results results;      // create instance of 'decode_results'

int transIR() // takes action based on IR code received
{

  switch(results.value)
  {
  case 0xFFA25D: {sevenSegWrite(17); return 1;    }    //break; //Serial.println("POWER")
  case 0xFFE21D: {sevenSegWrite(18); return 2;    }    //break; //Serial.println("FUNC/STOP")
  case 0xFF629D: {sevenSegWrite(14); return 3;    }    //break; //Serial.println("VOL+"); 
  case 0xFF22DD: {sevenSegWrite(10); return 4;    }    //   break; //Serial.println("FAST BACK");
  case 0xFF02FD: {sevenSegWrite(16); return 5;    }    //   break; //Serial.println("PAUSE");
  case 0xFFC23D: {sevenSegWrite(11); return 6;    }    //  break; //Serial.println("FAST FORWARD");
  case 0xFFE01F:  {sevenSegWrite(13); return 7;   }    //   break; //Serial.println("DOWN");
  case 0xFFA857: {sevenSegWrite(15); return 8;    }    //  break; //Serial.println("VOL-"); 
  case 0xFF906F: {sevenSegWrite(12); return 9;    }    //  break; //Serial.println("UP"); 
  case 0xFF9867: {sevenSegWrite(20); return 10;   }    //    break; //Serial.println("EQ");
  case 0xFFB04F:  {sevenSegWrite(21); return 11;  }    //    break; //Serial.println("ST/REPT");
  case 0xFF6897:  {sevenSegWrite(0); return 12;  }    //   break;  //Serial.println("0");
  case 0xFF30CF:  {sevenSegWrite(1); return 13;  }    //   break; // Serial.println("1");
  case 0xFF18E7:  {sevenSegWrite(2); return 14;  }    //    break; //Serial.println("2");
  case 0xFF7A85:  {sevenSegWrite(3); return 15;  }    //   break; //Serial.println("3");
  case 0xFF10EF:  {sevenSegWrite(4); return 16;  }    //    break; //Serial.println("4");
  case 0xFF38C7:  {sevenSegWrite(5); return 17;  }    //    break; //Serial.println("5");
  case 0xFF5AA5:  {sevenSegWrite(6); return 18;  }    //    break; //Serial.println("6");
  case 0xFF42BD:  {sevenSegWrite(7); return 19;  }    //    break; //Serial.println("7");
  case 0xFF4AB5:  {sevenSegWrite(8); return 20;  }    //    break; // Serial.println("8");
  case 0xFF52AD:  {sevenSegWrite(9); return 21;  }    //    break; //Serial.println("9");
  case 0xFFFFFFFF: {sevenSegWrite(19);return 22;  }    //   break;  //Serial.println(" REPEAT")
  //default: 
    {sevenSegWrite(22);return 0;} //Serial.println(" other button   ");irrecv.resume();
  }
}

/*===============================================*/
/*温度和湿度
int detTH(){
  byte temperature = 0;
  byte humidity = 0;
  byte data[40] = {0};
  if (dht11.read(pinDHT11, &temperature, &humidity, data)) {
    Serial.print("Read DHT11 failed");
    return;
  }
  hu=data[0]*128+data[1]*64+data[2]*32+data[3]*16+data[4]*8+data[5]*4+data[6]*2+data[7];
  te=data[16]*128+data[17]*64+data[18]*32+data[19]*16+data[20]*8+data[21]*4+data[22]*2+data[23];
}
*/

void detTH()

{

  //delay(dht.getMinimumSamplingPeriod());
  hu=dht.getHumidity();
  te=dht.getTemperature();

}




/*===============================================*/
/*亮度*/
int detlight()
{
  int lig=analogRead(lightPin);
  return lig;
}

/*===============================================*/
/*模拟控制器*/

int detX()
{
  int xaxis=analogRead(X_pin);
  return xaxis;
}

int detY()
{
  int yaxis=analogRead(Y_pin);
  return yaxis;
}
int detSw()
{
  int sw=digitalRead(SW_pin);
  return sw;
}
/*===============================================*/
/*油门控制器*/

int power()
{
  int power = analogRead(A3);
  return power-9;
}

/*===============================================*/
/*多任务*/
void sensor()
{
    detTH();
    di=sr04.Distance();
    li=detlight();
    jsonBuffer(now(),di,te,hu,li);
}

void control()
{
    if (irrecv.decode(&results))
    {
      ir=transIR(); 
    }
    else ir=0;
    joyStick(detSw(),detX(),detY(),power(), ir);
    irrecv.resume();
}

TimedAction sensorThread = TimedAction(5000,sensor);
TimedAction controlThread = TimedAction(100,control);

/*===============================================*/
/*主程序开始*/

void setup() {
irrecv.enableIRIn();

pinMode(SW_pin, INPUT);
digitalWrite(SW_pin, HIGH);

pinMode(latchPin, OUTPUT);
pinMode(clockPin, OUTPUT);
pinMode(dataPin, OUTPUT);

dht.setup(2); // data pin 2
Serial.begin(9600);
while (!Serial) {} // wait serial port initialization
//jsonBuffer(1351824120,01,311,24,52,999);
//joyStick(1000, 999);
setTime(11,30,30,5,9,2017);
//setTime(hr,min,sec,day,month,yr);
}

void loop() {
    sensorThread.check();
    controlThread.check();
}
