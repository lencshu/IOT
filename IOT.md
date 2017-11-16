[TOC]

# 0.0 概况



```sequence
Title: The structure of Projet IOT
Sensors-->>Actionneur:Co-existe
Actionneur->Arduino:①Interface Numerique&Analogique
Sensors->Arduino:②Interface numerique&analogique
Arduino->Raspberry: ③Interface série
Raspberry->Drone: ④Bluetooth
Raspberry->Web: ⑤TCP-IP
Web-->Arduino: ⑥Commande
Web-->Raspberry: ⑦Commande
Web->>Wechat:⑧Mobile
```


```sequence
Title: 模块结构树
传感器-->>执行器:并存
执行器->Arduino下位机:①数字模拟接口
传感器->Arduino下位机:②数字模拟接口
Arduino下位机->树莓派: ③串口通信
树莓派->四轴: ④蓝牙通信
树莓派->Web: ⑤Web通信
Web-->Arduino下位机: ⑥执行命令
Web-->树莓派: ⑦控制脚本
Web->>微信:⑧移动端部署
```

控制流程图

```flow
st=>start: Start:>http://gliang.eu[http://gliang.eu]
e=>end:>http://gliang.eu
op1=>operation: 下位机传感器收集数据
op2=>operation: 树莓派Django数据库收集并处理数据
op3=>inputoutput: Web页面显示数据
op4=>inputoutput: 微信小程序显示数据
op5=>operation: 启动四轴飞行器
op6=>inputoutput: 树莓派发送实时蓝牙控制命令
sub1=>subroutine: 四轴飞行器降落并待命
cond=>condition: Swich
单击动作'0'(需要去重复)
为奇数次:>http://gliang.eu


st->op1->op2->op3->op4->cond
cond(yes)->op6->op5->e
cond(no)->sub1(right)->op1
```


##0.1 利其器之Markdown
### 0.1.1 侧边栏

!!! Note "手动修改步骤"
    1.删除body样式
    2.添加css样式
    
    ~~~css
    .tod {
      height: 100%; /*目录框的高度*/
      float:left;/*目录框的位置*/
      overflow-y:scroll;/*目录框添加滚动条*/
      padding-right: 10px;
      position: fixed;/*目录框相对浏览器进行定位*/
      width:36%;/*目录框的宽度*/
      font-family: sans-serif;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      color: #333333;
      font-family: "Helvetica Neue", Helvetica, "Segoe UI", Arial, freesans, sans-serif;
      font-size: 16px;
      line-height: 1.6;
      word-wrap: break-word;
      text-decoration: none;
        }
    A { text-decoration: none} 
    A:hover { text-decoration:underline;} 

    .markdown-body {
      font-family: sans-serif;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      color: #333333;
      overflow: hidden;
      font-family: "Helvetica Neue", Helvetica, "Segoe UI", Arial, freesans, sans-serif;
      font-size: 16px;
      line-height: 1.6;
      word-wrap: break-word;
      margin: 16px auto;
      max-width: 980px;
      outline: 1300px solid #fff;

        float:right;/*正文的位置*/
        padding-left: 10px;/*边距*/
        width:60%;/*正文的宽度*/
    }
    ~~~

    3.修改html
    ~~~html
    <h1 id="0-markdown
    </article>
    ~~~
    搜索并将以下代码放在以上位置之前 
    ~~~html
    <div class="right-div">
        这里是正文部分
    </div>
    ~~~


!!! Note "自动修改步骤"

	① pip install beautifulsoup4
	② os.getcwd()
	③ 代码如下
	~~~python
	# -*- coding: utf-8 -*- 
	from bs4 import BeautifulSoup
	import re
	import os

	if os.path.exists("index.html") :
		os.remove("index.html")
	html = open('in.html',"r+")

	soup = BeautifulSoup(html, "html5lib")
	#Rename
	divto = soup.find("div", class_="to")
	divtoc = soup.find("div", class_="toc")
	print divto
	if divto!=None or divto!="": 
	    divto.append(divtoc)
	divto.div['class'] = 'tod'
	html = soup.prettify("utf-8")

	keyword="outline: 1300px solid #fff;"
	post = html.find(keyword)
	if post != -1:
	    html = html[:post+len(keyword)]+"float:right;padding-left:10px;width:60%;"+html[post+len(keyword):]
	    file = open('index.html', 'w')
	    file.write(html)
	file.close( )
	os.remove("in.html")

	~~~

## 0.2 利其器之Sublime

### 0.2.1 添加 snippet

~~~html
<snippet>
	<content><![CDATA[
|${1:this}|${2}| 
| ------------- |:---------------:| 
|${3}|${4}| 
|${5}|${6}|
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	 <tabTrigger>mt</tabTrigger> 
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<!-- <scope>source.python</scope> -->
	 <description>Markdown-table</description>
</snippet>

<snippet>
	<content><![CDATA[
!!! ${1:hint}${2:Attention}${3:Caution}${4:Danger}${5:Question}${6:Note}${7:Unknown} "${8}"
    ${9:content}
]]></content>
	 <tabTrigger>mb</tabTrigger> 
	 <description>Markdown-hint</description>
</snippet>

<snippet>
	<content><![CDATA[
- [${1:X}] ${2:Attention}
 	* [${3:X}] ${4:Note}
    	+ [${5:X}] ${6:Note}
]]></content>
	 <tabTrigger>mal</tabTrigger> 
	 <description>Markdownlist</description>
</snippet>

<snippet>
	<content><![CDATA[
波浪符号${2:python}
${1:Code here}
波浪符号
]]></content>
	 <tabTrigger>mc</tabTrigger> 
	 <description>MarkdownCodes</description>
</snippet>


<snippet>
	<content><![CDATA[
$$${1:Formular here}^{${2:upper}}$$
]]></content>
	 <tabTrigger>mf</tabTrigger> 
	 <description>MarkdownFormular</description>
</snippet>

<snippet>
	<content><![CDATA[
${51:指数} ^{$1} _{$3}
${54:偏微分} \partial f_{\mbox{$4}}
${55:分数} \frac{$5}{$6}
${57:根号} \sqrt[{7:次数}]{$8}
${59:累加} \sum_{$9=1}^$10
${511:积分} \int_$11^$12
\overline{$13}
\underline{$14}
${55:上花} \overbrace{$15}^{$16}
\underbrace{$17}_{$18}
\dot{$19}
\ddot{$20}
\vec{$21}
\left(${21:……}\right)
\in
\mathbb{R} 
]]></content>
	 <tabTrigger>mu</tabTrigger> 
	 <description>MarkdownFormular</description>
</snippet>
~~~

##0.3 AutoHotkey

示例

~~~python
msgbox, 这是我的第一个AutoHotkey脚本 `n 我既关注效率，也尊重版权
run, http://xbeta.info/autohotkey-guide.htm
~~~

;ClipSaved := ClipboardAll   ; 把剪贴板的所有内容保存到您选择的变量中.
;Clipboard := ClipSaved   ; 恢复剪贴板为原来的内容. 注意这里使用 Clipboard (不是 ClipboardAll).
;FileAppend, %ClipboardAll%, C:\Company Logo.clip ;
;ClipSaved =   ; 在原来的剪贴板含大量内容时释放内存.

~~~ahk
;将本地图片插入Markdown
^+c:: ;ctrl+shift+c
clipboard= ;清空剪贴板
send, ^c
clipwait
clipboard = ![](%clipboard%)
msgbox, 图片路径已复制！%clipboard%
return
~~~




!!! hint "保存格式"
    保存格式必须选为 UTF-8 with BOM！

***

#1 传感器 执行器
##1.1 Arduino传感器模块示例

### 1.1.1 IR 模块

~~~c
#include <IRremote.h>
#include <IRremoteInt.h>

int receiver = 13; // Signal Pin of IR receiver to Arduino Digital Pin 13

/*-----( Declare objects )-----*/
IRrecv irrecv(receiver);     // create instance of 'irrecv'
decode_results results;      // create instance of 'decode_results'1

/*-----( Function )-----*/
void translateIR() // takes action based on IR code received

// describing Remote IR codes

{

  switch(results.value)

  {
  case 0xFFA25D: Serial.println("POWER"); break;
  case 0xFFE21D: Serial.println("FUNC/STOP"); break;
  case 0xFF629D: Serial.println("VOL+"); break;
  case 0xFF22DD: Serial.println("FAST BACK");    break;
  case 0xFF02FD: Serial.println("PAUSE");    break;
  case 0xFFC23D: Serial.println("FAST FORWARD");   break;
  case 0xFFE01F: Serial.println("DOWN");    break;
  case 0xFFA857: Serial.println("VOL-");    break;
  case 0xFF906F: Serial.println("UP");    break;
  case 0xFF9867: Serial.println("EQ");    break;
  case 0xFFB04F: Serial.println("ST/REPT");    break;
  case 0xFF6897: Serial.println("0");    break;
  case 0xFF30CF: Serial.println("1");    break;
  case 0xFF18E7: Serial.println("2");    break;
  case 0xFF7A85: Serial.println("3");    break;
  case 0xFF10EF: Serial.println("4");    break;
  case 0xFF38C7: Serial.println("5");    break;
  case 0xFF5AA5: Serial.println("6");    break;
  case 0xFF42BD: Serial.println("7");    break;
  case 0xFF4AB5: Serial.println("8");    break;
  case 0xFF52AD: Serial.println("9");    break;
  case 0xFFFFFFFF: Serial.println(" REPEAT");break;

  default:
    Serial.println(" other button   ");

  }// End Case

  delay(500); // Do not get immediate repeat


} //END translateIR
void setup()   /*----( SETUP: RUNS ONCE )----*/
{
  Serial.begin(9600);
  Serial.println("IR Receiver Button Decode");
  irrecv.enableIRIn(); // Start the receiver

}/*--(end setup )---*/


void loop()   /*----( LOOP: RUNS CONSTANTLY )----*/
{
  if (irrecv.decode(&results)) // have we received an IR signal?

  {
    translateIR();
    irrecv.resume(); // receive the next value
  }
}/* --(end main loop )-- */

~~~

### 1.1.2 四位数显

~~~c
int latch=9;  //74HC595  pin 9 STCP
int clock=10; //74HC595  pin 10 SHCP
int data=8;   //74HC595  pin 8 DS

unsigned char table[]=
{0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0xbf,0x86,0xdb,0xcf,0xe6,0xed,0xfd,0x87,0xff,0xef};

//0x77,0x7c,0x39,0x5e,0x7b,0x71,0x3d


void setup() {
  pinMode(latch,OUTPUT);
  pinMode(clock,OUTPUT);
  pinMode(data,OUTPUT);
}
void Display(unsigned char num)
{

  digitalWrite(latch,LOW);
  shiftOut(data,clock,MSBFIRST,table[num]);
  digitalWrite(latch,HIGH);

}
void loop() {
  Display(1);
  delay(500);
  Display(2);
  delay(500);
  Display(3);
  delay(500);
  Display(4);
  delay(500);
  Display(5);
  delay(500);
  Display(6);
  delay(500);
  Display(7);
  delay(500);
  Display(8);
  delay(500);
  Display(9);
  delay(500);
  Display(10);
  delay(500);
  Display(11);
  delay(500);
  Display(12);
  delay(500);
  Display(13);
  delay(500);
  Display(14);
  delay(500);
  Display(15);
  delay(500);
  Display(16);
  delay(500);
  Display(17);
  delay(500);
  Display(18);
  delay(500);
  Display(19);
  delay(500);
  Display(20);
  delay(500);
}
~~~



### 1.1.3 超声波测距

~~~c
#include <SR04.h>
#define TRIG_PIN 12
#define ECHO_PIN 11
SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);
long a;

void setup() {
   Serial.begin(9600);
   delay(1000);
}

void loop() {
   a=sr04.Distance();
   Serial.print(a);
   Serial.println("cm");
   delay(1000);
}
~~~

### 1.1.4 温度湿度

~~~c
#include <SimpleDHT.h>

// for DHT11,
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
int pinDHT11 = 2;
SimpleDHT11 dht11;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // start working...
  Serial.println("=================================");
  Serial.println("Sample DHT11...");

  // read with raw sample data.
  byte temperature = 0;
  byte humidity = 0;
  byte data[40] = {0};
  if (dht11.read(pinDHT11, &temperature, &humidity, data)) {
    Serial.print("Read DHT11 failed");
    return;
  }

  Serial.print("Sample RAW Bits: ");
  for (int i = 0; i < 40; i++) {
    Serial.print((int)data[i]);
    if (i > 0 && ((i + 1) % 4) == 0) {
      Serial.print(' ');
    }
  }
  Serial.println("");

  Serial.print("Sample OK: ");
  Serial.print((int)temperature); Serial.print(" ℃, ");
  Serial.print((int)humidity); Serial.println(" %");
    int
/*
hu=data[0]*128+data[1]*64+data[2]*32+data[3]*16+data[4]*8+data[5]*4+data[6]*2+data[7];
  int te=data[16]*128+data[17]*64+data[18]*32+data[19]*16+data[20]*8+data[21]*4+data[22]*2+data[23];
  Serial.print(te);
  Serial.print(' ');
  Serial.print(hu);
  Serial.println("");*/

  // DHT11 sampling rate is 1HZ.
  delay(1000);
}
~~~

### 1.1.5 模拟控制器

~~~c
// Arduino pin numbers
const int SW_pin = 4; // digital pin connected to switch output
const int X_pin = 0; // analog pin connected to X output
const int Y_pin = 1; // analog pin connected to Y output

void setup() {
  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  Serial.begin(9600);
}

void loop() {
  Serial.print("Switch:  ");
  Serial.print(digitalRead(SW_pin));
  Serial.print("\n");
  Serial.print("X-axis: ");
  Serial.print(analogRead(X_pin));
  Serial.print("\n");
  Serial.print("Y-axis: ");
  Serial.println(analogRead(Y_pin));
  Serial.print("\n\n");
  delay(500);
}
~~~

###1.1.6 有源蜂鸣器

~~~c
int buzzer = 7;//the pin of the active buzzer
void setup()
{
 pinMode(buzzer,OUTPUT);//initialize the buzzer pin as an output
}
void loop()
{
 unsigned char i;
 while(1)
 {
   //output an frequency
   for(i=0;i<80;i++)
   {
    digitalWrite(buzzer,HIGH);
    delay(1);//wait for 1ms
    digitalWrite(buzzer,LOW);
    delay(1);//wait for 1ms
    }
    //output another frequency
     for(i=0;i<100;i++)
      {
        digitalWrite(buzzer,HIGH);
        delay(2);//wait for 2ms
        digitalWrite(buzzer,LOW);
        delay(2);//wait for 2ms
      }
  }
}
~~~

### 1.1.7 亮度传感器


~~~c
int lightPin = 2;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int reading  = analogRead(lightPin);
  Serial.print(reading);
  Serial.print("\n");
  delay(500);
}
~~~

### 1.1.8 彩色LED

~~~c
// Define Pins
#define BLUE 3
#define GREEN 5
#define RED 6

void setup()
{
pinMode(RED, OUTPUT);
pinMode(GREEN, OUTPUT);
pinMode(BLUE, OUTPUT);
digitalWrite(RED, HIGH);
digitalWrite(GREEN, LOW);
digitalWrite(BLUE, LOW);
}

// define variables
int redValue;
int greenValue;
int blueValue;

// main loop
void loop()
{
#define delayTime 10 // fading time between colors

redValue = 255; // choose a value between 1 and 255 to change the color.
greenValue = 0;
blueValue = 0;

// this is unnecessary as we've either turned on RED in SETUP
// or in the previous loop ... regardless, this turns RED off
// analogWrite(RED, 0);
// delay(1000);

for(int i = 0; i < 255; i += 1) // fades out red bring green full when i=255
{
redValue -= 1;
greenValue += 1;
// The following was reversed, counting in the wrong directions
// analogWrite(RED, 255 - redValue);
// analogWrite(GREEN, 255 - greenValue);
analogWrite(RED, redValue);
analogWrite(GREEN, greenValue);
delay(delayTime);
}

redValue = 0;
greenValue = 255;
blueValue = 0;

for(int i = 0; i < 255; i += 1) // fades out green bring blue full when i=255
{
greenValue -= 1;
blueValue += 1;
// The following was reversed, counting in the wrong directions
// analogWrite(GREEN, 255 - greenValue);
// analogWrite(BLUE, 255 - blueValue);
analogWrite(GREEN, greenValue);
analogWrite(BLUE, blueValue);
delay(delayTime);
}

redValue = 0;
greenValue = 0;
blueValue = 255;

for(int i = 0; i < 255; i += 1) // fades out blue bring red full when i=255
{
// The following code has been rearranged to match the other two similar sections
blueValue -= 1;
redValue += 1;
// The following was reversed, counting in the wrong directions
// analogWrite(BLUE, 255 - blueValue);
// analogWrite(RED, 255 - redValue);
analogWrite(BLUE, blueValue);
analogWrite(RED, redValue);
delay(delayTime);
}
}
~~~

### 1.1.9 个位数显

~~~c
// define the LED digit patterns, from 0 - 9
// 1 = LED on, 0 = LED off, in this order:
//                74HC595 pin     Q0,Q1,Q2,Q3,Q4,Q5,Q6,Q7
//                Mapping to      a,b,c,d,e,f,g of Seven-Segment LED
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
                            B11100111,  // = q.     19
                            B10011110,   // = E     20
                            B11100111, // = e    21
                            B11111111  // = 8.   22
                             };

// connect to the ST_CP of 74HC595 (pin 3,latch pin)
int latchPin = 9;
// connect to the SH_CP of 74HC595 (pin 4, clock pin)
int clockPin = 10;
// connect to the DS of 74HC595 (pin 2)
int dataPin = 8;

void setup() {
  // Set latchPin, clockPin, dataPin as output
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
}

// display a number on the digital segment display
void sevenSegWrite(byte digit) {
  // set the latchPin to low potential, before sending data
  digitalWrite(latchPin, LOW);

  // the original data (bit pattern)
  shiftOut(dataPin, clockPin, LSBFIRST, seven_seg_digits[digit]);

  // set the latchPin to high potential, after sending data
  digitalWrite(latchPin, HIGH);
}

void loop() {
  // count from 22 to 0
  for (byte digit = 22; digit > 0; --digit) {
    delay(1000);
    sevenSegWrite(digit - 1);
  }

  // suspend 4 seconds
  delay(3000);
}
~~~

### 1.1.10 电位器实现油门
模拟信号读取

~~~c
double predata=0;
int readPin = A5;
double sensorValue=0;

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

}

// the loop routine runs over and over again forever:
void loop() {
	  // read the input on analog pin 0:
	sensorValue = analogRead(readPin);
	  // print out the value you read:
	if (sensorValue !=  0)
	{
	 if (sensorValue < predata-1 || sensorValue > predata+1)
	  {
	  Serial.println(sensorValue);
	  predata = sensorValue;
	  }
	}
  
}
~~~

***

# 2 Arduino下位机
##2.1 Arduino 格式化数据 ArduinoJson
###2.1.1 Encoding JSON
~~~mermaid
graph TD;
A(1.Reserve memory space:StaticJsonBuffer)-->B(2.Build object tree in memory);
B-->C(3.Generate the JSON string);
~~~
`StaticJsonBuffer<200> jsonBuffer;`
###2.1.2 示例

~~~c
// Copyright Benoit Blanchon 2014-2017
// MIT License
//
// Arduino JSON library
// https://bblanchon.github.io/ArduinoJson/
// If you like this project, please add a star!

#include <ArduinoJson.h>

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    // wait serial port initialization
  }

  // Memory pool for JSON object tree.
  //
  // Inside the brackets, 200 is the size of the pool in bytes.
  // If the JSON object is more complex, you need to increase that value.
  // See https://bblanchon.github.io/ArduinoJson/assistant/
  StaticJsonBuffer<200> jsonBuffer;

  // StaticJsonBuffer allocates memory on the stack, it can be
  // replaced by DynamicJsonBuffer which allocates in the heap.
  //DynamicJsonBuffer jsonBuffer;

  // Create the root of the object tree.
  //
  // It's a reference to the JsonObject, the actual bytes are inside the
  // JsonBuffer with all the other nodes of the object tree.
  // Memory is freed when jsonBuffer goes out of scope.
  JsonObject& root = jsonBuffer.createObject();

  // Add values in the object
  //
  // Most of the time, you can rely on the implicit casts.
  // In other case, you can do root.set<long>("time", 1351824120);
  root["sensor"] = "gps";
  root["time"] = 1351824120;

  // Add a nested array.
  //
  // It's also possible to create the array separately and add it to the
  // JsonObject but it's less efficient.
  JsonArray& data = root.createNestedArray("data");
  data.add(48.756080);
  data.add(2.302038);

  root.printTo(Serial);
  // This prints:
  // {"sensor":"gps","time":1351824120,"data":[48.756080,2.302038]}

  Serial.println();

  root.prettyPrintTo(Serial);
  // This prints:
  // {
  //   "sensor": "gps",
  //   "time": 1351824120,
  //   "data": [
  //     48.756080,
  //     2.302038
  //   ]
  // }
}

void loop() {
  // not used in this example
}
~~~

### 2.1.3 计算缓冲块大小

~~~c
const int BUFFER_SIZE1 = JSON_OBJECT_SIZE(6);
const int BUFFER_SIZE2 = JSON_OBJECT_SIZE(1) + JSON_ARRAY_SIZE(2);
Serial.println(BUFFER_SIZE1);
Serial.println(BUFFER_SIZE2);

const int BUFFER_SIZE = JSON_OBJECT_SIZE(3) + JSON_ARRAY_SIZE(2);
StaticJsonBuffer<BUFFER_SIZE> jsonBuffer;
~~~

###2.1.4 输入数据

~~~c
  String input ="{\"sensor\":\"gps\",\"time\":1351824120,\"data\":[48.756080,2.302038]}";
  JsonObject& root = jsonBuffer.parseObject(input);
~~~

###2.1.5 代码整合

~~~c
#include <ArduinoJson.h>

void jsonBuffer(long ti, int ir,int di, int te, int hu, int li) {
StaticJsonBuffer<70> jsonBuffer;
JsonObject& rootB = jsonBuffer.createObject();
rootB["Time"] =ti;
rootB["IR"] =ir;
rootB["Distance"] =di;
rootB["Temperature"] =te;
rootB["Humity"] =hu;
rootB["Light"] =li;
rootB.prettyPrintTo(Serial);
Serial.println();
}

void joyStick(int x, int y){
StaticJsonBuffer<40> joyStick;
JsonObject& rootS = joyStick.createObject();
JsonArray& Stick= rootS.createNestedArray("Stick");
Stick.add(x);
Stick.add(y);
rootS.prettyPrintTo(Serial);
Serial.println();
}

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
while (!Serial) { } // wait serial port initialization

jsonBuffer(1351824120,01,311,24,52,999);
joyStick(1000, 999);
}

void loop() {
  // put your main code here, to run repeatedly:

}
~~~

###2.1.6 时间函数库

~~~c
#include <Time.h>
#include <TimeLib.h>

//The functions available in the library include
hour();            // the hour now  (0-23)
minute();          // the minute now (0-59)
second();          // the second now (0-59)
day();             // the day now (1-31)
weekday();         // day of the week (1-7), Sunday is day 1
month();           // the month now (1-12)
year();            // the full four digit year: (2009, 2010 etc)

hourFormat12();    // the hour now in 12 hour format
isAM();            // returns true if time now is AM
isPM();            // returns true if time now is PM

now();             // returns the current time as seconds since Jan 1 1970


time_t t = now(); // store the current time in time variable t
hour(t);          // returns the hour for the given time t
minute(t);        // returns the minute for the given time t
second(t);        // returns the second for the given time t
day(t);           // the day for the given time t
weekday(t);       // day of the week for the given time t
month(t);         // the month for the given time t
year(t);          // the year for the given time t

setTime(t);                      // set the system time to the give time t
setTime(hr,min,sec,day,mnth,yr); // alternative to above, yr is 2 or 4 digit yr
                                 // (2010 or 10 sets year to 2010)
adjustTime(adjustment);          // adjust system time by adding the adjustment value
timeStatus();                    // indicates if time has been set and recently synchronized
                                 // returns one of the following enumerations:
timeNotSet                       // the time has never been set, the clock started at Jan 1 1970
timeNeedsSync                    // the time had been set but a sync attempt did not succeed
timeSet                          // the time is set and is synced


~~~

###2.1.7 改造并集成Arduino传感器

~~~c
#include <Time.h>
#include <TimeLib.h>

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

/*全局变量*/
long ti=1351824120;
int ir=01;
int di=311;
int te=1;
int hu=2;
int li=999;
int x=888;
int y=-999;
int s=0;


/*构建缓冲区并生成JSON*/
void jsonBuffer(unsigned long ti, int di, int te, int hu, int li) {
StaticJsonBuffer<60> jsonBuffer;
JsonObject& rootB = jsonBuffer.createObject();
rootB["Time"] =ti;
rootB["Distance"] =di;
rootB["Temperature"] =te;
rootB["Humity"] =hu;
rootB["Light"] =li;
rootB.prettyPrintTo(Serial);
Serial.println();
}

void joyStick(int swich,int x, int y,int ir){
StaticJsonBuffer<60> joyStick;
JsonObject& rootS = joyStick.createObject();
rootS["IR"] =ir;
rootS["Swich"] =swich;
JsonArray& Stick= rootS.createNestedArray("Stick");
Stick.add(x);
Stick.add(y);
rootS.prettyPrintTo(Serial);
Serial.println();
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
  case 0xFFA25D: {return 1;    }    //break; //Serial.println("POWER")
  case 0xFFE21D: {return 2;    }    //break; //Serial.println("FUNC/STOP")
  case 0xFF629D: {return 3;    }    //break; //Serial.println("VOL+");
  case 0xFF22DD: {return 4;    }    //   break; //Serial.println("FAST BACK");
  case 0xFF02FD: {return 5;    }    //   break; //Serial.println("PAUSE");
  case 0xFFC23D: {return 6;    }    //  break; //Serial.println("FAST FORWARD");
  case 0xFFE01F:  {return 7;   }    //   break; //Serial.println("DOWN");
  case 0xFFA857: {return 8;    }    //  break; //Serial.println("VOL-");
  case 0xFF906F: {return 9;    }    //  break; //Serial.println("UP");
  case 0xFF9867: {return 10;   }    //    break; //Serial.println("EQ");
  case 0xFFB04F:  {return 11;  }    //    break; //Serial.println("ST/REPT");
  case 0xFF6897:  {return 12;  }    //   break;  //Serial.println("0");
  case 0xFF30CF:  {return 13;  }    //   break; // Serial.println("1");
  case 0xFF18E7:  {return 14;  }    //    break; //Serial.println("2");
  case 0xFF7A85:  {return 15;  }    //   break; //Serial.println("3");
  case 0xFF10EF:  {return 16;  }    //    break; //Serial.println("4");
  case 0xFF38C7:  {return 17;  }    //    break; //Serial.println("5");
  case 0xFF5AA5:  {return 18;  }    //    break; //Serial.println("6");
  case 0xFF42BD:  {return 19;  }    //    break; //Serial.println("7");
  case 0xFF4AB5:  {return 20;  }    //    break; // Serial.println("8");
  case 0xFF52AD:  {return 21;  }    //    break; //Serial.println("9");
  //case 0xFFFFFFFF: {irrecv.resume();return 22;  }    //   break;  //Serial.println(" REPEAT")
  //default:
    //{irrecv.resume();return 23; } //Serial.println(" other button   ");
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

  delay(dht.getMinimumSamplingPeriod());
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


void setup() {
irrecv.enableIRIn();
pinMode(SW_pin, INPUT);
digitalWrite(SW_pin, HIGH);
dht.setup(2); // data pin 2
Serial.begin(9600);
while (!Serial) {} // wait serial port initialization


//jsonBuffer(1351824120,01,311,24,52,999);
//joyStick(1000, 999);
setTime(11,30,30,5,9,2017);
//setTime(hr,min,sec,day,month,yr);
}

void loop() {
if (irrecv.decode(&results))

  {
    detTH();
    di=sr04.Distance();
    li=detlight();
    jsonBuffer(now(),di,te,hu,li);
    irrecv.resume();

    ir=transIR();
    joyStick(detSw(),detX(),detY(),ir);
  }
}
~~~

##2.2 集成多任务控制

~~~cpp
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
~~~

***

# 3 树莓派配置

## 3.1 安装初始化

~~~shell
sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade

sudo passwd pi

~~~

### 3.1.1 WIFI

sudo apt-get install wireless-tools wpasupplicant

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

```cs
network=
{
	ssid="XXX"
	psk="XXXXXXXXXXX"
}
```

sudo nano /etc/dhcpcd.conf

	interface eth0
	static ip_address=192.168.1.222/24
	static routers=192.168.1.1
	static domain_name_servers=192.168.1.1
	interface wlan0
	static ip_address=192.168.1.111/24
	static routers=192.168.1.1
	static domain_name_servers=192.168.1.1


sudo raspi-config

sudo reboot


### 3.1.2 自动备份

插上优盘，执行命令。
**sudo sh b.sh**

~~~
#!/bin/sh
#install tools
sudo apt-get -y install rsync dosfstools parted kpartx exfat-fuse
#mount USB device
usbmount=/mnt
mkdir -p $usbmount
if [ -z $1 ]; then
	echo "no argument, assume the mount device is /dev/sda1 ? Y/N"
	read key
	if [ "$key" = "y" -o "$key" = "Y" ]; then
		sudo mount -o uid=1000 /dev/sda1 $usbmount
	else
		echo "$0 [backup dest device name], e.g. $0 /dev/sda1"
		exit 0
	fi
else
	sudo mount -o uid=1000 $1 $usbmount
fi
if [ -z "`grep $usbmount /etc/mtab`" ]; then
	echo "mount fail, exit now"
	exit 0
fi
img=$usbmount/rpi-`date +%Y%m%d-%H%M`.img
#img=$usbmount/rpi.img
echo ===================== part 1, create a new blank img ===============================
# New img file
#sudo rm $img
bootsz=`df -P | grep /boot | awk '{print $2}'`
rootsz=`df -P | grep /dev/root | awk '{print $3}'`
totalsz=`echo $bootsz $rootsz | awk '{print int(($1+$2)*1.3)}'`
sudo dd if=/dev/zero of=$img bs=1K count=$totalsz
# format virtual disk
bootstart=`sudo fdisk -l /dev/mmcblk0 | grep mmcblk0p1 | awk '{print $2}'`
bootend=`sudo fdisk -l /dev/mmcblk0 | grep mmcblk0p1 | awk '{print $3}'`
rootstart=`sudo fdisk -l /dev/mmcblk0 | grep mmcblk0p2 | awk '{print $2}'`
echo "boot: $bootstart >>> $bootend, root: $rootstart >>> end"
#rootend=`sudo fdisk -l /dev/mmcblk0 | grep mmcblk0p2 | awk '{print $3}'`
sudo parted $img --script -- mklabel msdos
sudo parted $img --script -- mkpart primary fat32 ${bootstart}s ${bootend}s
sudo parted $img --script -- mkpart primary ext4 ${rootstart}s -1
loopdevice=`sudo losetup -f --show $img`
device=/dev/mapper/`sudo kpartx -va $loopdevice | sed -E 's/.*(loop[0-9])p.*/\1/g' | head -1`
sleep 5
sudo mkfs.vfat ${device}p1 -n boot
sudo mkfs.ext4 ${device}p2
echo ===================== part 2, fill the data to img =========================
# mount partitions
mountb=$usbmount/backup_boot/
mountr=$usbmount/backup_root/
mkdir -p $mountb $mountr
# backup /boot
sudo mount -t vfat ${device}p1 $mountb
sudo cp -rfp /boot/* $mountb
sync
echo "...Boot partition done"
# backup /root
sudo mount -t ext4 ${device}p2 $mountr
if [ -f /etc/dphys-swapfile ]; then
        SWAPFILE=`cat /etc/dphys-swapfile | grep ^CONF_SWAPFILE | cut -f 2 -d=`
	if [ "$SWAPFILE" = "" ]; then
		SWAPFILE=/var/swap
	fi
	EXCLUDE_SWAPFILE="--exclude $SWAPFILE"
fi
sudo rsync --force -rltWDEgop --delete --stats --progress \
	$EXCLUDE_SWAPFILE \
	--exclude '.gvfs' \
	--exclude '/dev' \
        --exclude '/media' \
	--exclude '/mnt' \
	--exclude '/proc' \
        --exclude '/run' \
	--exclude '/sys' \
	--exclude '/tmp' \
        --exclude 'lost\+found' \
	--exclude '$usbmount' \
	// $mountr
# special dirs
for i in dev media mnt proc run sys boot; do
	if [ ! -d $mountr/$i ]; then
		sudo mkdir $mountr/$i
	fi
done
if [ ! -d $mountr/tmp ]; then
	sudo mkdir $mountr/tmp
	sudo chmod a+w $mountr/tmp
fi
#sudo rm -f $mountr/etc/udev/rules.d/70-persistent-net.rules
sync
ls -lia $mountr/home/pi/
echo "...Root partition done"
# if using the dump/restore
# tmp=$usbmount/root.ext4
# sudo chattr +d $img $mountb $mountr $tmp
# sudo mount -t ext4 ${device}p2 $mountr
# cd $mountr
# sudo dump -0uaf - / | sudo restore -rf -
# cd
# replace PARTUUID
opartuuidb=`blkid -o export /dev/mmcblk0p1 | grep PARTUUID`
opartuuidr=`blkid -o export /dev/mmcblk0p2 | grep PARTUUID`
npartuuidb=`blkid -o export ${device}p1 | grep PARTUUID`
npartuuidr=`blkid -o export ${device}p2 | grep PARTUUID`
sudo sed -i "s/$opartuuidr/$npartuuidr/g" $mountb/cmdline.txt
sudo sed -i "s/$opartuuidb/$npartuuidb/g" $mountr/etc/fstab
sudo sed -i "s/$opartuuidr/$npartuuidr/g" $mountr/etc/fstab
sudo umount $mountb
sudo umount $mountr
# umount loop device
sudo kpartx -d $loopdevice
sudo losetup -d $loopdevice
sudo umount $usbmount
rm -rf $mountb $mountr
echo "==== All done. You can un-plug the backup device"
~~~

### 3.1.3 远程屏幕登陆

在树莓派上安装VNC Server：

	sudo apt-get install tightvncserver
启动树莓派VNC Server
	sudo tightvncserver :1 -geometry 1600x900
	tightvncserver -kill :1   //终止控制台

XXXXX
重置密码

	sudo tightvncpasswd

自动启动

sudo nano /etc/init.d/tightvncserver

~~~shell
#!/bin/sh
### BEGIN INIT INFO
# Provides:          tightvncserver
# Required-Start:    $local_fs
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop tightvncserver
### END INIT INFO

# More details see:
# http://www.penguintutor.com/linux/tightvnc

### Customize this entry
# Set the USER variable to the name of the user to start tightvncserver under
export USER='pi'
### End customization required

eval cd ~$USER

case "$1" in
  start)
    # 启动命令行。此处自定义分辨率、控制台号码或其它参数。
    su $USER -c '/usr/bin/tightvncserver -depth 16 -geometry 1600x900 :1'
    echo "Starting TightVNC server for $USER "
    ;;
  stop)
    # 终止命令行。此处控制台号码与启动一致。
    su $USER -c '/usr/bin/tightvncserver -kill :1'
    echo "Tightvncserver stopped"
    ;;
  *)
    echo "Usage: /etc/init.d/tightvncserver {start|stop}"
    exit 1
    ;;
esac
exit 0
~~~

sudo chmod +755 /etc/init.d/tightvncserver
sudo update-rc.d tightvncserver defaults

**桌面端登录**

~~~sh
192.168.1.111:1
XXXX
~~~

### 3.1.4清理垃圾

sudo apt-get autoclean
sudo apt-get clean
sudo apt-get autoremove

### 3.1.5 开机运行

	nano /etc/rc.local
在最后一行 exit 0 之上加入

	su txt.sh start

### 3.1.6 温度监控
创建新sh文档

nano tempera.sh
~~~
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU => $((cpu/1000))'C"
~~~
更改文件权限
>chmod +x tempera.sh

运行
./my-pi-temp.sh

~~~
结果如下
Sun 10 Sep 21:15:11 CEST 2017 @ Vi_raspberry
-------------------------------------------
GPU => temp=31.1'C
CPU => 30'C
~~~

### 3.1.7 中文
显示

~~~python
sudo apt-get -y install ttf-wqy-zenhei
~~~


## 3.2 集成arduino IDE

安装arduino IDE

	sudo apt-get update && sudo apt-get install arduino


## 3.3 远程SSH登录树莓派

 Dogtunnel

### 3.3.1 安装go语言环境

```sh
wget https://storage.googleapis.com/golang/go1.9.linux-armv6l.tar.gz
sudo tar -C /usr/local -xzf go1.9.linux-armv6l.tar.gz
export PATH=$PATH:/usr/local/go/bin
source ~/.profile
```

新建名为hello.go的文件来测试是否安装成功

```go
package main
import "fmt"
func main() {
fmt.Printf("Hello World\n")
}
```

在终端运行

```sh
go run hello.go
```



### 3.3.2 下载狗洞客户端并配置

共同的配置

- 安装依赖

  ```css
  go get github.com/go-sql-driver/mysql
  go get github.com/klauspost/reedsolomon
  go get github.com/cznic/zappy
  git clone https://github.com/vzex/dog-tunnel.git
  go get github.com/go-sql-driver/mysql
  make
  mv dtunnel /usr/bin/dtunnel
  ```

  说明：

  下载对应您系统的dtunnel客户端(win/linux/mac/arm),程序需要在狗洞两端运行，服务的一方叫远端，连接的一方叫近端。

  **远端** Raspbian

  ./dtunnel -reg name -local :80 -clientkey qwerty

  reg:注册服务名,

  local:监听端口，填socks5则为socks5代理服务，

  clientkey:默认空，近端访问用的密码

  **近端** 

  ./dtunnel -link name -local :8888 -clientkey qwerty

   link:注册服务名,

  local:服务端口，用于近端其他应用连接，

  clientkey:默认空，要和远端一致

  近端:待出现service start success字样后代表狗洞准备就绪，请连接local指定的端口测试

  注意:对于多公网ip的终端，请用-stun参数指定stun服务器辅助连接，或者用-addip参数手工指定出口ip列表

  **常规版本**

  ```css
  dtunnel_s -addr 0.0.0.0:8000 -addrudp 0.0.0.0:8018 -admin 127.0.0.1:1234 -https -ssl -cert /path/to/https.crt -key /path/to/https.key -dbhost 1.2.3.4:3306 -dbpass mysqlpass -dbuser mysqluser -replace
   
  #参数说明
  -addr：TCP端口地址
  -addrudp：UDP端口地址，用于P2P辅助打洞
  -admin：管理接口，用于提供API方便管理
  -https：启用管理接口的HTTPS支持，需要指定-cert和-cert参数，默认关闭
  -ssl：启用ssl支持，启用需要指定-cert和-cert参数，默认关闭
  -cert：证书路径
  -key：证书密钥路径
  -dbhost：数据库服务器
  -dbpass：数据库密码
  -dbuser：数据库用户
  -replace：如果客户端注册名冲突，踢掉之前的，默认关闭
  -version：显示版本
  ```

  **客户端**

  ```css
  远端: dtunnel -addip 127.0.0.1 -buster 1.2.3.4:8018 -remote 1.2.3.4::8000 -clientkey testkey -compress -delay 2 -dnscache 20 -encrypt -kcp k2:v2 -reg test -local :80 -mode 0 -ssl
   
  近端: dtunnel -addip 127.0.0.1 -buster 1.2.3.4:8018 -remote 1.2.3.4::8000 -clientkey testkey -compress -delay 2 -dnscache 20 -encrypt -kcp k2:v2 -link test -local :8888 -mode 0 -ssl
   
  #参数说明
  -addip：出口IP(单个或列表)
  -buster：打洞服务器，用于P2P模式
  -remote：远程服务器，用于C/S模式
  -clientkey：客户端Key，用于远端和近端认证，需一致
  -compress：压缩数据，远端和近端需一致
  -debug：调试模式
  -delay：打洞失败后重试延迟，秒
  -dnscache：DNS缓存有效期，如果大于0将定时清空DNS缓存，分钟
  -encrypt：P2P模式加密
  -f：从文件中加载配置
  -kcp：kcp配置，远端和近端需一致
  -key：访问Key(服务端数据库中的AuthKey)
  -reg：注册名，远端使用
  -link：连接的注册名，近端使用，用于识别连接远端
  -local：本地监听端口，填socks5则为socks5代理服务
  -mode：连接模式(0:P2P打洞失败后切换为C/S 1:只使用P2P 2:只使用C/S)
  -pipen：管道数
  -ds：数据纠错？？仅在P2P模式有效，远端和近端需一致
  -ps：奇偶校验？？仅在P2P模式有效，远端和近端需一致
  -ssl：启用ssl支持，默认启用，服务端没有启用的话请使用-ssl=false来关闭
  -v：输出详细日志
  -version：显示版本
  ```

  ​

#### 3.3.2.1 Raspbian

下载

```
mkdir dogtunnel
cd dogtunnel
wget http://dog-tunnel.tk/down/dtunnel_linux_arm_0.80.tgz
mkdir dt
sudo tar -C ~/dogtunnel/dt -xzf dtunnel_linux_arm_0.80.tgz
```

更改权限并运行

```
cd dt
chmod +x ./dtunnel
./dtunnel -reg lencshu -local :22 -clientkey XXXX
#任意目录可执行命令
/home/pi/dogtunnel/dt/dtunnel -reg lencshu -local :22 -clientkey XXXX
```

#### 3.3.2.2 VPS

下载

```
mkdir dogtunnel
cd dogtunnel
wget http://dog-tunnel.tk/down/dtunnel_linux_x64_0.80.tgz
mkdir dt
sudo tar -C /home/liang/dogtunnel/dt -xzf dtunnel_linux_x64_0.80.tgz
```

更改权限并运行

```
cd dt
chmod +x ./dtunnel
./dtunnel -link lencshu -local :8888 -clientkey XXXX
#任意目录可执行
/home/liang/dogtunnel/dt/dtunnel -link lencshu -local :8888 -clientkey XXXX
```



### 3.3.3 添加开机自启动脚本

#### 3.3.3.0 准备步骤

**将命令更改为后台运行并且任意目录可执行**

```python
#服务端 Raspbian
sudo nohup /home/pi/dogtunnel/dt/dtunnel -reg lencshu -local :22 -clientkey XXXX -v 2>& 1 1 > /var/log/dtunnel.log &
#客户端 66
sudo nohup /root/dogtunnel/dt/dtunnel -link lencshu -local :8888 -clientkey XXXX -v 2>& 1 1 > /var/log/dtunnel.log &
# 日志文件目录权限问题
nohup /home/pi/dogtunnel/dt/dtunnel -reg xxx -local :22 -clientkey XXXXXXXX -v 2>& 1 1 > /home/pi/log/dogtunnel.log &
```

后重启
``/var/log/dtunnel.log`` 是输出日志

因为dtunnel本身不是后台命令，直接这样执行的话，可能是会阻塞住那个启动脚本的，上面是改成了后台执行，还是启动不了的话就看看输出日志里有没有异常


#### 3.3.3.1 命令行自动运行

`sudo nano /etc/init.d/dogtunnel`

~~~python
#! /bin/sh
# /etc/init.d/noip 

### BEGIN INIT INFO
# Provides:          noip
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
# Description:       A simple script which will start / stop a program a boot / shutdown.
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting DogTunnel"
    # run application you want to start
    #服务端
    #/home/pi/dogtunnel/dt/dtunnel -reg lencshu -local :22 -clientkey XXXX
    #客户端
    /home/liang/dogtunnel/dt/dtunnel -link lencshu -local :8888 -clientkey XXXX
    ;;
  stop)
    echo "Stopping DogTunnel"
    # kill application you want to stop
    killall dtunnel
    ;;
  *)
    echo "Usage: /etc/init.d/dtunnel {start|stop}"
    exit 1
    ;;
esac

exit 0
~~~

Make the script executable:

```
sudo chmod +755 /etc/init.d/dogtunnel
```

测试

```
sudo /etc/init.d/dogtunnel start  
sudo /etc/init.d/dogtunnel stop
```

Register script to be run at startup:

```
cd /etc/init.d/
sudo update-rc.d dogtunnel defaults
```

清除 remove the script from start-up

```
sudo update-rc.d -f dogtunnel remove
```



### 3.3.4 FTP

~~~shell
sudo apt install -y proftpd

sudo nano /etc/proftpd/proftpd.conf

sudo service proftpd reload
~~~


### 3.3.5 查看端口占用

`sudo apt-get update && sudo apt-get install lsof`

~~~shell
ps –ef|grep 进程名
netstat -anp|grep pid
sudo lsof -i :80

	nginx   520     root    6u  IPv4  11792      0t0  TCP *:http (LISTEN)
	nginx   520     root    7u  IPv6  11793      0t0  TCP *:http (LISTEN)
	nginx   521 www-data    6u  IPv4  11792      0t0  TCP *:http (LISTEN)
	nginx   521 www-data    7u  IPv6  11793      0t0  TCP *:http (LISTEN)
	nginx   522 www-data    6u  IPv4  11792      0t0  TCP *:http (LISTEN)
	nginx   522 www-data    7u  IPv6  11793      0t0  TCP *:http (LISTEN)
	nginx   523 www-data    6u  IPv4  11792      0t0  TCP *:http (LISTEN)
	nginx   523 www-data    7u  IPv6  11793      0t0  TCP *:http (LISTEN)
	nginx   524 www-data    6u  IPv4  11792      0t0  TCP *:http (LISTEN)
	nginx   524 www-data    7u  IPv6  11793      0t0  TCP *:http (LISTEN)



Utilisation de commande lsof :

lsof -i           (tous services internet TCP/UDP)
lsof -i tcp      (tous services TCP)
lsof -i udp     (tous services UDP)
lsof -i tcp:80 (services TCP sur port 80)
lsof -i @56.85.68.98   (liaison internet de mon poste avec 56.85.68.98)
Afficher les fichiers ouverts par un processus :

lsof -p 1456
Afficher les connexions internet ouvertes par un processus :

lsof -i -p 1234
Pour connaître tous les ports réseau ouvert par le processus qui a le pid 1234 (-a est interprété comme AND)

lsof -i -a -p 1234
La forme suivante de la commande permet de connaître tous les fichiers ouverts par l’utilisateur 500 ou toto ou par le processus 1234 ou 12345 :

lsof -p 1234,12345 -u 500,toto
~~~

### 3.3.6 Nginx web服务器

`service nginx {start|stop|status|restart|reload|configtest} `


`sudo nano /etc/nginx/sites-available/default`


### 3.3.7 python paramiko

paramiko 遵循SSH2协议，支持以加密和认证的方式，进行远程服务器的连接，可以实现远程文件的上传，下载或通过ssh远程执行命令。
`sudo apt-get install build-essential libssl-dev libffi-dev python3-dev`

## 3.4 Conda 管理 配置python环境
### 3.4.1 安装配置 Miniconda (bundled with Python 3)

~~~
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
sudo md5sum Miniconda3-latest-Linux-armv7l.sh
sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh
~~~

Prepending PATH=/home/pi/miniconda3/bin to PATH in /root/.bashrc
A backup will be made to: /root/.bashrc-miniconda3.bak

将默认安装目录更改为

~~~python
/home/pi/miniconda3
sudo nano /home/pi/.bashrc
# Bdd the following line to the end of the file
export PATH="/home/pi/miniconda3/bin:$PATH"

#Save and close this file
source ~/.bashrc
python -version
#Python 3.4.3 :: Continuum Analytics, Inc.

sudo chown -R pi miniconda3
conda config --set show_channel_urls True
conda config --add channels conda-forge
conda config --add channels poppy-project
conda update --all --yes
conda install conda-build
conda install anaconda-client
conda clean -tipy
conda install --yes jinja2
conda config --set anaconda_upload yes
conda config --set use_pip false
conda config --set show_channel_urls true

~~~


**配置Pyserial**

~~~python
conda create -n py2.7 python=2.7
source activate py27
#通过-c指定通过某个channel安装
conda install -c conda-forge pyserial
~~~

**配置IPython Notebook**

~~~python
conda install ipython
conda install jupyter
jupyter notebook
~~~



### 3.4.2 参考命令
#### 3.4.2.1 卸载
~~~python
sudo rm -rf ~/miniconda3 ~/.condarc ~/.conda ~/.continuum
#remove the anaconda directory from your PATH environment variable
sudo nano /home/pi/.bashrc
source ~/.bashrc
~~~


#### 3.4.2.2 常用命令

~~~python
#查看列表
conda list

#更新
conda update conda

#环境
conda create -n env_vi python=3.4.3
conda env list

#切换新环境
source activate py27
#退出环境，也可以使用`activate root`切回root环境
source activate root
source deactivate py27
#移除环境
conda remove --all -n py27
# 创建只有django的python2环境，名字py2-dj，注意，python=2 django是连续参数
conda create python=2 django -n py2-dj
~~~

***

### 3.4.3 python 库

#### 3.4.3.1 simplejson

~~~python
 git clone https://github.com/simplejson/simplejson.git
 python setup.py install
~~~

##3.5 云打印机

installing CUPS

~~~shell
sudo apt-get update
sudo apt-get install cups
#The usergroup created by CUPS is “lpadmin”. The default Rasbian user (and the user we’re logged into) is “pi” (adjust the following command accordingly if you want a different user to have access to the printer).
sudo usermod -a -G lpadmin pi
~~~

For the curious, the “-a” switch allows us to add an existing user (pi) to an existing group (lpadmin), specified by the “-G” switch.

The rest of the configuration can be completed via the web browser on the Pi, but if you’re not actually sitting right at the Pi and would prefer to use, say, the browser on your Windows desktop to complete the configuration, you’ll need to toggle a small value in /etc/cups/cupsd.conf. At the terminal, enter the following command:

~~~shell
sudo nano /etc/cups/cupsd.conf
~~~

Comment out the “Listen localhost:631” line and replace it with the following:

~~~python
# Only listen for connections from the local machine
# Listen localhost:631
Port 631
~~~

Inside the file, look for this section:

~~~python
< Location / >
# Restrict access to the server...
Order allow,deny
Allow @local
< /Location >

< Location /admin >
# Restrict access to the admin pages...
Order allow,deny
Allow @local
Allow 192.168.1.0/24
< /Location >

< Location /admin/conf >
AuthType Default
Require user @SYSTEM

# Restrict access to the configuration files...
Order allow,deny
Allow @local
< /Location >
~~~

The addition of the “allow @local” line allows access to CUPS from any computer on your local network. Anytime you make changes to the CUPS configuration file, you’ll need to restart the CUPS server. Do so with the following command:

~~~python
sudo /etc/init.d/cups restart

sudo iptables -A INPUT -i wlan0 -p tcp -m tcp --dport 631 -j ACCEPT
sudo iptables -A INPUT -i wlan0 -p udp -m udp --dport 631 -j ACCEPT
~~~

电脑连接
http://XXXXXXXX/printers/Vi.Canon


注册为谷歌print

~~~shell
#安装
git clone https://github.com/armooo/cloudprint.git
sudo apt-get install libcups2-dev
sudo pip3 install pycups
apt-get install python-cups
sudo apt-get install python3-dev
sudo pip install daemon
#sudo python setup.py install
sudo pip install cloudprint
~~~

cloudprint-service

~~~python
sudo apt-get install cloudprint-service
echo "deb http://davesteele.github.io/cloudprint-service/repo cloudprint-jessie main" | sudo tee /etc/apt/sources.list.d/cloudprint.list
wget -q -O - https://davesteele.github.io/key-366150CE.pub.txt | sudo apt-key add -
sudo apt-get update
~~~

Install the software. This will likely involve more than 40 packages.

~~~shell
sudo apt-get -y upgrade
sudo apt-get -y install cloudprint-service
~~~

Make the CUPS web page externally accessible.

~~~shell
sudo cupsctl --remote-admin
sudo usermod -a -G lpadmin pi
sudo systemctl restart cups
~~~


#配置

~~~python
sudo cps-auth
~~~

The output of the cps_auth command will include a URL. Copy this URL to your browser, and use it to establish authentication.

Now restart the cloudprint service to use this account.

~~~python
sudo systemctl restart cloudprintd
sudo cupsctl --no-remote-admin
sudo systemctl restart cups
~~~

~~~shell
sudo nano /etc/resolv.conf.head
nano /etc/resolv.conf
~~~

in your terminal. You will have a blank slate to work with. Next copy and paste the following code:

~~~python
#Google Servers
nameserver 8.8.8.8
nameserver 8.8.4.4
~~~

click on cntrl + x to exit out and select y for the following options to save. Restart your Raspberry Pi with

~~~shell
sudo reboot
sudo systemctl restart cloudprintd
~~~
ios
sudo apt-get install avahi-discover

扫描

~~~python
scanimage -L
sudo aptitude install xsane
sudo nano /etc/sane.d/saned.conf
sudo apt-get install xsane skanlite
~~~

sudo nano /etc/sane.d/saned.conf
192.168.1.0/24
sudo nano /etc/default/saned
RUN=no

sane-find-scanner
sudo adduser saned lp

sudo systemctl start saned.socket
sudo systemctl enable saned.socket
sudo systemctl status saned.socket


关于打印速度的讨论

在实际使用中，发现Windows PC打印速度快，即提交打印任务后打印立即开始，而使用iOS设备发送打印任务之后存在较长的等待时间才会开始打印。在研究造成该问题的原因之前，我们需要知道CUPS共享打印机的原理是什么。 CUPS使用原生驱动，可将多种类型的文件，如PDF，PostScript文件直接渲染成打印机支持的二进制文件。CUPS同时也支持将原始二进制流直接传送至打印机，而无需做本地文件渲染。CUPS对于输入文件流类型的支持可在mime.convs与mime.types两个文件中进行设置。 由于在Windows上安装了打印机的原生驱动，渲染操作在客户端已经完成，CUPS只需要将原始二进制流不经更改地传送给打印机，因此基本无需等待时间。而iOS使用AirPrint的原理则为将各种类型的文本图像先生成PDF文档，再将PDF传送至AirPrint打印服务器。而AirPrint服务器在收到该PDF文档后仍需要将文件渲染成打印机支持的二进制流，再将该流传送至打印机设备。因此在使用iOS进行AirPrint时实际需要对原始文件进行两次转换。同时，受到iOS与Raspberry Pi的处理能力限制，两次转换的效率很大程度上取决于原始文件的大小与复杂度。

***


# 4 Raspberry 和 Arduino 串口通信

## 4.1 配置协议

安装python

	sudo aptitude install python-dev

安装python的GPIO模块

	sudo apt-get install python-dev python-rpi.gpio

安装serial用于串口通信及USB通信

	sudo apt-get install python-serial

在树莓派安装串口调试工具

	sudo apt-get install minicom
配置minicom：

	sudo minicom -s
启动出现配置菜单选 **serial port setup** 进入串口配置
输入A 配置串口驱动为

	/dev/ttyAMA0
输入E 配置速率为

	9600 8N1
输入F 将 Hardware Flow Control 设为 NO
回车 退出

由于我们使用minicom作为超级终端控制路由器等设备, 而不是控制modem, 所以需要修改 **Modem and dialing**

	将以下设置为空
	A. Init string,
	B. Reset string,
	k. Hang-up string.
设置完成后选择Save setup as dfl将当前设置保存为默认设置

	Exit from minicon
命令minicom是进入串口超级终端画面，而minicom -s为配置minicom。说明/dev/ttyAMA0 对应为串口0 为你连接开发板的端口
接下来测一下环境是否都OK：

	sudo nano test.py
输入内容为：

	import serial
	import RPi.GPIO

Ctrl +X 保存退出执行

	python test.py
没有报错，说明正确安装python-serial等。

插上arduino与树莓派USB口：

~~~python
#!/usr/bin/env python
# -*- coding: latin-1 -*-

import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
        print(ser.readline())
~~~

## 4.2 Json解码

添加一个开关Triger object，方便判断json文件的来源

~~~python
void jsonBuffer(unsigned long ti, int di, int te, int hu, int li) {
StaticJsonBuffer<66> jsonBuffer;
JsonObject& rootB = jsonBuffer.createObject();
rootB["Triger"] =0;
rootB["Time"] =ti;
rootB["Distance"] =di;
rootB["Temperature"] =te;
rootB["Humity"] =hu;
rootB["Light"] =li;
rootB.prettyPrintTo(Serial);
Serial.println();
}

void joyStick(int swich,int x, int y,int ir){
StaticJsonBuffer<66> joyStick;
JsonObject& rootS = joyStick.createObject();
rootS["Triger"] =1;
rootS["IR"] =ir;
rootS["Swich"] =swich;
JsonArray& Stick= rootS.createNestedArray("Stick");
Stick.add(x);
Stick.add(y);
rootS.prettyPrintTo(Serial);
Serial.println();
}
~~~

从串口获取数据

~~~python
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
    print(ser.readline())
~~~

解码Json

If we prefer working with files instead of strings, we may want to use json.dump() / json.load() to encode / decode JSON data

示例

~~~python
#!/usr/bin/env python
# -*- coding: unicode -*-

import serial
import time
import json
# Port s  rie ttyACM0
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en   criture : 1 sec

with serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1, writeTimeout=1) as poSer:
    if poSer.isOpen():
        while True:
            #poSer.write([time.time()])
            rawLigne = poSer.readline()
            print(rawLigne)
            tempData=json.loads(rawLigne)
            #tempData["Triger"] # will return 'blabla'
            print(tempData)

#data["masks"]["id"]    # will return 'valore'
#data["om_points"]      # will return 'value'
~~~

尝试

从串口获取的数据类型

```json
{
  "Triger": 0,
  "Time": 1504611032,
  "Distance": 5,
  "Temperature": 20,
  "Humity": 49,
  "Light": 103
}
{
  "Triger": 1,
  "IR": 0,
  "Swich": 1,
  "Stick": [
    499,
    510
  ]
}
```



~~~python
#!/usr/bin/env python
import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)
while ser.isOpen():
    rawLigne = ser.readline()
    #print len(rawLigne)
    stringLength=len(rawLigne)
    if (stringLength==57 or stringLength==58 or stringLength==59 or stringLength==60 or stringLength==61 or stringLength==62 or stringLength==86):
      tempeData = json.loads(rawLigne)
      if (tempeData["Triger"]):
        print tempeData
      else:
        print('6 variables')
~~~

改进代码

~~~python
#!/usr/bin/env python
import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)
while ser.isOpen():
    rawLigne = ser.readline()
    #print len(rawLigne)
    try:
      tempeData = json.loads(rawLigne)
      if (tempeData["Triger"]):
        print tempeData
      else:
        print '==>', tempeData
    except:
      # do nothing, not a valid JSON
      pass
~~~


***

# 5 Arduino 四轴飞行器

## 5.1 I2C通讯
内部集成电路（I2C）协议是双向双线串行总线，其提供集成电路之间的通信链路。

I2C是使主设备（例如处理器，微控制器（MCU）或专用集成电路（ASIC））能够与同一双线总线上的其它外围设备通信的流行通信协议。一条线专用于数据传输，而另一条用于时钟信号。想象它就像一个双车道公路：每个车道都有汽车从一端流向另一端，就像数据包将从主设备（处理器、MCU、ASIC）传输到外围设备（温度传感器、湿度传感器及其它设备）。

I2C可以在同一总线上轻松实现多个外设 - 例如，使用各种传感器来监视服务器的温度。I2C协议实际上设计用于在单个总线上支持多个设备，而如串行外设接口（SPI）的其他协议的设计用于点对点单设备支持。双线I2C接口还可以帮助简化对四线SPI接口的布线，并减少通用输入/输出（GPIO）。

I2C使系统设计人员能够轻松实现鲁棒的系统控制。

### 5.1.1 GY-80 模块


There are four sensors on this board: 
-角速度计 3 axis gyroscope from ST (L3G4200D), I2C Address: 0x69 
-加速度计 3 axis accelerometer from Analog Devices (ADXL345), I2C Address:  0x53 
-罗盘数据 3 axis digital Magnetometer (compass) from Honeywell (HMC5883L), I2C Address:  0x1E 
-气压计 Barometric Pressure and Temperature Sensor from Bosch (BMP085), I2C Address:  0x77 


#### 5.1.1.1 集合库示例

~~~c++
#include <Wire.h>
#include <GY80.h>

GY80 sensor = GY80(); //create GY80 instance

void setup()
{
    // initialize serial communication at 115200 bits per second:
    Serial.begin(9600);
    sensor.begin();       //initialize sensors
}


void loop()
{
    GY80_scaled val = sensor.read_scaled();       //get values from all sensors
    // print out values

    Serial.print("Mag:");                         //magnetometer values
    Serial.print(val.m_x,2);
    Serial.print(',');
    Serial.print(val.m_y,2);
    Serial.print(',');
    Serial.print(val.m_z,2);
    Serial.print(' ');
    Serial.print("Acc:");                         //accelerometer values
    Serial.print(val.a_x,3);
    Serial.print(',');
    Serial.print(val.a_y,3);
    Serial.print(',');
    Serial.print(val.a_z,3);
    Serial.print(' ');
    Serial.print("Gyro:");                        //gyroscope values
    Serial.print(val.g_x,1);
    Serial.print(',');
    Serial.print(val.g_y,1);
    Serial.print(',');
    Serial.print(val.g_z,1);
    Serial.print(' ');
    Serial.print("P:");                           //pressure values
    Serial.print(val.p,5);
    Serial.print(' ');
    Serial.print("T:");                           //temperature values
    Serial.println(val.t,1);


    delay(250);        // delay in between reads for stability
}
~~~

#### 5.1.1.2 集合库使用说明


Copy Folder to Arduino/libraries


~~~c++

#include <GY80.h>

//Create the GY80 class (here named sensor):
GY80 sensor = GY80();

//For initialization call once:
sensor.begin();

//To get values from all sensors:
GY80_scaled values = sensor.read_scaled;

//See below for the GY80_scaled type.

/*======Measuring functions=======*/

GY80_scaled read_scaled();
//returns scaled values from all sensors

GY80_single_scaled m_read_scaled();
//returns scaled values from magnetometer in microTesla [µT]

GY80_single_scaled a_read_scaled();
//returns scaled accelerometer values in G, 1G = 9.81 m/s2

GY80_single_scaled g_read_scaled();
//returns scaled gyroscope values in dps, 6dps = 1rpm

float p_read_scaled();
//returns pressure value in bar

float p_read_altitude();
/*returns altitude in m - not accurate, 
better used only for measuring altitude differences 
and over a short time as air pressure changes with time*/

float t_read_scaled();
//get temperature value in degree celsius


/*======Measuring functions [raw values]=======*/

GY80_raw read_raw();
//returns raw values from all sensors

GY80_single_raw m_read_raw();
//returns raw values from magnetometer

GY80_single_raw a_read_raw();
//returns raw accelerometer values

GY80_single_raw g_read_raw();
//returns raw gyroscope values 

uint32_t p_read_raw();
//returns raw pressure value

uint16_t t_read_raw();
//get raw temperature value


/*======Functions for configuration=======*/

void m_set_scale(uint8_t scale);
//set magnetometer full scale range [values in µT]
  GY80_m_scale_88
  GY80_m_scale_130
  GY80_m_scale_190
  GY80_m_scale_250
  GY80_m_scale_400
  GY80_m_scale_470
  GY80_m_scale_560
  GY80_m_scale_810 <-default

void a_set_scale(uint8_t scale);
//set accelerometer full scale range in G
  GY80_a_scale_2
  GY80_a_scale_4
  GY80_a_scale_8
  GY80_a_scale_16 <-default

void a_set_bw(uint8_t bw);
//set measuring frequency, can be:
  GY80_a_bw_3200  // 1600Hz Bandwidth   140µA IDD
  GY80_a_bw_1600  //  800Hz Bandwidth    90µA IDD
  GY80_a_bw_800   //  400Hz Bandwidth   140µA IDD
  GY80_a_bw_400   //  200Hz Bandwidth   140µA IDD
  GY80_a_bw_200   //  100Hz Bandwidth   140µA IDD
  GY80_a_bw_100   //   50Hz Bandwidth   140µA IDD
  GY80_a_bw_50    //   25Hz Bandwidth    90µA IDD
  GY80_a_bw_25    // 12.5Hz Bandwidth    60µA IDD
  GY80_a_bw_12_5  // 6.25Hz Bandwidth    50µA IDD (default value)
  GY80_a_bw_6_25  // 3.13Hz Bandwidth    45µA IDD
  GY80_a_bw_3_13  // 1.56Hz Bandwidth    40µA IDD
  GY80_a_bw_1_56  // 0.78Hz Bandwidth    34µA IDD
  GY80_a_bw_0_78  // 0.39Hz Bandwidth    23µA IDD
  GY80_a_bw_0_39  // 0.20Hz Bandwidth    23µA IDD
  GY80_a_bw_0_20  // 0.10Hz Bandwidth    23µA IDD
  GY80_a_bw_0_10  // 0.05Hz Bandwidth    23µA IDD

void g_set_scale(uint8_t scale);
//sets gyroscpe scale in dps, can be:
  GY80_g_scale_250
  GY80_g_scale_500
  GY80_g_scale_2000


/*======Struct types=======*/

//GY80_scaled
    float a_x;
    float a_y;
    float a_z;

    float m_x;
    float m_y;
    float m_z;

    float g_x;
    float g_y;
    float g_z;

    float p;
    float t;

//GY80_raw
    int16_t a_x;
    int16_t a_y;
    int16_t a_z;

    int16_t m_x;
    int16_t m_y;
    int16_t m_z;

    int16_t g_x;
    int16_t g_y;
    int16_t g_z;

    uint32_t p;
    uint16_t t;


//GY80_single_raw
    int16_t x;
    int16_t y;
    int16_t z;

//GY80_single_scaled
    float x;
    float y;
    float z;
~~~

### 5.1.2 MPU-6050
MPU6050是一种非常流行的空间运动传感器芯片，可以获取器件当前的三个加速度分量和三个旋转角速度。由于其体积小巧，功能强大，精度较高，不仅被广泛应用于工业，同时也是航模爱好者的神器，被安装在各类飞行器上驰骋蓝天。

随着Arduino开发板的普及，许多朋友希望能够自己制作基于MPU6050的控制系统，但由于缺乏专业知识而难以上手。此外，MPU6050的数据是有较大噪音的，若不进行滤波会对整个控制系统的精准确带来严重影响。

MPU6050芯片内自带了一个数据处理子模块DMP，已经内置了卡尔曼滤波算法，在许多应用中使用DMP输出的数据已经能够很好的满足要求。关于如何获取DMP的输出数据

There are four sensors on this board: I2C Address: 0x68
1. a MEMS (microelectromechanical system) accelerometer  加速度计
加速度计的三轴分量ACC_X、ACC_Y和ACC_Z均为16位有符号整数，分别表示器件在三个轴向上的加速度，取负值时加速度沿座标轴负向，取正值时沿正向。三个加速度分量均以重力加速度g的倍数为单位，能够表示的加速度范围，即倍率可以统一设定，有4个可选倍率：2g、4g、8g、16g。以ACC_X为例，若倍率设定为2g（默认），则意味着ACC_X取最小值-32768时，当前加速度为沿X轴正方向2倍的重力加速度；若设定为4g，取-32768时表示沿X轴正方向4倍的重力加速度，以此类推。显然，倍率越低精度越好，倍率越高表示的范围越大，这要根据具体的应用来设定。

2. gyroscope with 16-bit analog-to-digital converters for 60 micro g and 0.01 degree/second precision, respectively. 角速度计
绕X、Y和Z三个座标轴旋转的角速度分量GYR_X、GYR_Y和GYR_Z均为16位有符号整数。从原点向旋转轴方向看去，取正值时为顺时针旋转，取负值时为逆时针旋转。三个角速度分量均以“度/秒”为单位，能够表示的角速度范围，即倍率可统一设定，有4个可选倍率：250度/秒、500度/秒、1000度/秒、2000度/秒。以GYR_X为例，若倍率设定为250度/秒，则意味着GYR取正最大值32768时，当前角速度为顺时针250度/秒；若设定为500度/秒，取32768时表示当前角速度为顺时针500度/秒。显然，倍率越低精度越好，倍率越高表示的范围越大。


### 5.1.2 地址冲突问题

~~~c++

//.h文件里
//#define HMC5983_Address 0x1E    //把这行注销掉
#define ConfigurationRegisterA 0x00
#define ConfigurationRegisterB 0x01
#define ModeRegister 0x02
#define DataRegisterBegin 0x03

//.cpp 里改成这样
HMC5983::HMC5983(uint8_t Addr)
{
  m_Scale = 0.92
uint8_t HMC5983_Address   = Addr;
  
}
/////////////////////////////////////////////////////////////
主程序里

const int MPU_addr=0x68

HMC5983 compass1（0x1E）；//这个地址要查手册是多少
HMC5983 compass2（0x1F）；//这个地址要查手册是多少
~~~

(1)通常传感器的 IIC address 是不能改的,
   我不认为 HMC5983 的 IIC address 可以改 ??
(2)同一条 IIC bus 上不可以有重复的 IIC slave address
   所以如果你都直接连在一起是不行的 !
(3)如果你一定要两个,
   那可以 try 这样:
   各自的 VDD 各自连到 Arduino 的数字脚, 例如 pin 3 和 pin 5
   其他照你原先接,
   每次只可读取一个,
   把要读的透过 pin 3 或 pin 5 给它电力, 另一个则用 digitalWrite(pin, LOW); 关闭电力
  如果是 5V, 
  假设要读 pin 3 那个,
  就 digitalWrite(5, 0);  digitalWrite(3, HIGH); 
如果 HMC5983 是 3V, 则改这样:
     digitalWrite(5, 0);  analogWrite(3, 185);  // 大约 3.5 Volt
  接着要 delay 一下, 例如 delay(1234);
  然后才下达 IIC 命令

### 5.1.3 MultiWii



***


# 6 Raspberry 和 Arduino 蓝牙通信

## 6.1 pybluez 库

~~~python

#安装配置依赖库
wget https://www.kernel.org/pub/linux/bluetooth/bluez-5.9.tar.xz
tar xvf bluez-5.9.tar.xz
sudo apt-get update
sudo apt-get install -y libusb-dev
sudo apt-get install -y libdbus-1-dev 
sudo apt-get install libudev-dev
sudo apt-get install -y glib2.0
sudo apt-get install -y libical-dev
sudo apt-get install -y libreadline-dev

./configure
make
sudo make install
systemctl status bluetooth
sudo systemctl start bluetooth
sudo systemctl enable bluetooth



mkdir pyblue
cd pyblue
wget https://github.com/karulis/pybluez/archive/master.zip
unzip master.zip
cd pybluez-master

sudo apt-get install libbluetooth-dev
python setup.py install

~~~


### 6.1.1 示例

~~~python
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))
~~~


## 6.1.2代码

~~~python
import bluetooth

target_name = "XXXXXXXX"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with name:", target_name
else:
    print "could not find target bluetooth device nearby"
~~~

## 6.2 连接Drone

Try creating a SP profile to the Pi. Edit the following file:

~~~python
sudo nano /etc/systemd/system/dbus-org.bluez.service
~~~

Find the following line and add a compatibility flag '-C' to the end:

~~~python
ExecStart=/usr/lib/bluetooth/bluetoothd -C
~~~

Additionally, add the following line after the above:

~~~shell
ExecStartPost=/usr/bin/sdptool add SP
~~~

Save and reboot. Try removing the device then repairing and trusting the device with bluetoothctl

~~~python
power on
agent on
#The Bluetooth agent is what manages the Bluetooth 'pairing code'. It can either respond to a 'pairing code' coming in, or can send one out.
scan on
pair XXXX
trust XXXX
#connect XXXX
~~~

Then connect to the device with terminal via:

~~~python
sudo rfcomm watch hci0

#or

#除了bluetoothctl，在Raspbian是shell中可以通过hciconfig来控制蓝牙模块。比如开关蓝牙模块
sudo hciconfig hci0 up   #启动hci设备
sudo hciconfig hci0 down #关闭hci设备
#命令中的hci0指的是0号HCI设备，即树莓派的蓝牙适配器

sudo rfcomm connect 0 XXXX 1

sudo rfcomm watch hci0

#与此同时，你可以用下面命令来查看蓝牙设备的工作日志： 

hcidump
~~~

 Connected /dev/rfcomm0 to XXXX on channel 1


If that doesn't work you can also try adding pi to the lp group

~~~python
sudo adduser pi lp
~~~

~~~python
sudo nano /etc/bluetooth/rfcomm.conf

rfcomm0 {
    bind no;
    device XXXX;
    channel 1;
    comment “Connection to Bluetooth serial module”;
}
~~~
The "bind no" is important, otherwise it will try to autmatically bind, which presents all sorts of problems for actually accessing the device (as it's quite picky about when its associated)

sudo rfcomm connect 0

sudo rfcomm connect rfcomm0 XXXX

~~~python
wget https://sourceforge.net/p/pyserial/code/HEAD/tree/trunk/pyserial/serial/tools/miniterm.py

sudo miniterm.py /dev/rfcomm0
sudo service bluetooth restart
~~~




###两行可行方案

~~~python
sudo hciconfig hci0 up
sudo rfcomm connect 0 XXXX 1
~~~

## 6.3 Python运行外部shell命令

### 6.3.1 subprocess 库

~~~python
#The os.system has many problems and subprocess is a much better way to executing unix command. The syntax is:
import subprocess
subprocess.call("command1")
subprocess.call(["command1", "arg1", "arg2"])

#subprocess模块中只定义了一个类: Popen。可以使用Popen来创建进程，并与进程进行复杂的交互。它的构造函数如下：

subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)


~~~

参数args可以是字符串或者序列类型（如：list，元组），用于指定进程的可执行文件及其参数。如果是序列类型，第一个元素通常是可执行文件的路径。我们也可以显式的使用executeable参数来指定可执行文件的路径。在windows操作系统上，Popen通过调用CreateProcess()来创建子进程,CreateProcess接收一个字符串参数，如果args是序列类型，系统将会通过list2cmdline()函数将序列类型转换为字符串。

参数bufsize：指定缓冲。我到现在还不清楚这个参数的具体含义，望各个大牛指点。

参数executable用于指定可执行程序。一般情况下我们通过args参数来设置所要运行的程序。如果将参数shell设为True，executable将指定程序使用的shell。在windows平台下，默认的shell由COMSPEC环境变量来指定。

参数stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。

参数preexec_fn只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用。

参数Close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。我们不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。

如果参数shell设为true，程序将通过shell来执行。

参数cwd用于设置子进程的当前目录。

参数env是字典类型，用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。

参数Universal_newlines:不同操作系统下，文本的换行符是不一样的。如：windows下用’/r/n’表示换，而Linux下用’/n’。如果将此参数设置为True，Python统一把这些换行符当作’/n’来处理。

参数startupinfo与createionflags只在windows下用效，它们将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等。



~~~python
#To store output to the output variable, run:
import subprocess
p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print "Today is", output

#get real time output:
import subprocess
cmdping = "ping -c4 www.cyberciti.biz"
p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()
~~~


### 6.3.2 超级管理员运行

~~~python
import subprocess
from subprocess import Popen, PIPE

sudo_password = 'My_pass'
command_open = 'sudo hciconfig hci0 up'.split()
command_connect = 'rfcomm connect 0 XXXX 1'.split()

p = Popen(['sudo', '-S'] + command_open, stdin=PIPE, stderr=PIPE,universal_newlines=True)
sudo_prompt = p.communicate(sudo_password + '\n')
p = Popen(['sudo', '-S'] + command_connect, stdin=PIPE, stderr=PIPE,universal_newlines=True)
sudo_prompt = p.communicate(sudo_password + '\n')
~~~

结束超级进程

~~~python
import os
os.system("sudo killall rfcomm")
~~~


### 6.3.3 蓝牙连接完整代码

~~~python
#!/home/pi/miniconda3/envs/py27/bin/
import bluetooth
import subprocess
from subprocess import Popen, PIPE
import time,os

target_name = "XXXX"
killcount=0
target_address = 'XXXX'
sudo_password = 'XXXXXXXX'
command_open = 'sudo hciconfig hci0 up'.split()
command_connect = 'nohup rfcomm connect 0 XXXX 1 > /home/pi/log/rfcomm_XXXX.log 2>&1 &'.split()


def detect_drone():
	nearby_devices = bluetooth.discover_devices(lookup_names = False,flush_cache = True, duration = 10)
	for bdaddr in nearby_devices:
		if bdaddr== target_address:
			return 1
			break
	return 0

def status_blue():
	stdoutdata = subprocess.check_output(["hcitool","con"])
	if "XXXX" in stdoutdata.split():
		print("Bluetooth device is connected")
		return 1
	else:
		return 0

Bluetooth = Popen(['sudo', '-S'] + command_open, stdin=PIPE, stderr=PIPE,universal_newlines=True)
sudo_prompt = Bluetooth.communicate(sudo_password + '\n')

while 1:
	if status_blue():
		time.sleep(3)
	elif detect_drone():
			print ("Found target bluetooth device with name:", target_name)
			print ("Starting rfcomm")
			Bluetooth = Popen(['sudo', '-S'] + command_open, stdin=PIPE, stderr=PIPE,universal_newlines=True)
			sudo_prompt = Bluetooth.communicate(sudo_password + '\n')
			os.system("sudo killall rfcomm")
			time.sleep(2)
			Drone_bluetooth = Popen(['sudo'] + command_connect, stdin=PIPE, stderr=PIPE,universal_newlines=True)
			time.sleep(3)
	else:
			print ("No target bluetooth device nearby")
~~~

We now look for nearby devices using `bluetooth.discover_devices`. I’m adding a few parameters as well. `lookup_names` is set to True so we can get the devices names instead of the just their addresses, and `flush_cache` is also set to True to make sure we always look for fresh information. Finally we set `duration` to 20, meaning we look for devices for up to 20 seconds. This is a bit excessive, but useful when testing.

nohup命令及其输出文件

nohup命令：如果你正在运行一个进程，而且你觉得在退出帐户时该进程还不会结束，那么可以使用nohup命令。该命令可以在你退出帐户/关闭终端之后继续运行相应的进程。nohup就是不挂起的意思(no hang up)。 
一般都是在linux下nohup格式：

~~~shell
nohup command 
或者 
nohup command & 
~~~
这之间的差别是带&的命令行，即使terminal（终端）关闭，或者电脑死机程序依然运行（前提是你把程序递交到服务器上).它把标准输出(STDOUT)和标准错误（STDERR）结果输出到nohup.txt文件这个看似很方便，但是当输出很大的时候，nohup.txt文件会非常大，或者多个后台命令的时候大家都会输出到nohup.txt文件，不利于查找结果和调试程序。所以能够重定向输出会非常方便。下面要介绍标准输出，标准输入 和标准错误了。 
其实我们一直都在用，只是没有注意到，比如 


~~~shell
>./command.sh > output
#这其中的>就是标准输出符号，其实是 1>output 的缩写
>./command.sh 2> output
#这里的2>就是将标准错误输出到output文件里。 
~~~

而`0<`则是标准输入了。 

下面步入正题，重定向后台命令 

~~~shell
nohup ./command.sh > output 2>&1 & 
~~~
解释：前面的nohup和后面的&我想大家都能明白了把。 主要是中间的`2>&1`意思是把标准错误(2)重定向到标准输出中(1)，而标准输出又导入文件output里面,所以结果是标准错误和标准输出都导入文件output里面了。 
至于为什么需要将标准错误重定向到标准输出的原因，那就归结为标准错误没有缓冲区，而stdout有。这就会导致 >output 2>output 文件output被两次打开，而stdout和stderr将会竞争覆盖，这肯定不是我门想要的. 

这就是为什么有人会写成： 
nohup ./command.sh >output 2>output出错的原因了 

最后谈一下/dev/null文件的作用 
这是一个无底洞，任何东西都可以定向到这里，但是却无法打开。 
所以一般很大的stdou和stderr当你不关心的时候可以利用stdout和stderr定向到这里>./command.sh >/dev/null 2>&1 


### 6.3.4 注册为python自动后台运行服务


修改默认环境

~~~python
sudo nano ~/.bashrc

export PATH=/home/pi/miniconda3/envs/py27/bin:$PATH
~~~

~~~shell
sudo nano /etc/rc.local
~~~

~~~shell
nohup /home/pi/miniconda3/envs/py27/bin/python /home/pi/bootwith/bluetooth_drone.py > /home/pi/log/bluetooth_drone.log 2>&1 &
~~~


~~~shell
sudo nano /etc/init.d/bluetooth_drone



#! /bin/sh
# /etc/init.d/noip 

### BEGIN INIT INFO
# Provides:          noip
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
# Description:       A simple script which will start / stop a program a boot / shutdown.
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting bluetooth_drone"
    nohup /home/pi/miniconda3/envs/py27/bin/python /home/pi/bootwith/bluetooth_drone.py > /home/pi/log/bluetooth_drone.log 2>&1 &
    ;;
  stop)
    echo "Stopping bluetooth_drone"
    # kill application you want to stop
    killall -9 rfcomm
    ;;
  *)
    echo "Usage: /etc/init.d/bluetooth_drone {start|stop}"
    exit 1
    ;;
esac

exit 0




sudo chmod +755 /etc/init.d/bluetooth_drone
~~~


测试

~~~shell
sudo /etc/init.d/bluetooth_drone start
sudo /etc/init.d/bluetooth_drone stop
~~~

Register script to be run at startup:

~~~shell
cd /etc/init.d/
sudo update-rc.d bluetooth_drone defaults
sudo update-rc.d -f bluetooth_drone remove
~~~






## 6.4 交换数据

### 6.4.1安装配置库文件

~~~shell
mkdir pymulti
wget https://github.com/alduxvm/pyMultiWii/archive/master.zip
unzip master.zip
python setup.py install
~~~

### 6.4.2 接收数据 

~~~python
#!/usr/bin/env python

"""show-attitude.py: Script to ask the MultiWii Board attitude and print it."""

from pymultiwii import MultiWii
from sys import stdout

if __name__ == "__main__":

    #board = MultiWii("/dev/ttyUSB0")
    board = MultiWii("/dev/rfcomm0")
    try:
        while True:
            board.getData(MultiWii.RAW_IMU)
            #print board.attitude #uncomment for regular printing

            # Fancy printing (might not work on windows...)
            message = "ax = {:+.0f} \t ay = {:+.0f} \t az = {:+.0f} gx = {:+.0f} \t gy = {:+.0f} \t gz = {:+.0f} mx = {:+.0f} \t my = {:+.0f} \t mz = {:+.0f} \t elapsed = {:+.4f} \t" .format(float(board.rawIMU['ax']),float(board.rawIMU['ay']),float(board.rawIMU['az']),float(board.rawIMU['gx']),float(board.rawIMU['gy']),float(board.rawIMU['gz']),float(board.rawIMU['mx']),float(board.rawIMU['my']),float(board.rawIMU['mz']),float(board.attitude['elapsed']))
            stdout.write("\r%s" % message )
            stdout.flush()
            # End of fancy printing
    except Exception,error:
        print "Error on Main: "+str(error)
~~~


### 6.4.3 发送数据

~~~python
#!/usr/bin/env python

"""test-send.py: Test script to send RC commands to a MultiWii Board."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2016 Altax.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pymultiwii import MultiWii

if __name__ == "__main__":

    #board = MultiWii("/dev/ttyUSB0")
    board = MultiWii("/dev/rfcomm0")
    try:
        while True:
        	#example of 8 RC channels to be send
            data = [1500,1550,1600,1560,1000,1040,1000,1000]
            
            # Old function 
            #board.sendCMD(16,MultiWii.SET_RAW_RC,data)

            #New function that will receive attitude after setting the rc commands
            board.sendCMDreceiveATT(16,MultiWii.SET_RAW_RC,data)
            
            print board.attitude
    except Exception,error:
        print "Error on Main: "+str(error)
~~~


!!! hint "RC alias"
	|No|Name|Range|
	| ------------- |:---------------:| :---------------:|
	|0|ROLL|1020~2000|
	|1|PITCH|1020~2000|
	|2|YAW|1020~2000|
	|3|THROTTLE|1000~2000|
	|4|AUX1|flight mode selection|
	|5|AUX2|tuning and calibration|
	|6|AUX3|overwrite CAM pitch (AUX1-AUX4) disable manual input and free the AUX channel|
	|7|AUX4||

测得解锁数据代码

!!! attention "解锁 日本手"
	|最小|居中|最大|
	| ------------- |:---------------:| :---------------:| 
	|throttle|pitch前进|yaw|
	|油门|roll翻滚|右自旋|


数值 `[1500,1500,2000,1020]`

/home/pi/miniconda3/envs/py27/lib/python2.7/site-packages/pymultiwii-1.6-py2.7.egg


### 6.4.4 蓝牙数据嗅探

$$验证解锁数据代码$$

~~~python
24:4d:3c:00:65:65:24:4d:3c:00:6c:6c:24:4d:3c:00:6d:6d:24:4d:3c:00:6a:6a:24:4d:3c:00:71:71:24:4d:3c:00:66:66

ee
ll
mm
jj
qq
ff
~~~

### 6.4.5 解锁


~~~python
from pymultiwii import MultiWii
import time

if __name__ == "__main__":

    board = MultiWii("/dev/rfcomm0")
    try:
        board.arm()
        print "Board is armed now!"
        print "In 3 seconds it will disarm..."
        time.sleep(3)
        board.disarm()
        print "Disarmed."
        time.sleep(3)

    except Exception,error:
        print "Error on Main: "+str(error)
~~~


库文件定义

~~~python
    def arm(self):
        timer = 0
        start = time.time()
        while timer < 0.5:
            data = [1500,1500,2000,1000]
            self.sendCMD(8,MultiWii.SET_RAW_RC,data)
            time.sleep(0.05)
            timer = timer + (time.time() - start)
            start =  time.time()

    def disarm(self):
        timer = 0
        start = time.time()
        while timer < 0.5:
            data = [1500,1500,1000,1000]
            self.sendCMD(8,MultiWii.SET_RAW_RC,data)
            time.sleep(0.05)
            timer = timer + (time.time() - start)
            start =  time.time()
~~~

### 6.4.6 接收信息并显示为图像

安装matplotlib库文件

~~~sh
source activate py27
conda install matplotlib
~~~

python-pyqtgraph库文件

Pyside为依赖库

~~~sh
sudo nano /etc/apt/sources.list
deb http://luke.campagnola.me/debian dev/
sudo apt-get install python-pyqtgraph
sudo apt-get install python-pyside 
sudo apt-get install python-qt4 


sudo apt-get install build-essential git cmake libqt4-dev libphonon-dev python2.7-dev libxml2-dev libxslt1-dev qtmobility-dev libqtwebkit-dev
pip install wheel
wget https://pypi.python.org/packages/source/P/PySide/PySide-1.2.4.tar.gz
tar -xvzf PySide-1.2.4.tar.gz
cd PySide-1.2.4
python setup.py bdist_wheel --qmake=/usr/bin/qmake-qt4

~~~


# 集成串口通信和蓝牙通信

~~~python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#======导入库文件======
#串口通信
import serial
import json
#蓝牙通信
from pymultiwii import MultiWii
import time

#======初始化全局变量======
timeN=1
armN=0
armSwich=1
bluePort = "/dev/rfcomm0"
serialPort = "/dev/ttyACM0"
arduinoSer = serial.Serial(serialPort, 9600)
arduinoDrone = MultiWii(bluePort)

#arduinoDrone.arm()
#======主程序======
while arduinoSer.isOpen():
  #======时间同步======
  #if timeN:
  # arduinoSer.write(time.time())
  # timeN=0
  rawLigne = arduinoSer.readline()
  try:
    tempeData = json.loads(rawLigne)
    if (tempeData["Triger"]):
      #{u'Swich': 1, u'Triger': 1, u'IR': 0, u'Stick': [592, 598], u'Power': 392}
      #======红外模块======
      #======四轴飞行器======
      #初始赋值
      #中间位置  528 537 
      #100 1000
      rawRoll = tempeData['Stick'][0]
      dataRoll = rawRoll+1000#/(999-100)*980+1020
      rawPitch = tempeData['Stick'][1]
      dataPitch = rawPitch+1000#/(999-100)*980+1020
      rawThrottle = tempeData['Power']
      dataThrottle = rawThrottle+950#/(999-100)*980+1020
      ifArm = tempeData['Swich']
      if ifArm==0:
        armN+=1
      #print armN
      #全局变量控制解锁。如果该变量/10%2等于1，则为奇数*10，那么解锁，否则锁定
      #解决按钮延迟的问题
      if armN // 10 % 2:
        if armSwich:
          arduinoDrone.arm()
          armSwich=0
          print 'unlocked'
        dataCMD = [dataRoll,dataPitch,1500,dataThrottle]
        #dataArm = [1500,1500,2000,1000]
        #[ROLL,PITCH,YAW,THROTTLE]
        arduinoDrone.sendCMD(8,MultiWii.SET_RAW_RC,dataCMD)
        print dataCMD
      else :
        if armSwich==0:
          #arduinoDrone.disarm()
          armSwich=1
          print 'locked'
        print 'StandBy'
    else:
      #======树莓派Django模块======
      #{u'Distance': 4, u'Temperature': 20, u'Light': 191, u'Humity': 63, u'Time': 1504611050, u'Triger': 0}
      print '存到数据库Django==>', tempeData
  except:
    # do nothing, not a valid JSON
    pass
~~~





***

# 7 VPS Web配置

## 7.1 初始化配置

安装sudo和nano

```css
apt-get update
apt-get upgrade
apt-get install sudo
apt-get install -y nano
```

添加账户

```css
adduser XXXX

usermod -a -G sudo XXXX
sudo passwd root

```

配置SSH

```
sudo nano /etc/ssh/sshd_config
```

修改配置文件

```css
PasswordAuthentication no
PermitRootLogin no
port 80
```

重启SSH服务

```css
sudo service ssh restart
```

80 端sslh口转发

```
sudo apt-get install libconfig-dev
wget https://github.com/yrutschle/sslh/archive/v1.18.tar.gz
sudo tar -C ./ -xzf v1.18.tar.gz
sudo make install
sudo cp sslh-fork /usr/local/sbin/sslh
sudo cp sslh-fork /etc/init.d/sslh
sudo cp basic.cfg /etc/sslh.cfg
sudo nano /etc/sslh.cfg
sudo update-rc.d sslh defaults
```



## 7.2 ShadowSocks代理配置

程序及其依赖组件

```css
sudo apt-get install python-pip
sudo pip install shadowsocks
sudo apt-get install python-m2crypto
```

编辑配置文件

```
sudo nano /etc/shadowsocks.json
```

```css
{
"server":"XXXX",
"server_port":XXXX,
"local_address": "127.0.0.1",
"local_port":1080,
"password":"XXXX",
"timeout":300,
"method":"aes-256-cfb"
}
```

```
sudo chmod 755 /etc/shadowsocks.json
sudo useradd ssuser
```

```
sudo nano /etc/rc.local
```

自启动：在 exit 0 这一行的上边加入如下

```
/usr/local/bin/ssserver -c /etc/shadowsocks.json -d start --user ssuser
```

## 7.3 BBR 网络加速

下载并安装内核

```css
wget kernel.ubuntu.com/~kernel-ppa/mainline/v4.11.3/linux-headers-4.11.3-041103_4.11.3-041103.201705251233_all.deb 
wget kernel.ubuntu.com/~kernel-ppa/mainline/v4.11.3/linux-headers-4.11.3-041103-generic_4.11.3-041103.201705251233_amd64.deb
wget kernel.ubuntu.com/~kernel-ppa/mainline/v4.11.3/linux-image-4.11.3-041103-generic_4.11.3-041103.201705251233_amd64.deb
sudo dpkg -i linux-headers-4.11*.deb linux-image-4.11*.deb
```

升级内核

```css
sudo /usr/sbin/update-grub
sudo reboot
```

检查内核，查看内核版本，含有 4.11 就表示 OK 了

```css
uname -a
```

开启BBR

```css
su
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p
```

检查BBR状态

```css
sysctl net.ipv4.tcp_available_congestion_control
#返回值一般为：net.ipv4.tcp_available_congestion_control = bbr cubic reno
sysctl net.ipv4.tcp_congestion_control
#返回值一般为：net.ipv4.tcp_congestion_control = bbr
sysctl net.core.default_qdisc
#返回值一般为：net.core.default_qdisc = fq
lsmod | grep bbr
#返回值有 tcp_bbr 模块即说明bbr已启动
```

## 7.4 HTTPS

### 7.4.1 Create the SSL Certificate

create a self-signed key and certificate pair with OpenSSL in a single command:

```css
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt
```

**The most important line is the one that requests the Common Name (e.g. server FQDN or YOUR name). You need to enter the domain name associated with your server or, more likely, your server's public IP address.**

While we are using OpenSSL, we should also create a strong Diffie-Hellman group, which is used in negotiating [Perfect Forward Secrecy](https://en.wikipedia.org/wiki/Forward_secrecy) with clients.

We can do this by typing:

```
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

This may take a few minutes, but when it's done you will have a strong DH group at `/etc/ssl/certs/dhparam.pem` that we can use in our configuration.

### 7.4.2 Configure Nginx to Use SSL

 #### 7.4.2.1 Configure Nginx to Use SSL

create a new Nginx configuration snippet `self-signed.conf` in the `/etc/nginx/snippets` directory

```
sudo nano /etc/nginx/snippets/self-signed.conf
```

we just need to set the `ssl_certificate` directive to our certificate file and the `ssl_certificate_key` to the associated key. In our case, this will look like this:

```
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
```

#### 8.4.2.2 Create a Configuration Snippet with Strong Encryption Settings

Set Nginx up with a strong SSL cipher suite and enable some advanced features that will help keep our server secure.The parameters we will set can be reused in future Nginx configurations, so we will give the file a generic name:

```
sudo nano /etc/nginx/snippets/ssl-params.conf
```

Finally, you should take take a moment to read up on [HTTP Strict Transport Security, or HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security), and specifically about the ["preload" functionality](https://hstspreload.appspot.com/). Preloading HSTS provides increased security, but can have far reaching consequences if accidentally enabled or enabled incorrectly. In this guide, we will not preload the settings, but you can modify that if you are sure you understand the implications:

```
# from https://cipherli.st/
# and https://raymii.org/s/tutorials/Strong_SSL_Security_On_nginx.html

ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
ssl_ecdh_curve secp384r1;
ssl_session_cache shared:SSL:10m;
ssl_session_tickets off;
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8 8.8.4.4 valid=300s;
resolver_timeout 5s;
# Disable preloading HSTS for now.  You can use the commented out header line that includes
# the "preload" directive if you understand the implications.
#add_header Strict-Transport-Security "max-age=63072000; includeSubdomains; preload";
add_header Strict-Transport-Security "max-age=63072000; includeSubdomains";
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;

ssl_dhparam /etc/ssl/certs/dhparam.pem;
```

#### 8.4.2.3 Adjust the Nginx Configuration to Use SSL

Now that we have our snippets, we can adjust our Nginx configuration to enable SSL.

Before we go any further, let's back up our current server block file:

```
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
```

Now, open the server block file to make adjustments:

```
sudo nano /etc/nginx/sites-available/default
```

we need to start a new server block directly below to contain the remaining configuration. We can uncomment the two `listen` directives that use port 443. We can add `http2` to these lines in order to enable HTTP/2 within this block. Afterwards, we just need to include the two snippet files we set up:

```
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name XXXX;
    return 301 https://$server_name$request_uri;
}

server {

    # SSL configuration

    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;
    include snippets/self-signed.conf;
    include snippets/ssl-params.conf;
    root /var/www/html;
    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;
}
```

####  Allow Both HTTP and HTTPS Traffic

(Alternative Configuration)

```
server {
    #listen 80 default_server;
    #listen [::]:80 default_server;
    listen 443 ssl http2 default_server;
    listen [::]:443 ssl http2 default_server;

    server_name gliang.eu;
    include snippets/self-signed.conf;
    include snippets/ssl-params.conf;
    location / {
      # First attempt to serve request as file, then
      # as directory, then fall back to displaying a 404.
      try_files $uri $uri/ =404;
        }
    root /var/www/html;
    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;

  }
```

### 7.4.3 Adjust the Firewall

see the available profiles by typing:

```
sudo ufw app list
```

You should see a list like this:

```
OutputAvailable applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH

```

You can see the current setting by typing:

```
sudo ufw status

```

It will probably look like this, meaning that only HTTP traffic is allowed to the web server:

```
OutputStatus: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere
Nginx HTTP                 ALLOW       Anywhere
OpenSSH (v6)               ALLOW       Anywhere (v6)
Nginx HTTP (v6)            ALLOW       Anywhere (v6)

```

To additionally let in HTTPS traffic, we can allow the "Nginx Full" profile and then delete the redundant "Nginx HTTP" profile allowance:

```
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'

```

Your status should look like this now:

```
sudo ufw status

OutputStatus: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere
Nginx Full                 ALLOW       Anywhere
OpenSSH (v6)               ALLOW       Anywhere (v6)
Nginx Full (v6)            ALLOW       Anywhere (v6)
```

### 7.4.4 Enable the Changes in Nginx

Now that we've made our changes and adjusted our firewall, we can restart Nginx to implement our new changes.

First, we should check to make sure that there are no syntax errors in our files. We can do this by typing:

```
sudo nginx -t
```

If everything is successful, you will get a result that looks like this:

```
Outputnginx: [warn] "ssl_stapling" ignored, issuer certificate not found
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

We can safely restart Nginx to implement our changes:

```
sudo systemctl restart nginx
```



### 7.4.5 Let’s Encrypt

 **Install**

On Ubuntu systems, the Certbot team maintains a [PPA](https://help.ubuntu.com/community/PPA). Once you add it to your list of repositories all you'll need to do is apt-get the following packages.

```
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx
```

Certbot has an Nginx plugin, which is supported on many platforms, and automates both obtaining and installing certs:

```
sudo certbot --nginx
```

Running this command will get a certificate for you and have Certbot edit your Nginx configuration automatically to serve it. If you're feeling more conservative and would like to make the changes to your Nginx configuration by hand, you can use the `certonly`subcommand:

```
sudo certbot --nginx certonly
```

Automating renewal
The Certbot packages on your system come with a cron job that will renew your certificates automatically before they expire. Since Let's Encrypt certificates last for 90 days, it's highly advisable to take advantage of this feature. You can test automatic renewal for your certificates by running this command:

```
sudo certbot renew --dry-run
```

If that appears to be working correctly, you can arrange for automatic renewal by adding a cron or systemd job which runs the following:
certbot renew 


```
git clone https://github.com/certbot/certbot.git
cd certbot
./certbot-auto certonly -d gliang.eu -d www.gliang.eu
```

 gliang.eu www.gliang.eu这样两个域名，会自动使用同一个证书进行认证，一切没问题后会在 /etc/letsencrypt/live/www.embbnux.com 下生成证书


***

#8 Raspbian 和 VPS 站点通信


***

























# 附录A Linux 开机自动启动

!!! Caution "重要！"
  首先将命令更改为后台运行并且任意目录可执行
  `nohup command > /dev/null 2>&1 &`

##A.1 编辑 rc.local

~~~sh
sudo nano /etc/rc.local
~~~

如果只是想开机时执行一些命令在背景运行, 而不是用到复杂的开机服务(例如可以暂停重启什么功能的), 可以这么做:
编辑`/etc/rc.local`, 在 exit 0 前面加入你要执行的命令、脚本。

!!! Danger "绝对路径"
  注意, 这个是很早的执行阶段, 可能PATH没有设置好, 所以最好用绝对路径!!!再说一次, 绝对路径! 包括脚本内!


##A.2 计划事务
 sudo crontab -e 进入计划事务编辑模式, 编辑计划, 加入这么一句`@reboot /path/to/script`. 这个可以加载比较多的指令了, 如果没有正常运行, 请用绝对路径.

##A.3 注册为服务

先把 脚本 放到 `/etc/init.d`目录下。该目录为定义的服务。
图形管理界面可以使用`sysv-rc-conf`, 命令行可以使用service命令.

~~~shell
sudo apt install sysv-rc-conf
sudo sysv-rc-conf
~~~

  这里面service是不同级别的runlevel处理方法, [X]就是开启, 否则是没有开启, 按空格键切换
  要马上操作服务: 按+开启,-停止服务
  q退出


放在/etc/init.d里的是一些可执行的bash脚本. 相应脚本其实是service 运行的. 而开机运行的内容放在`/etc/rc*`内. 有些系统有/etc/rc/文件夹专门放置, 在ubuntu16里面都放在/etc/内. 在`/etc/rc*`的一般是放`/etc/init.d`内文件的链接文件.
在开机启动内容文件夹内一般有`rc*.d`和`rc.local`,一般定义一句话开机启动的就定义在`rc.local`好了, 这个是最后必定加载的文件.因为`rc.local`是等待`/etc/init.d`的服务都开启后才执行的，所以如果`/etc/init.d`中的服务未开启完成，`rc.local`是不会执行的。如启动了`firstboot`服务，将会导致多用户模式下`rc.local`不能执行, 可通过 chkconfig –del 把 firstboot服务去除。服务开启时都会写启动日志，可通过`/var/log/boot.log`查看服务启动与否，再结合`/etc/rc.d/rcx.d/`下服务启动顺序排查哪些服务阻塞了。可结合 `ps awux | grep ServerName` 一起排查。

而`rc*.d`则对应不同开机级数作相应运行, 文件名开头S的表示该服务会加载,K代表该服务不加载:

!!! note "Attention"
  rc0.d: 关机级别 -> shutdown 命令 （千万不要把initdefault 设置为0 ）
  rc1.d: 单用户, 不带网络, 不执行daemon背景程序, 不允许非root登陆 类似安全模式。
  rc2.d: 多用户, 不带网络, 不执行daemon背景程序的级别
  rc3.d: 多用户, 带网络的级别(正常级别)
  rc4.d: 用户自定义
  rc5.d: 多用户带图形界面(一般情况)
  rc6.d: 重启级别 -> reboot 命令
  rcS.d: 在rc?.d之前运行

  !!! caution "Attention"
      runlevel 命令可以知道当前级别. 
      ```
      $ sudo runlevel
      N 3
      ```
      总的加载顺序是: 
      开机init -> rcS.d -> rc0~6.d -> rc.local 
      即使有个服务存在/etc/init.d 
      但要是没有rc的运行级别来运行, 依然是运行不起来的~ 
      sudo init N 就是切换当前操作系统的Runlevel的命令 一般用init 3和init 5


用命令行来设置运行级别的服务可以使用update-rc.d命令, 不同系统该指令有差异.

~~~shell
# Set service at 2,3,4,5 Level
update-rc.d servicename default
# Cancel service at 2,3,4,5 Level
update-rc.d servicename remove
# Cancel service at 2,3,4,5 Level, and delete the symlinks even it exists in /etc/init.d
update-rc.d -f servicename remove
# Set service at giving Level
update-rc.d servicename enable  [S|2|3|4|5]
# Cancel service at giving Level
update-rc.d servicename disable  [S|2|3|4|5]

#设定启动级别 
update-rc.d xxx(脚本名) start 98 2 . 
    #98 为启动序号，
​    #2是系统的运行级别，可自己调整，
​    #注意不要忘了结尾的句点。
    #现在我们到 `/etc/rc2.d` 下，就多了一个 S98mysql 这样的符号链接。
~~~

卸载启动服务脚本

```
$ cd /etc/init.d
$ sudo update-rc.d -f test remove
```

!!! hint "service命令"
    这个命令主要用途是一次性操作服务 (相当于sysv-rc-conf的+-号).

  ~~~shell
  service < option > | --status-all | [ service_name [ command | --full-restart ] ]
  ## 查看所有服务当前的状态
  service --status-all
  ## 开启/重启服务
  service mysql start/restart
  ## 停止服务 
  service mysql stop
  ~~~

##完整实例

`sudo nano /etc/init.d/servicename`

~~~sh
#! /bin/sh
# /etc/init.d/noip 

### BEGIN INIT INFO
# Provides:          noip
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
# Description:       A simple script which will start / stop a program a boot / shutdown.
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting "
    # run application you want to start
    servicename

    ;;
  stop)
    echo "Stopping "
    # kill application you want to stop
    killall servicename

    ;;
  *)
    echo "Usage: /etc/init.d/servicename {start|stop}"
    exit 1
    ;;
esac

exit 0
~~~

Make the script executable:

```
sudo chmod +755 /etc/init.d/servicename
```

测试

```
sudo /etc/init.d/servicename start  
sudo /etc/init.d/servicename stop
```

Register script to be run at startup:

```
cd /etc/init.d/
sudo update-rc.d servicename defaults
```

清除 remove the script from start-up

```
sudo update-rc.d -f servicename remove
```

!!! Danger "Python脚本"
    nohup /home/pi/miniconda3/envs/py27/bin/python name.py > /home/pi/log/name.log 2>&1 &


##A.4 shell脚本

将写好的脚本（.sh文件）放到目录 `/etc/profile.d/` 下，系统启动后就会自动执行该目录下的所有shell脚本。

##A.5 登陆命令行时自动运行

Add your script executable command to the bottom of .bashrc that will run your script every time you log in.

Make sure you are in the pi folder:
`$ cd ~`
Create a file and write a script to run in the file:
`$ sudo nano superscript`
Open up` .bashrc` for configuration:
`$ sudo nano .bashrc`
Scroll down to the bottom and add the line: ./superscript
Save and exit

***


# 附录B Python

## B.0 python学习笔记

### B.0.1基础语法

#### B.0.1.1 输出

print()在括号中加上字符串，就可以向屏幕上输出指定的文字。
~~~CPP
>>>print('hello, world')
>>>print('The quick brown fox', 'jumps over', 'the lazy dog')
The quick brown fox jumps over the lazy dog
#逗号自动转为空格
>>> print('100 + 200 =', 100 + 200)
100 + 200 = 300
~~~

**格式化字符串**

在Python中，采用的格式化方式和C语言是一致的，用%实现

~~~
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
~~~
%d  整数
%f  浮点数
%s  字符串
%x  十六进制整数

指定位数

~~~
>>> '%.2f' % 3.1415926
'3.14'
~~~
如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串。有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%

#### B.0.1.2 输入
~~~
>>> name = input('please enter your name: ')
 #显示引号内字符串，输入任意字符，然后按回车后完成输入。
~~~
input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：

~~~
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
~~~

#### B.0.1.3 数据类型
##### B.0.1.3.1整数
计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示

##### B.0.1.3.2 浮点数/小数
科学计数法表示，把10用e替代

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的。而浮点数运算则可能会有四舍五入的误差。

##### B.0.1.3.3 字符串
字符串是以单引号"或双引号"括起来的任意文本。''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。如果字符串内部既包含'又包含"，可以用转义字符\"或\'来标识。

~~~
>>>'I\'m \"OK\"!'
I'm "OK"!
~~~

转义字符:
\n表示换行，\t表示制表符，\n表示换行，\t表示制表符
用r''表示''内部的字符串默认不转义
~~~
>>> print(r'\\\t\\')
\\\t\\
~~~
Python允许用'''...'''的格式表示多行内容

~~~
>>> print('''line1
... line2
... line3''')
line1
line2
line3

#写成程序
print('''line1
line2
line3''')
~~~

*字符串编码*
计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了*GB2312*编码，用来把中文编进去。
日文编到Shift_JIS里，韩文编到Euc-kr里。为了消除乱码，Unicode应运而生。现代操作系统和大多数编程语言都直接支持Unicode。

ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。
字母A用ASCII编码是十进制的65，二进制的01000001；
字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。
你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间

UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

*现在计算机系统通用的字符编码工作方式：*
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
![记事本编辑](https://www.liaoxuefeng.com/files/attachments/001387245992536e2ba28125cf04f5c8985dbc94a02245e000/0)

网页
![网页](https://www.liaoxuefeng.com/files/attachments/001387245979827634fd6204f9346a1ae6358d9ed051666000/0)


*Python的字符串*

对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

~~~cpp
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'

>>> '\u4e2d\u6587'
'中文'
~~~
由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

Python对bytes类型的数据用带b前缀的单引号或双引号表示：

~~~
x = b'ABC'
~~~
后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
以Unicode表示的str通过encode()方法可以编码为指定的bytes

~~~
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
~~~

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

~~~
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
~~~
要计算str包含多少个字符，可以用len()函数。如果换成bytes，len()函数就计算字节数。

~~~
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
~~~
可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

~~~
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
~~~
**必须并且要确保文本编辑器正在使用UTF-8 without BOM编码**

##### B.0.1.3.4布尔值
在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
~~~
>>> True
True
>>> False
False
>>> 3 > 2
True
>>> 3 > 5
False
~~~
布尔值可以用and、or和not运算。

and运算是与运算，只有所有都为True，and运算结果才是True；or运算是或运算，只要其中有一个为True，or运算结果就是True；not运算是非运算，它是一个单目运算符，把True变成False，False变成True。

##### B.0.1.3.5 空值
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
##### B.0.1.3.6 列表 list
list是一种有序的集合，可以随时添加和删除其中的元素。
列出班里所有同学的名字

~~~
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']
~~~
用len()函数可以获得list元素的个数

~~~
>>> len(classmates)
3
~~~

取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：

~~~
>>> classmates[-1]
'Tracy'
~~~

list是一个可变的有序表

*追加*

~~~
#追加元素到末尾
>>> classmates.append('Adam')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']

#元素插入到指定的位置
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
~~~

*删除*

~~~
#删除list末尾的元素
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']

#删除指定位置的元素
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
~~~

*替换*

~~~
>>> classmates[1] = 'Sarah'
>>> classmates
['Michael', 'Sarah', 'Tracy']
~~~

list里面的元素的数据类型也可以不同

~~~
>>> L = ['Apple', 123, True]

#list元素也可以是另一个list
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
>>> len(s)
4
~~~
要拿到'php'可以写s[2][1]，因此s可以看成是一个二维数组

##### B.0.1.3.7 字典 dict
dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
例如要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
~~~
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
~~~
list越长，耗时越长。
如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
~~~
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
~~~
dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

dict是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。

*添加*
除了初始化时指定外，还可以通过key放入数据
~~~
>>> d['Adam'] = 67
>>> d['Adam']
67
~~~
*修改*
由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉

要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
~~~
>>> 'Thomas' in d
False
~~~
二是通过dict提供的get方法，如果key不存在，可以返回None(返回None的时候Python的交互式命令行不显示结果。)，或者自己指定的value
~~~
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
~~~
*删除*
要删除一个key，用pop(key)方法，对应的value也会从dict中删除

~~~
>>> d.pop('Bob')
75
>>> d
{'Michael': 95, 'Tracy': 85}
~~~

dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

| dict          |          list          |
| ------------- | :--------------------: |
| 查找和插入的速度极快    |   查找和插入的时间随着元素的增加而增加   |
| 不会随着key的增加而变慢 |      占用空间小，浪费内存很少      |
| 需要占用大量的内存     | **dict是用空间来换取时间的一种方法** |

注意：
dict的key必须是不可变对象。因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

~~~
>>> key = [1, 2, 3]
>>> d[key] = 'a list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
~~~


##### B.0.1.3.8 Set  无序和无重复元素的集合

~~~
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
~~~
传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。重复元素在set中自动被过滤。


add(key)方法可以添加元素到set中

~~~
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
~~~
通过remove(key)方法可以删除元素

~~~
>>> s.remove(4)
>>> s
{1, 2, 3}
~~~

set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”


##### B.0.1.3.9  不可变对象
str是不变对象，而list是可变对象。
对于可变对象list 操作，list内部的内容是会变化的

~~~
>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
~~~

而对于不可变对象str进行操作

~~~
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc'
~~~
要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'

当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了

所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

##### B.0.1.3.10 tuple
tuple 有序列表：元组
tuple和list非常类似，但是tuple一旦初始化就不能修改。没有append()，insert()这样的方法。所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来：

~~~
#空的
>>> t = ()

#定义一个只有1个元素的tuple时，加一个逗号,，以免成数学计算意义上的括号。
 >>> t = (1,)

#“可变的”tuple
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])

~~~
表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的



##### B.0.1.3.11 变量
变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头

在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量

~~~
a = 123 # B是整数
print(a)
a = 'ABC' # B变为字符串
print(a)
~~~
这种变量本身类型不固定的语言称之为动态语言。

##### B.0.1.3.12 常量
用全部大写的变量名表示常量只是一个习惯上的用法。
·PI = 3.14159265359·


#### B.0.1.4 运算
整数的除法也是精确的。
在Python中，有两种除法，一种除法是/
~~~
 >>>9 / 3
3.0
~~~
还有一种除法是//，称为地板除，两个整数的除法仍然是整数
~~~
>>> 10 // 3
3
~~~
因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数

~~~
>>> 10 % 3
1
~~~

#### B.0.1.5 逻辑语句

##### B.0.1.5.1 if语句

~~~
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#简写
if x:
    print('True')
~~~
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
##### B.0.1.5.2循环

###### B.0.1.5.2.1  for...in
~~~
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
~~~

计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数

~~~
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
~~~
###### B.0.1.5.2.2 while 循环

~~~
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
~~~

### B.0.2 函数
#### B.0.2.1 定义

~~~
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
~~~
#### B.0.2.2 调用

~~~
>>> int('123')
123
>>> int(12.34)
12
>>> float('12.34')
12.34
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
>>> bool('')
False

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
>>> a = abs # 变量a指向abs函数
>>> a(-1) # 所以也可以通过a调用abs函数
1
~~~
#### B.0.2.3 参数

定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

##### B.0.2.3.1 位置参数

~~~
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
~~~
##### B.0.2.3.2 默认参数

新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用。这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2

~~~python
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
~~~

设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
二当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
使用默认参数最大的好处是能降低调用函数的难度。

```python
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

    enroll('Adam', 'M', city='Tianjin')
```
但是默认参数有个最大的坑。默认参数必须指向不变对象！
先定义一个函数，传入一个list，添加一个END再返回

```python
def add_end(L=[]):
    L.append('END')
    return L

  #当你正常调用时，结果似乎不错
  >>> add_end([1, 2, 3])
[1, 2, 3, 'END']
>>> add_end(['x', 'y', 'z'])
['x', 'y', 'z', 'END']

#当你使用默认参数调用时，一开始结果也是对的
>>> add_end()
['END']

#但是，再次调用add_end()时，结果就不对了
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
```
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

要修改上面的例子，我们可以用None这个不变对象来实现

```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

##### B.0.2.3.3 可变参数

~~~python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
~~~
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数

如果已经有一个list或者tuple，要调用一个可变参数

~~~python
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
~~~
*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

##### B.0.2.3.4 关键字参数

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

~~~python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
~~~
可以传入任意个数的关键字参数

~~~python
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
~~~
关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去

~~~python
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#或简化
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
~~~
******extra表示把extra这个dict的所有key-value用关键字参数传入到函数的****kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

**命名关键字参数**
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
检查是否有city和job参数

~~~python
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
~~~

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数

~~~python
def person(name, age, *, city, job):
    print(name, age, city, job)
~~~

和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*

~~~python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
~~~

命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错。由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。

命名关键字参数可以有缺省值，从而简化调用

~~~python
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
~~~

##### B.0.2.3.5 参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
  1.必选参数
  2.默认参数
  3.可变参数
  4.命名关键字参数
  5.关键字参数

~~~python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
~~~

在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去

~~~python
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
~~~

通过一个tuple和dict，你也可以调用上述函数

~~~python
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
~~~

**所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的**

#### B.0.2.4 递归

在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

~~~python
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
~~~

递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)

解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：

~~~python
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
~~~

可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。


fact(5)对应的fact_iter(5, 1)的调用如下

~~~python
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
~~~

尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。


基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。


### B.0.3 高级特性

在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。

基于这一思想，Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。

#### B.0.3.1 切片

一行代码取一个list的前3个元素

~~~python
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

>>> L[:3]
['Michael', 'Sarah', 'Tracy']
~~~

L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。如果第一个索引是0，还可以省略

倒数切片

~~~python
>>> L[-2:]
['Bob', 'Jack']
>>> L[-2:-1]
['Bob']
~~~

创建一个0-99的数列

~~~python
L = list(range(100))

#前10个数，每两个取一个
>>> L[:10:2]
[0, 2, 4, 6, 8]

#所有数，每5个取一个
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

#只写[:]就可以原样复制一个list
>>> L[:]
[0, 1, 2, 3, ..., 99]
~~~

tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

~~~python
>>> (0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)
~~~

字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

~~~python
>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[::2]
'ACEG'
~~~

#### B.0.3.2 迭代

Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

~~~python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
...
a
c
b
~~~

默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

迭代字符

~~~python
>>> for ch in 'ABC':
...     print(ch)
...
A
B
C
~~~

迭代list变成索引-元素对

~~~python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
~~~

可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
判断一个对象是可迭代对象

~~~python
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
~~~

而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

使用isinstance()判断一个对象是否是Iterator对象

~~~python
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
~~~
list、dict、str等数据类型不是Iterator。因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


Python的for循环本质上就是通过不断调用next()函数实现的

~~~python
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
~~~


#### B.0.3.3 列表生成

生成[1x1, 2x2, 3x3, ..., 10x10]列表

~~~python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
~~~

还可以筛选出仅偶数的平方

~~~python
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
~~~

使用两层循环，可以生成全排列

~~~python
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
~~~

可以使用两个变量来生成list

~~~python
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']
~~~

所有的字符串变成小写

~~~python
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
~~~

#### B.0.3.4 生成器
一边循环一边计算的机制，称为生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

~~~python
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
~~~

如果要一个一个打印出来
通过next()函数获得generator的下一个返回值
或者使用for循环，因为generator也是可迭代对象

比如斐波拉契数列：除第一个和第二个数外，任意一个数都可由前两个数相加得到
1, 1, 2, 3, 5, 8, 13, 21, 34, ...

~~~python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
~~~

赋值语句
a, b = b, a + b
相当于：

~~~python
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
~~~

要把fib函数变成generator，只需要把print(b)改为yield b就可以了

~~~python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
~~~

### B.0.4 OOP (object-oriented design)

编程的发展已经从简单控制流中按步的指令序列进入到更有组织的方式中，依靠代码块可以形成命名子程序和完成既定的功能。结构化的或过程性编程可以让我们把程序组织成逻辑块，以便重复或重用

!!! Question "实质"
    如果我们能对数据加上动作呢？如果我们所创建和编写的数据片段，是真实生活中实体的模型，内嵌数据体和动作呢？
    如果我们能通过一系列已定义的接口(又称存取函数集合)访问数据属性，像自动取款机卡或能访问你的银行帐号的个人支票，我们就有了一个“对象”系统，从大的方面来看，每一个对象既可以与自身进行交互，也可以与其它对象进行交互。
!!! Attention "实现方式与类比"
    数据层和逻辑层现在由一个可用以创建这些对象的简单抽象层来描述。类提供了这样一些对象的定义，实例即是这些定义的实现。
    C++可以被认为“更好的C”; 
    Java，则要求万物皆类,一个源文件对应一个类定义；
    在 Python 中，一切皆对象。

!!! Question "为什么要OOP"
    考虑用 OOD 来工作的一个最重要的原因，在于它直接提供建模和解决现实世界问题和情形的途径

相关术语

* [ ] 抽象/实现 
* [ ] 封装/接口 
* [x] 合成:彼此是“有一个”的关系
* [x] 派生/继承/继承结构:继承结构表示多“代”派生，可以描述成一个“族谱”，连续的子类，与祖先类都有关系。
* [ ] 泛化/特化:子类可以认为同祖先类是“是一个”的关系
* [ ] 多态
* [ ] 自省/反射:查出传入的一个对象有什么能力


!!! Unknown "Python"
    面向对象编程主要有两个主题:
    1. 类
    2. 实例
    类是对象的定义，而实例是"真正的实物"，它存放了类中所定义的对象的具体信息。
    object 是“所有类之母”。如果你的类没有继承任何其他父类，object 将作为默认的父类。
    工厂制造机器相当于类，而生产出来的玩具就是它们各个类的实例。尽管每个实例都有一个基本的结构，但各自的属性像颜色或尺寸可以改变-----这就好比实例的属性。
    创建一个实例的过程称作实例化

  ~~~python
  myFirstObject = MyNewObjectType() 
  ~~~
  我们改进类的方式之一就是给类添加功能(通俗的名字叫方法)。

  ~~~python
  class MyDataWithMethod(object):  # 定义类 
  def printFoo(self):  # 定义方法 
  print 'You invoked printFoo()!' 

  #调用
  >>> myObj = MyDataWithMethod()  # 创建实例 
  >>> myObj.printFoo()  # 现在调用方法 
  You invoked printFoo()! 
  ~~~

  self 参数存在于所有方法声明中。代表实例对象本身。在其它语言中，self 称为“this”。

  特殊的方法__init__()，子类化及继承。
  Python 创建实例后，在实例化过程中，调用__init__()方法，当一个类被实例化时，就可以定义额外的行为，如果不存在默认的参数，那么传给__init__()的两个参数在实例化时是必须的。

  ~~~python
  class AddrBookEntry(object): # 类定义 
  'address book entry class' 
   def __init__(self, nm, ph): # 定义构造器  
     self.name = nm  # 设置 name 
     self.phone = ph  # 设置 phone 
     print 'Created instance for:', self.name 
   def updatePhone(self, newph):  # 定义方法 
     self.phone = newph 
     print 'Updated phone# for:', self.name 

  #创建
  >>> john = AddrBookEntry('John Doe', '408-555-1212') #为 John Doe 创建实例 
  >>> jane = AddrBookEntry('Jane Doe', '650-555-1212') #为 Jane Doe 创建实例
  
  #方法调用（通过实例）
  >>> john.updatePhone('415-555-1212') #更新 John Doe 的电话 
  >>> john.phone 
  '415-555-1212' 

  #定义子类
  class EmplAddrBookEntry(AddrBookEntry): 
  'Employee Address Book Entry class'#员工地址本类 
      def __init__(self, nm, ph, id, em):  
          AddrBookEntry.__init__(self, nm, ph)  
          self.empid = id #未绑定的不是通过实例的方法调用 需要:
          self.email = em #显式传递 self 实例对象给基类构造器
   
      def updateEmail(self, newem): 
          self.email = newem 
          print 'Updated e-mail address for:', self.name 

  #创建子类
  >>> john = EmplAddrBookEntry('John Doe', '408-555-1212',42, 'john@spam.doe') 
  Created instance for: John Doe  #给 John Doe 创建实例
  ~~~



#### B.0.4.1 创建类 

~~~python
class ClassName(bases): 
'class documentation string' #'类文档字符串' 
class_suite #类体 
~~~

!!! Attention "命名"
    类名通常由大写字母打头。数据值应该使用名词作为名字，方法使用谓词（动词加对象）。


#### B.0.4.2 类属性
